from flask import Flask, render_template, request , jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("forms.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    print("Received file:", file.filename)
    print("file", file)

    if file.filename.endswith(".csv"):
        path = "userfile/" + file.filename
        file.save(path)
        return f"File '{file.filename}' uploaded successfully!"
    
        df = pd.read_csv("userfile/names_csv.csv")
        print(df.head())

        minimum_fees = df["fee"].min()
        maximum_fees = df["fee"].max()
        total_students = df["fee"].count()
        average_fees = df["fee"].mean()

        response = {"minimum_fees": minimum_fees,
                    "maximum_fees": maximum_fees,
                    "total_students": total_students,
                    "average_fees": average_fees}
        
        return jsonify(response)

    else:
        return "Invalid file type. Please upload a CSV file."

if __name__ == "__main__":
    app.run(debug=True, port=5002)