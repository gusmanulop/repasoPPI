from flask import Flask, render_template, request, redirect, url_for, session
from db_connection import get_db_connection
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = 'mi_secreto' 

@app.route('/')
def home():
     return render_template('dashboard.html')

# Ruta para el dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
# Ruta para SmartPhones
@app.route('/smart')
def smart():
    return render_template('smart.html')

# Ruta para suscripcion

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO personas (nombre, apellido, correo_electronico) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query, (nombre, apellido, email))
            conn.commit()
            cursor.close()
            conn.close()
            return "Registro guardado exitosamente ✅"
        except mysql.connector.Error as err:
            conn.rollback()
            cursor.close()
            conn.close()
            return f"Error al guardar los datos: {err}"

    return render_template('register.html')


# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
