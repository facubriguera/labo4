from fastapi import APIRouter, Path, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from services.categoriesServices import CategoryService
from schemas.categorias import Category as CategorySchema
from models.category import Category as CategoryModel

category_router = APIRouter()

@category_router.get('/categories', tags=['categorias'], response_model=list)
def get_categories() -> list:
    db = Session()
    result = CategoryService(db).get_categories()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@category_router.get('/categories/{cat_id}', tags=['categorias'], response_model=CategorySchema)
def get_category(cat_id: int = Path(..., ge=1)) -> CategorySchema:
    db = Session()
    result = CategoryService(db).get_category(cat_id)
    if not result:
        raise HTTPException(status_code=404, detail='Categoría no encontrada')
    return result

@category_router.post('/categories', tags=['categorias'], response_model=dict, status_code=201)
def create_category(nombre: str, descripcion: str) -> dict:
    db = Session()
    new_category = CategoryService(db).create_category(nombre, descripcion)
    return JSONResponse(status_code=201, content={"message": "Categoría creada con éxito", "category": jsonable_encoder(new_category)})

@category_router.put('/categories/{cat_id}', tags=['categorias'], response_model=dict, status_code=200)
def update_category(cat_id: int, category: CategorySchema) -> dict:
    db = Session()
    result = CategoryService(db).get_category(cat_id)
    if not result:
        raise HTTPException(status_code=404, detail='Categoría no encontrada')
    
    updated_category = CategoryService(db).update_category(cat_id, category)
    return JSONResponse(status_code=200, content={"message": "Categoría actualizada correctamente", "category": jsonable_encoder(updated_category)})

@category_router.delete('/categories/{cat_id}', tags=['categorias'], response_model=dict, status_code=200)
def delete_category(cat_id: int) -> dict:
    db = Session()
    result = CategoryService(db).delete_category(cat_id)
    if not result:
        raise HTTPException(status_code=404, detail='Categoría no encontrada')
    return JSONResponse(status_code=200, content={"message": "Categoría eliminada correctamente"})
