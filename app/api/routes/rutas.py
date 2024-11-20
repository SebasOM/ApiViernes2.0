from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta 
from app.api.schemas.DTO import GastoDTOPeticion, GastoDTORespuesta
from app.api.schemas.DTO import CategoriaDTOPeticion, CategoriaDTORespuesta
from app.api.schemas.DTO import MetodoPagoDTOPeticion, MetodoPagoDTORespuesta
from app.api.schemas.DTO import IngresoDTOPeticion, IngresoDTORespuesta

from app.api.models.modelosApp import Usuario, Gasto, Categoria, MetodoPago, Ingreso
from app.database.configuration import sessionLocal, engine

#Para que un api funcione debe tener un archivo enrutador
rutas=APIRouter() #ENDPOINTS

#Crear una funcion para establecer cuando yo quiera y necesite
#conexion hacia la base de datos
def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

#PROGRAMACION DE CADA UNO DE LOS SERVICIOS
#QUE OFRECERA NUESTRA API

#SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN BD
@rutas.post("/usuarios", response_model=UsuarioDTORespuesta)
def guardarUsuario(datosPeticion:UsuarioDTOPeticion, db:Session=Depends(getDataBase)):
    try:
        usuario=Usuario(
            nombres=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            contraseña=datosPeticion.contraseña,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return UsuarioDTORespuesta(
            id=usuario.id,
            nombre=usuario.nombres,
            telefono=usuario.telefono,
            ciudad=usuario.ciudad
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    

@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Usuario).all()
        return [
            UsuarioDTORespuesta(
                id=usuario.id,
                nombre=usuario.nombres,
                telefono=usuario.telefono,
                ciudad=usuario.ciudad
            ) for usuario in listadoDeUsuarios
        ]

    except Exception as error:
        db.rollback()
        raise HTTPException()
    
    ####

@rutas.post("/Gastos", response_model=GastoDTORespuesta)
def guardarGasto(datosPeticion:GastoDTOPeticion, db:Session=Depends(getDataBase)):
    try:
        gasto=Gasto(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            nombre=datosPeticion.nombre
        )
        db.add(gasto)
        db.commit()
        db.refresh(gasto)
        return GastoDTORespuesta(
            id=gasto.id,
            monto=gasto.monto,
            fecha=gasto.fecha,
            descripcion=gasto.descripcion,
            nombre=gasto.nombre
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    
@rutas.get("/Gastos", response_model=List[GastoDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Gasto).all()
        return [
            GastoDTORespuesta(
                id=gasto.id,
                monto=gasto.monto,
                fecha=gasto.fecha,
                descripcion=gasto.descripcion,
                nombre=gasto.nombre
            ) for gasto in listadoDeUsuarios
        ]

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    
    ####

@rutas.post("/Ingreso")
def guardarUsuario(datosPeticion:IngresoDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        ingreso=Ingreso(
            monto=datosPeticion.monto,
            fecha=datosPeticion.fecha,
            descripcion=datosPeticion.descripcion,
            nombre=datosPeticion.nombre
        )
        db.add(ingreso)
        db.commit()
        db.refresh(ingreso)
        return ingreso
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    
@rutas.get("/Ingreso", response_model=List[IngresoDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Ingreso).all()
        return listadoDeUsuarios

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    
    ####

@rutas.post("/Categoria", response_model=CategoriaDTORespuesta)
def guardarUsuario(datosPeticion:CategoriaDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        categoria=Categoria(
            nombreCategoria=datosPeticion.nombreCategoria,
            descripcion=datosPeticion.descripcion
        )
        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return CategoriaDTORespuesta(
            id=categoria.id,
            nombreCategoria=categoria.nombreCategoria,
            descripcion=categoria.descripcion
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")

@rutas.get("/Categoria", response_model=List[CategoriaDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(Categoria).all()
        return [
            CategoriaDTORespuesta(
                id=categoria.id,
                nombreCategoria=categoria.nombreCategoria,
                descripcion=categoria.descripcion
            ) for categoria in listadoDeUsuarios
        ]

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")

    ####

@rutas.post("/MetodoPago", response_model=MetodoPagoDTORespuesta)
def guardarUsuario(datosPeticion:MetodoPagoDTOPeticion, db:Session=Depends(getDataBase) ):
    try:
        metodoPago=MetodoPago(
            nombreMetodo=datosPeticion.nombreMetodo,
            descripcion=datosPeticion.descripcion
        )
        db.add(metodoPago)
        db.commit()
        db.refresh(metodoPago)
        return MetodoPagoDTORespuesta(
            id=metodoPago.id,
            nombreMetodo=metodoPago.nombreMetodo,
            descripcion=metodoPago.descripcion
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")
    
@rutas.get("/MetodoPago", response_model=List[MetodoPagoDTORespuesta])
def buscarUsuarios(db:Session=Depends(getDataBase)):
    try:
        listadoDeUsuarios=db.query(MetodoPago).all()
        return [
            MetodoPagoDTORespuesta(
                id=metodoPago.id,
                nombreMetodo=metodoPago.nombreMetodo,
                descripcion=metodoPago.descripcion
            ) for metodoPago in listadoDeUsuarios
        ]

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario XOXO{error}")