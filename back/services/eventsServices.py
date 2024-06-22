from schemas.eventos import Events
from models.events import Events as EventsModel

class EventService():
    def __init__(self, db) -> None:
        self.db = db

    def get_events(self):
        result = self.db.query(EventsModel).all()
        return result

    def get_event(self, id):
        result = self.db.query(EventsModel).filter(EventsModel.id == id).first()
        return result

    def get_events_by_category(self, category):
        result = self.db.query(EventsModel).filter(EventsModel.category == category).all()
        return result
    
    def create_event(self, event: Events):
        new_event = EventsModel(**event.dict())
        self.db.add(new_event)
        self.db.commit()
        return
    
    def get_event_by_name(self, name):
        result = self.db.query(EventsModel).filter(EventsModel.name == name).all()
        return result
    
    def get_event_by_description(self, description):
        result = self.db.query(EventsModel).filter(EventsModel.description == description).all()
        return result
    
    def update_event(self, id: int, data: Events):
        event = self.db.query(EventsModel).filter(EventsModel.id == id).first()
        event.name = data.name
        event.descripcion = data.descripcion
        event.fecha_inicio = data.fecha_inicio
        event.fecha_fin = data.fecha_fin
        event.cupos = data.cupos
        event.lugar = data.lugar
        event.categoria_id = data.categoria_id
        self.db.commit()
        return

    def delete_event(self, id: int):
       self.db.query(EventsModel).filter(EventsModel.id == id).delete()
       self.db.commit()
       return