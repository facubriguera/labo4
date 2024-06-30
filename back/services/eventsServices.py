from schemas.eventos import Events as EventsSchema
from models.events import Events as EventsModel

class EventService:
    def __init__(self, db):
        self.db = db

    def get_events(self):
        return self.db.query(EventsModel).all()

    def get_event(self, id):
        return self.db.query(EventsModel).filter(EventsModel.event_id == id).first()

    def get_events_by_category(self, category):
        return self.db.query(EventsModel).filter(EventsModel.cat_id == category).all()

    def create_event(self, event: EventsSchema) -> EventsModel:
        new_event = EventsModel(**event.dict())
        self.db.add(new_event)
        self.db.commit()
        self.db.refresh(new_event)  # Refresca el objeto para obtener el event_id generado
        return new_event

    def get_event_by_name(self, name):
        return self.db.query(EventsModel).filter(EventsModel.name == name).first()

    def get_event_by_description(self, description):
        return self.db.query(EventsModel).filter(EventsModel.description == description).first()

    def update_event(self, id: int, data: EventsSchema) -> EventsModel:
        event = self.db.query(EventsModel).filter(EventsModel.event_id == id).first()
        if event:
            event.name = data.name
            event.description = data.description
            event.fecha_inicio = data.fecha_inicio
            event.fecha_fin = data.fecha_fin
            event.cupos = data.cupos
            event.lugar = data.lugar
            event.cat_id = data.cat_id
            self.db.commit()
            return event
        return None  # Manejar el caso donde no se encontró el evento

    def delete_event(self, id: int) -> EventsModel:
        event = self.db.query(EventsModel).filter(EventsModel.event_id == id).first()
        if event:
            self.db.delete(event)
            self.db.commit()
            return event
        return None  # Manejar el caso donde no se encontró el evento
