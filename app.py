
from distutils.log import debug
from operator import methodcaller
import MySQLdb
from flask import Flask, jsonify, request
from config import config
from flask_mysqldb import MySQL


app=Flask(__name__)

conexion = MySQL(app)

@app.route('/cursos') #Metodo GET
def listar_cursos():

    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM curso"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos= []
        for fila in datos:
            curso ={'codigo':fila[0],'creditos':fila[1],'nombre':fila[2]}
            cursos.append(curso)
        print(datos)
        return jsonify({'cursos':cursos,'Mensaje':"Cursos listados"})

    except Exception as ex:
            return jsonify({'Mensaje':"error"})

@app.route('/cursos/<codigo>', methods = ['GET']) #MetodoGET para un solo curso
def read_curso(codigo):

    try:
    
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM curso WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:

            curso ={'codigo':datos[0],'creditos':datos[1],'nombre':datos[2]}
            return jsonify({'cursos':curso,'Mensaje':"Curso listado"})
        else:
            return jsonify({'mensaje':"Curso no encontrado"})
 
    except Exception as ex:
        
        return jsonify({'Mensaje':"error"})

@app.route('/cursos', methods=['POST'])
def registrarcurso() : 

    try:


        cursor = conexion.connection.cursor()
        sql = """INSERT INTO curso (codigo, creditos,nombre) 
        VALUES ('{0}',{1},'{2}')""".format(request.json['codigo'],request.json['creditos'],request.json['nombre'],)
        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje': "Curso registrado"})


    except Exception as ex:

        return jsonify({'Mensaje':"error"})

def pag_no_encontrada(error):
    return "<h1>LA PAGINA QUE INTENTAS BUSCAR NO EXISTE ! </h1>",404

if __name__ == '__main__':
    app.config.from_object('config.DevelopmentConfig')
    app.register_error_handler(404,pag_no_encontrada)
    app.run( )