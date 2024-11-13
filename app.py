from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)
db_kriteria = "database/kriteria.xlsx"

def read_data():
    return pd.read_excel(db_kriteria)

def save_data(df):
    df.to_excel(db_kriteria, index=False)

@app.route("/")
def index():
    df = read_data()
    data = df.to_dict(orient="records")
    return render_template("index.jinja", data=data)

@app.route("/tambah", methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        kriteria = request.form["kriteria"]
        df = read_data()
        df = df._append({"kriteria" : kriteria}, ignore_index=True)
        save_data(df)
        return redirect(url_for("index"))
    return render_template("tambah.jinja")

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    df = read_data()
    data_to_edit = df.loc[id].to_dict() 
    
    if request.method == 'POST' :
        kriteria = request.form["kriteria"]
        df.loc[id, "kriteria"] = kriteria
        save_data(df)
        return redirect(url_for("index"))
    return render_template("edit.jinja", data=data_to_edit)

@app.route("/hapus/<int:id>")
def hapus(id):
    df = read_data()
    df = df.drop(id)
    save_data(df)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(port=5000, debug=True)