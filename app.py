from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
app.secret_key = 'testing0909'
db_kriteria = "database/tb_kriteria.xlsx"
db_ahli = "database/tb_ahli.xlsx"
db_swara = "database/tb_swara.xlsx"
db_alternatif = "database/tb_alternatif.xlsx"
db_saw = "database/tb_saw.xlsx"
db_user = "database/tb_user.xlsx"

def read_kriteria():
    return pd.read_excel(db_kriteria)

def save_kriteria(df):
    df.to_excel(db_kriteria, index=False)
    
def generate_kode_kriteria(df):
    if df.empty:
        return "C1"
    
    last_code = df["kode_kriteria"].iloc[-1]
    last_number = int(last_code[1:])
    new_number = last_number + 1
    
    return f"C{new_number}"

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

def read_swara():
    return pd.read_excel(db_swara)

def save_swara(df):
    df.to_excel(db_swara, index=False)
    
def read_alternatif():
    return pd.read_excel(db_alternatif)

def save_alternatif(df):
    df.to_excel(db_alternatif, index=False)
    
def generate_kode_alternatif(df):
    if df.empty:
        return "A1"
    
    last_code = df["kode_alternatif"].iloc[-1]
    last_number = int(last_code[1:])
    new_number = last_number + 1
    
    return f"A{new_number}"

def read_saw():
    return pd.read_excel(db_saw)

def save_saw(df):
    df.to_excel(db_saw, index=False)
    
def read_user():
    return pd.read_excel(db_user)

def save_user(df):
    df.to_excel(db_user, index=False)

@app.route("/kriteria")
def index():
    username = session.get('username')
    df = read_kriteria()
    data = df.to_dict(orient="records")
    return render_template("kriteria/index.jinja", username=username, data=data)

@app.route("/tambah", methods=['POST'])
def tambah():
    kriteria = request.form["kriteria"]
    jenis_kriteria = request.form["jenis_kriteria"]
    df = read_kriteria()
    kode_kriteria = generate_kode_kriteria(df)
    df = df._append({"kode_kriteria":kode_kriteria, "kriteria" : kriteria, "jenis_kriteria":jenis_kriteria}, ignore_index=True)
    save_kriteria(df)
    return jsonify(success=True, message="Berhasil Menambahkan Kriteria Baru")

@app.route("/edit/<string:kode_kriteria>", methods=['POST'])
def edit(kode_kriteria):
    df = read_kriteria()
    kriteria = request.form["kriteria"]
    jenis_kriteria = request.form["jenis_kriteria"]
    df.loc[df["kode_kriteria"] == kode_kriteria, "kriteria"] = kriteria
    df.loc[df["kode_kriteria"] == kode_kriteria, "jenis_kriteria"] = jenis_kriteria
    save_kriteria(df)
    return jsonify(success=True, message="Berhasil Mengubah Kriteria")

@app.route("/hapus/<string:kode_kriteria>", methods=['POST'])
def hapus(kode_kriteria):
    df = read_kriteria()
    drop_kriteria = df[df['kode_kriteria'] == kode_kriteria].index
    df.drop(drop_kriteria, inplace=True)
    save_kriteria(df)
    return jsonify(success=True, message="Data berhasil dihapus")

@app.route("/ahli", methods=['GET', 'POST'])
def ahli():
    username = session.get('username')
    kriteria_df = read_kriteria()
    ahli_df = read_ahli()
    
    kriteria_data = kriteria_df.iloc[:, 1].tolist()
    
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
    
    return render_template("ahli/index.jinja", username=username, data=data, headers=headers)

@app.route("/ahli/tambah", methods=['POST'])
def tambah_ahli():
    ahli_df = read_ahli()
    headers = ahli_df.columns.tolist()
    new_row = {col : request.form.get(col) for col in headers if col != 'kode_ahli'}
        
    new_row['kode_ahli'] =generate_kode_ahli(ahli_df)
        
    ahli_df = ahli_df._append(new_row, ignore_index=True)
        
    save_ahli(ahli_df)
        
    return jsonify(success=True, message="Berhasil Menambahkan Pendapat Ahli Baru")
        
@app.route("/ahli/edit/<string:kode_ahli>", methods=['POST'])
def edit_ahli(kode_ahli):
    ahli_df = read_ahli()
    headers = ahli_df.columns.tolist()
    
    for col in headers:
        if col != 'kode_ahli':
            ahli_df.loc[ahli_df['kode_ahli'] == kode_ahli, col] = request.form.get(col)
    save_ahli(ahli_df)
        
    return jsonify(success=True, message="Berhasil Mengubah Data Pendapat Ahli")

@app.route("/ahli/hapus/<string:kode_ahli>", methods=['POST'])
def hapus_ahli(kode_ahli):
    ahli_df = read_ahli()
    drop_ahli = ahli_df[ahli_df['kode_ahli'] == kode_ahli].index
    ahli_df.drop(drop_ahli, inplace=True)
    save_ahli(ahli_df)
    return jsonify(success=True, message="Data berhasil dihapus")

@app.route("/swara")
def swara():
    username = session.get('username')
    kriteria_df = read_kriteria()
    swara_df = read_swara()
    ahli_df = read_ahli()
    
    kriteria_data = kriteria_df.iloc[:, 1].tolist()
    swara_data = swara_df.iloc[:, 0].tolist()
    
    data_kriteria = set(kriteria_data)
    data_swara = set(swara_data)
    
    tambah_data = data_kriteria - data_swara
    for row in tambah_data:
       swara_df = swara_df._append({'kriteria': row}, ignore_index=True)
        
    hapus_data = data_swara - data_kriteria
    swara_df = swara_df[~swara_df['kriteria'].isin(hapus_data)]
    
    for idx, row in swara_df.iterrows():
        kriteria_name = row['kriteria']
        if kriteria_name in ahli_df.columns:
            rata_rata = ahli_df[kriteria_name].mean()
            swara_df.at[idx, 'tj'] = rata_rata
            
    swara_df['j'] = swara_df['tj'].rank(ascending=False, method='dense').astype(int)
    
    swara_df = swara_df.sort_values(by='j').reset_index(drop=True)
    
    average_j = swara_df['j'].mean()
    
    for i in range(len(swara_df)):
        if i == 0:
            swara_df.at[i, 'Sj'] = 0
            swara_df.at[i, 'Kj'] = 1
            swara_df.at[i, 'Qj'] = 1
        else:
            swara_df.at[i, 'Sj'] = (swara_df.at[i, 'j'] - 1) / average_j
            swara_df.at[i, 'Kj'] = swara_df.at[i, 'Sj'] + 1
            swara_df.at[i, 'Qj'] = swara_df.at[i - 1, 'Qj'] / swara_df.at[i, 'Kj']
            
    total_qj = swara_df['Qj'].sum()
    
    swara_df['Wj'] = swara_df['Qj'] / total_qj
    
    save_swara(swara_df)
    
    swara_df = read_swara()
    
    data = swara_df.to_dict(orient="records")
    
    return render_template("swara/index.jinja",username=username, data=data)

@app.route("/swara/perhitungan")
def swara_perhitungan():
    username = session.get('username')
    ahli_df = read_ahli()
    data_ahli = ahli_df.to_dict(orient="records")
    headers_ahli = ahli_df.columns.tolist()
    
    swara_df = read_swara()
    data_swara = swara_df.to_dict(orient="records")
    
    return render_template("swara/perhitungan.jinja", username=username, data_ahli=data_ahli, headers_ahli=headers_ahli, data_swara=data_swara)

@app.route('/bobot')
def bobot():
    username = session.get('username')
    swara_df = read_swara()
    data_swara = swara_df.to_dict(orient="records")
    return render_template("/bobot/index.jinja", data=data_swara, username=username)

@app.route('/alternatif')
def alternatif():
    username = session.get('username')
    kriteria_df = read_kriteria()
    alternatif_df = read_alternatif()
    
    kriteria_data = kriteria_df.iloc[:, 1].tolist()
    
    alternatif_columns = set(alternatif_df.columns)
    kriteria_to_alternatif = set(kriteria_data)
    
    new_columns = kriteria_to_alternatif - alternatif_columns
    for col in new_columns:
        alternatif_df[col]= 0
    
    remove_columns = alternatif_columns - kriteria_to_alternatif
    remove_columns = remove_columns - {'kode_alternatif'} - {'alternatif'}
    alternatif_df.drop(columns=remove_columns, inplace=True)
    
    save_alternatif(alternatif_df)
    
    alternatif_df = read_alternatif()
    data = alternatif_df.to_dict(orient="records")
    headers = alternatif_df.columns.tolist()
    
    return render_template("alternatif/index.jinja", username=username, data=data, headers=headers)

@app.route("/alternatif/tambah", methods=['POST'])
def tambah_alternatif():
    alternatif_df = read_alternatif()
    headers = alternatif_df.columns.tolist()
    
    new_row = {col : request.form.get(col) for col in headers if col != 'kode_alternatif'}
        
    new_row['kode_alternatif'] =generate_kode_alternatif(alternatif_df)
        
    alternatif_df = alternatif_df._append(new_row, ignore_index=True)
        
    save_alternatif(alternatif_df)
        
    return jsonify(success=True, message="Berhasil Menambahkan Alternatif Baru")
        
@app.route("/alternatif/edit/<string:kode_alternatif>", methods=['POST'])
def edit_alternatif(kode_alternatif):
    alternatif_df = read_alternatif()
    headers = alternatif_df.columns.tolist()
    
    for col in headers:
        if col != 'kode_alternatif':
            alternatif_df.loc[alternatif_df['kode_alternatif'] == kode_alternatif, col] = request.form.get(col)
    save_alternatif(alternatif_df)
        
    return jsonify(success=True, message="Berhasil Mengubah Data Alternatif")

@app.route("/alternatif/hapus/<string:kode_alternatif>", methods=['POST'])
def hapus_alternatif(kode_alternatif):
    alternatif_df = read_alternatif()
    drop_alternatif = alternatif_df[alternatif_df['kode_alternatif'] == kode_alternatif].index
    alternatif_df.drop(drop_alternatif, inplace=True)
    save_alternatif(alternatif_df)
    return jsonify(success=True, message="Data berhasil dihapus")

@app.route("/saw")
def saw():
    username = session.get('username')
    kriteria_df = read_kriteria()
    swara_df = read_swara()
    alternatif_df = read_alternatif()
    saw_df = read_saw()
    
    saw_df = alternatif_df.drop(columns=["alternatif"]).copy()
    saw_df = saw_df.rename(columns={col: col + "(R)" for col in saw_df.columns if col != "kode_alternatif"})
    
    for kriteria in kriteria_df["kriteria"]:
        col_name = kriteria + "(R)"
        if kriteria_df[kriteria_df["kriteria"] == kriteria]["jenis_kriteria"].values[0] == "benefit":
            saw_df[col_name] = saw_df[col_name] / saw_df[col_name].max()
        else:
            saw_df[col_name] = saw_df[col_name].min() / saw_df[col_name]
            
    for kriteria in kriteria_df["kriteria"]:
        col_name_r = kriteria + "(R)"
        col_name_v = kriteria + "(V)"
        bobot = swara_df[swara_df["kriteria"] == kriteria]["Wj"].values[0]
        saw_df[col_name_v] = saw_df[col_name_r] * bobot
    
    saw_df["Skor_SAW"] = saw_df[[col + "(V)" for col in kriteria_df["kriteria"]]].sum(axis=1)
    saw_df['Rank_SAW'] = saw_df['Skor_SAW'].rank(ascending=False, method='dense').astype(int)
    
    headers_r = [col for col in saw_df.columns if "(R)" in col]
    headers_v = [col for col in saw_df.columns if "(V)" in col]
        
    save_saw(saw_df)
    read_saw()
    selected_columns = ["kode_alternatif", "Skor_SAW", "Rank_SAW"]  
    saw_df = saw_df[selected_columns]
    data = saw_df.to_dict(orient="records")
    
    headers = saw_df.columns.tolist()
    
    return render_template("saw/index.jinja", username=username, data=data, headers_r=headers_r, headers_v=headers_v, headers=headers)

@app.route("/saw/perhitungan")
def saw_perhitungan():
    username = session.get('username')
    kriteria_df = read_kriteria()
    swara_df = read_swara()
    alternatif_df = read_alternatif()
    saw_df = read_saw()
    
    saw_df = alternatif_df.drop(columns=["alternatif"]).copy()
    saw_df = saw_df.rename(columns={col: col + "(R)" for col in saw_df.columns if col != "kode_alternatif"})
    
    for kriteria in kriteria_df["kriteria"]:
        col_name = kriteria + "(R)"
        if kriteria_df[kriteria_df["kriteria"] == kriteria]["jenis_kriteria"].values[0] == "benefit":
            saw_df[col_name] = saw_df[col_name] / saw_df[col_name].max()
        else:
            saw_df[col_name] = saw_df[col_name].min() / saw_df[col_name]
            
    for kriteria in kriteria_df["kriteria"]:
        col_name_r = kriteria + "(R)"
        col_name_v = kriteria + "(V)"
        bobot = swara_df[swara_df["kriteria"] == kriteria]["Wj"].values[0]
        saw_df[col_name_v] = saw_df[col_name_r] * bobot
    
    saw_df["Skor_SAW"] = saw_df[[col + "(V)" for col in kriteria_df["kriteria"]]].sum(axis=1)
    saw_df['Rank_SAW'] = saw_df['Skor_SAW'].rank(ascending=False, method='dense').astype(int)
    
    headers_r = [col for col in saw_df.columns if "(R)" in col]
    headers_v = [col for col in saw_df.columns if "(V)" in col]
    saw_df = read_saw()
    
    data_alternatif = alternatif_df.to_dict(orient="records")
    headers_alternatif = alternatif_df.columns.tolist()
    data = saw_df.to_dict(orient="records")
    
    saw_df = saw_df.sort_values(by='Skor_SAW', ascending=False).reset_index(drop=True)
    selected_columns = ["kode_alternatif", "Skor_SAW", "Rank_SAW"]  
    saw_df = saw_df[selected_columns]
    data_rank = saw_df.to_dict(orient="records")
    headers_rank = saw_df.columns.tolist()
    
    join_df = saw_df.merge(alternatif_df[['kode_alternatif', 'alternatif']], on='kode_alternatif', how='left')
    top_alternatif = join_df.nlargest(1, 'Skor_SAW').to_dict(orient="records")[0]
    
    return render_template("saw/perhitungan.jinja", username=username, data_rank=data_rank, headers_rank=headers_rank, data=data, headers_r=headers_r, headers_v=headers_v, data_alternatif=data_alternatif, headers_alternatif=headers_alternatif, top_alternatif=top_alternatif)

@app.route("/user")
def user():
    username = session.get('username')
    df = read_user()
    data = df.to_dict(orient="records")
    return render_template("user/index.jinja", username=username, data=data)

@app.route("/user/tambah", methods=['POST'])
def tambah_user():
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    df = read_user()
    df = df._append({"email":email, "username" : username, "password":password}, ignore_index=True)
    save_user(df)
    return jsonify(success=True, message="Berhasil Menambahkan User Baru")

@app.route("/user/edit/<int:id>", methods=['POST'])
def edit_user(id):
    df = read_user()
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    
    df.loc[id, "email"] = email
    df.loc[id, "username"] = username
    df.loc[id, "password"] = password
   
    save_user(df)
    return jsonify(success=True, message="Berhasil Mengubah Data User")

@app.route("/user/hapus/<int:id>", methods=['POST'])
def hapus_user(id):
    user_df = read_user()
    df = user_df.drop(id)
    save_user(df)
    return jsonify(success=True, message="Data berhasil dihapus")

@app.route("/dashboard")
def dashboard():
    username = session.get('username')
    user_df = read_user()
    kriteria_df = read_kriteria()
    ahli_df = read_ahli()
    alternatif_df = read_alternatif()
    saw_df = read_saw()
    
    user_count = user_df.shape[0]
    kriteria_count = kriteria_df.shape[0]
    ahli_count = ahli_df.shape[0]
    alternatif_count = alternatif_df.shape[0]
    
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#DEAF4B')
    ax.set_facecolor('#DEAF4B')
    ax.bar(saw_df['kode_alternatif'], saw_df['Skor_SAW'], color='#585D61')
    ax.set_xlabel('Kode Alternatif')
    ax.set_ylabel('Skor SAW')
    ax.set_title('Grafik SAW Alternatif')

    chart_path = os.path.join('static', 'img', 'saw_chart.png')
    plt.savefig(chart_path)
    plt.close(fig)
    return render_template("dashboard/index.jinja", username=username,  user_count=user_count, kriteria_count=kriteria_count, ahli_count=ahli_count,alternatif_count=alternatif_count, chart_path=chart_path)

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form["username"].strip()
        password = request.form['password'].strip()
        
        print("Username Input:", username)
        print("Password Input:", password)
        
        df = read_user()
        df['username'] = df['username'].astype(str).str.strip()
        df['password'] = df['password'].astype(str).str.strip()
        print("DataFrame:\n", df)
        
        validasi = ((df['username'] == username) & (df['password'] == password)).any()
        print("Filtered User Data:\n", validasi)
        
        if validasi:
            session['username'] = username
            return jsonify(success=True)
        else:
            return jsonify(success=False, message="Username atau Password Salah")
        
    return render_template("login/login.jinja")

@app.route("/register", methods=['POST'])
def register():
    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    df = read_user()
    df = df._append({"email" : email, "username":username, "password":password}, ignore_index=True)
    save_user(df)
    return jsonify(success=True)

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)