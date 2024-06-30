from models.users import UserModel
from schemas.users import User

class UserService:
    
    def __init__(self, db):
        self.db = db

    def get_users(self):
        return self.db.query(UserModel).all()

    def get_user(self, user_id: int):
        return self.db.query(UserModel).filter(UserModel.user_id == user_id).first()

    def create_user(self, user_data: User):
        new_user = UserModel(**user_data.dict())
        self.db.add(new_user)
        self.db.commit()
        return new_user.user_id

    def update_user(self, user_id: int, user_data: User):
        user = self.db.query(UserModel).filter(UserModel.user_id == user_id).first()
        if user:
            for key, value in user_data.dict().items():
                setattr(user, key, value)
            self.db.commit()
        return user

    def delete_user(self, user_id: int):
        self.db.query(UserModel).filter(UserModel.user_id == user_id).delete()
        self.db.commit()
