from config.database import Session
from models.category import Category as CategoryModel
from schemas.categorias import Category as CategorySchema
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

class CategoryService():
    def __init__(self, db) -> None:
        self.db = db

    def get_categories(self):
        categories = self.db.query(CategoryModel).all()
        return categories

    def get_category(self, cat_id):
        category = self.db.query(CategoryModel).filter(CategoryModel.cat_id == cat_id).first()
        return category

    def create_category(self, nombre: str, descripcion: str):
        new_category = CategoryModel(nombre=nombre, descripcion=descripcion)
        self.db.add(new_category)
        self.db.commit()
        return new_category

    def update_category(self, cat_id: int, category: CategorySchema):
        category_db = self.db.query(CategoryModel).filter(CategoryModel.cat_id == cat_id).first()
        if category_db:
            category_db.nombre = category.nombre
            category_db.descripcion = category.descripcion
            self.db.commit()
        return category_db

    def delete_category(self, cat_id: int):
        category = self.db.query(CategoryModel).filter(CategoryModel.cat_id == cat_id).first()
        if category:
            self.db.delete(category)
            self.db.commit()
        return category
