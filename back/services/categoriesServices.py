from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.category import Category as CategoryModel
from schemas.categorias import Category as CategorySchema

class CategoryService:
    def __init__(self, db: Session):
        self.db = db

    def get_categories(self):
        return self.db.query(CategoryModel).all()

    def get_category(self, cat_id: int):
        return self.db.query(CategoryModel).filter(CategoryModel.cat_id == cat_id).first()

    def create_category(self, nombre: str, descripcion: str) -> CategoryModel:
        new_category = CategoryModel(nombre=nombre, descripcion=descripcion)
        try:
            self.db.add(new_category)
            self.db.commit()
            self.db.refresh(new_category)
            return new_category
        except IntegrityError as e:
            self.db.rollback()
            # Aquí podrías manejar la excepción, por ejemplo, registrar el error o lanzar una excepción personalizada
            raise e

    def update_category(self, cat_id: int, category: CategorySchema) -> CategoryModel:
        category_db = self.get_category(cat_id)
        if category_db:
            category_db.nombre = category.nombre
            category_db.descripcion = category.descripcion
            category_db.cat_id = category.cat_id
            try:
                self.db.commit()
                self.db.refresh(category_db)
                return category_db
            except IntegrityError as e:
                self.db.rollback()
                # Manejar la excepción según sea necesario
                raise e
        return None  # Manejar el caso donde no se encontró la categoría

    def delete_category(self, cat_id: int) -> CategoryModel:
        category_db = self.get_category(cat_id)
        if category_db:
            try:
                self.db.delete(category_db)
                self.db.commit()
                return category_db
            except IntegrityError as e:
                self.db.rollback()
                # Manejar la excepción según sea necesario
                raise e
        return None  # Manejar el caso donde no se encontró la categoría
