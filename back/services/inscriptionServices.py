from schemas.eventos import Events
from models.events import Events as EventsModel

class inscriptionServices():
    def __init__(self, db) -> None:
        self.db = db

    def get_user_inscriptions(self):
        return 
    
    def get_user_incription_history(self):
        return