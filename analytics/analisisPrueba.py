#Analisis de datos con PANDAS
#1. Para analizar datos con PANDAS necesitamos instalar e importar la herramienta
import pandas as pd

#2. Se obtiene la fuente de Datos
#Lista de datos:
datos = [
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
    {'Nombre':'Cristopher','Ciudad':'Medellín','Edad':19},
    {'Nombre':'Camilo','Ciudad':'Bello','Edad':27},
    {'Nombre':'Juan Esteban','Ciudad':'Bello','Edad':23},
    {'Nombre':'Argemiro','Ciudad':'Bogota','Edad':48},
    {'Nombre':'Garabito','Ciudad':'Medellín','Edad':53},
]

#3. Se capturan los datos
#Datos:
#(PANDAS utiliza una tabla tabulada que se llama DataFrame)
datosOrdenados = pd.DataFrame(datos)

# print(datosOrdenados)

#Utilizando el head() (Primeros Registros)
# print(datosOrdenados.head(10))

#Utilizando el tail() (Ultimos Registros)
# print(datosOrdenados.tail())

#Utilizando en info() (Informacion de la tabla)
# print(datosOrdenados.info())

#Utilizando el describe()
# print(datosOrdenados.describe())

#Utilizando []
# print(datosOrdenados['Nombre'])
# print(datosOrdenados['Edad'] + 5)

#Eliminando Registros
# datosOrdenados.drop(0)
# print(datosOrdenados)

#Agrupar DATOS
# print(datosOrdenados.groupby('Ciudad').size())