from sqlalchemy import Column,Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tablas
Base=declarative_base()

#Listado de modelos de la APLICACION
#USUARIO
class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))

class Gasto(Base):
    __tablename__='Gastos'
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(100))
    nombre=Column(String(50))

#INGRESO
class Ingreso(Base):
    __tablename__='Ingreso'
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(100))
    nombre=Column(String(50))

#CATEGORIA
class Categoria(Base):
    __tablename__='Categoria'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(50))
    descripcion=Column(String(100))

#MOVIMIENTO
'''class Movimiento(Base):
    id=Column(Integer, primary_key=True, autoincrement=True)
    Cantidad=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(100))'''
    
#METODO DE PAGO
class MetodoPago(Base):
    __tablename__='MetodoPago'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    descripcion=Column(String(100))

#FACTURA
class Factura(Base):
    __tablename__='Factura'
    id=Column(Integer, primary_key=True, autoincrement=True)