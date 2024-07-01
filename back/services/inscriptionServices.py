from models.inscriptions import InscripcionModel
from schemas.inscripciones import InscripcionSchema
from utils.validators import idDuplicados
from datetime import date
from models.events import Events
class InscripcionService():
    def __init__(self, db) -> None:
        self.db = db

    def get_inscripciones(self):
        result = self.db.query(InscripcionModel).all()
        return result
    
    def get_inscripcion(self, inscrip_id):
        result = self.db.query(InscripcionModel).filter(InscripcionModel.inscrip_id == inscrip_id).first()
        return result
    
    def create_inscripcion(self, inscripcion: InscripcionSchema):
        lista = self.get_inscripciones()
        idDuplicados(inscripcion, lista)
        new_inscripcion = InscripcionModel(**inscripcion.model_dump())
        self.db.add(new_inscripcion)
        self.db.commit()
        return new_inscripcion
    
    def update_inscripcion(self, inscrip_id: int, inscripcion: InscripcionSchema):
        result = self.db.query(InscripcionModel).filter(InscripcionModel.inscrip_id == inscrip_id).first()
        result.evento_id = inscripcion.event_id
        result.usuario_id = inscripcion.usuario_id
        result.fecha_inscripcion = inscripcion.fecha_inscripcion
        self.db.commit()
        return result
    
    def delete_inscripcion(self, inscrip_id:int):
        self.db.query(InscripcionModel).filter(InscripcionModel.inscrip_id == inscrip_id).delete()
        self.db.commit()
        return True
    
    def get_inscripcion_usuario(self, user_id: int):
        result = self.db.query(InscripcionModel).filter(InscripcionModel.user_id == user_id).all()
        return result
    
    def get_inscripcion_usuario_activa(self, user_id: int):
        today = date.today()
        result = self.db.query(InscripcionModel).join(Events, InscripcionModel.event_id == Events.event_id).filter(
            InscripcionModel.user_id == user_id,
            Events.fecha_inicio >= today
        ).all()
        return result