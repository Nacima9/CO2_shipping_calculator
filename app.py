import os
from flask import Flask, render_template, request
import pandas as pd
from services.co2_calculation import calculate_co2
from services.data_loader import load_data
from services.statistics_calculation import calculate_total_co2_per_year, calculate_average_co2_per_year




UPLOAD_FOLDER = "data/uploads"
ALLOWED_EXTENSIONS = {"csv", "xlsx", "xls"}
DEV_MODE = True
TEST_DATA_PATH = "data/uploads/co2_shipping_testdataCSV.csv"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


# Entwicklungsmodus mit feste Testdatei
@app.route("/", methods=["POST"])
def uploadData():
    data_preview = None
    error = None
    df = None
    rows = []
    yearly_totals= {}
    yearly_averages = {}

    try:
        if DEV_MODE:
            df = load_data(TEST_DATA_PATH)

        elif request.method == "POST":
            file = request.files.get("file")

            if not file or file.filename == "":
                error = "Keine Datei ausgewählt"
            elif not allowed_file(file.filename):
                error = "Dateiformat nicht unterstützt"
            else:
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(filepath)
                df = load_data(filepath)

        if df is not None:
            data_preview = {
                "rows": df.shape[0],
                "columns": df.shape[1],
                "column_names": list(df.columns)
            }
            for _, row in df.iterrows():
                co2 = calculate_co2(row)
                row_dict = row.to_dict()
                row_dict["co2_kg"] = round(co2, 2)

                rows.append(row_dict)
            yearly_totals = calculate_total_co2_per_year(rows)
            yearly_averages = calculate_average_co2_per_year(rows)

    except Exception as e:
        error = f"Fehler beim Einlesen der Datei: {e}"

    return render_template(
        "index.html",
        dev_mode=DEV_MODE,
        data=data_preview,
        error=error,
        rows=rows,
        yearly_totals=yearly_totals,
        yearly_averages=yearly_averages
    )



if __name__ == "__main__":
    app.run(debug=True)

