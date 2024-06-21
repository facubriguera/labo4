from models.users import UserModel
from schemas.users import User


#Aca creo las operaciones CRUD para nuestro objeto de usuario.
class UserService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user(self, user_id):
        result = self.db.query(UserModel).filter(UserModel.user_id == user_id).first()
        return result

    def create_user(self, user_data: dict):
        new_user = UserModel(**user_data)
        self.db.add(new_user)
        self.db.commit()
        return new_user.user_id

    def update_user(self, user_id: int, data: dict):
        user = self.db.query(UserModel).filter(UserModel.user_id == user_id).first()
        for key, value in data.items():
            setattr(user, key, value)
        self.db.commit()
        return

    def delete_user(self, user_id: int):
        self.db.query(UserModel).filter(UserModel.user_id == user_id).delete()
        self.db.commit()
        return
