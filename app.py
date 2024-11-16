from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)
db_kriteria = "database/tb_kriteria.xlsx"
db_ahli = "database/tb_ahli.xlsx"

def read_kriteria():
    return pd.read_excel(db_kriteria)

def save_kriteria(df):
    df.to_excel(db_kriteria, index=False)

def read_ahli():
    return pd.read_excel(db_ahli)

def save_ahli(df):
    df.to_excel(db_ahli, index=False)
    
def generate_kode_ahli(df):
    if df.empty:
        return "P1"
    
    last_code = df["kode_ahli"].iloc[-1]
    last_number = int(last_code[1:])
    new_number = last_number + 1
    
    return f"P{new_number}"

@app.route("/")
def index():
    df = read_kriteria()
    data = df.to_dict(orient="records")
    return render_template("index.jinja", data=data)

@app.route("/tambah", methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        kriteria = request.form["kriteria"]
        df = read_kriteria()
        df = df._append({"kriteria" : kriteria}, ignore_index=True)
        save_kriteria(df)
        return redirect(url_for("index"))
    return render_template("tambah.jinja")

@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    df = read_kriteria()
    data_to_edit = df.loc[id].to_dict() 
    
    if request.method == 'POST' :
        kriteria = request.form["kriteria"]
        df.loc[id, "kriteria"] = kriteria
        save_kriteria(df)
        return redirect(url_for("index"))
    return render_template("edit.jinja", data=data_to_edit)

@app.route("/hapus/<int:id>")
def hapus(id):
    df = read_kriteria()
    df = df.drop(id)
    save_kriteria(df)
    return redirect(url_for("index"))

@app.route("/ahli", methods=['GET', 'POST'])
def ahli():
    
    kriteria_df = read_kriteria()
    ahli_df = read_ahli()
    
    kriteria_data = kriteria_df.iloc[:, 0].tolist()
    
    ahli_columns = set(ahli_df.columns)
    kriteria_to_ahli = set(kriteria_data)
    
    new_columns = kriteria_to_ahli - ahli_columns
    for col in new_columns:
        ahli_df[col]= 0
    
    remove_columns = ahli_columns - kriteria_to_ahli
    remove_columns = remove_columns - {'kode_ahli'}
    ahli_df.drop(columns=remove_columns, inplace=True)
    
    save_ahli(ahli_df)
    
    ahli_df = read_ahli()
    data = ahli_df.to_dict(orient="records")
    headers = ahli_df.columns.tolist()
    
    return render_template("ahli/index.jinja", data=data, headers=headers)

@app.route("/ahli/tambah", methods=['GET', 'POST'])
def tambah_ahli():
    ahli_df = read_ahli()
    headers = ahli_df.columns.tolist()
    
    if request.method == "POST":
        new_row = {col : request.form.get(col) for col in headers if col != 'kode_ahli'}
        
        new_row['kode_ahli'] =generate_kode_ahli(ahli_df)
        
        ahli_df = ahli_df._append(new_row, ignore_index=True)
        
        save_ahli(ahli_df)
        
        return redirect(url_for('ahli'))
        
    return render_template("ahli/tambah.jinja", headers=headers)

@app.route("/ahli/edit/<string:kode_ahli>", methods=['GET' , 'POST'])
def edit_ahli(kode_ahli):
    ahli_df = read_ahli()
    ahli_data = ahli_df[ahli_df['kode_ahli']==kode_ahli].iloc[0]
    headers = ahli_df.columns.tolist()
    
    if request.method == "POST":
        for col in headers:
            if col != 'kode_ahli':
                ahli_df.loc[ahli_df['kode_ahli'] == kode_ahli, col] = request.form.get(col)
        save_ahli(ahli_df)
        
        return redirect(url_for('ahli'))
    
    return render_template("ahli/edit.jinja", data=ahli_data, headers=headers)

@app.route("/ahli/hapus/<string:kode_ahli>")
def hapus_ahli(kode_ahli):
    ahli_df = read_ahli()
    drop_ahli = ahli_df[ahli_df['kode_ahli'] == kode_ahli].index
    ahli_df.drop(drop_ahli, inplace=True)
    save_ahli(ahli_df)
    return redirect(url_for('ahli'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)