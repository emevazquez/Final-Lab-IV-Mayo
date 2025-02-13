from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from backend.datos import db

class Lineaequipoplan(db.Model):
    __tablename__ = 'li_eq_pl'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    adicion_numero = Column(Integer(), ForeignKey('adiciones.numero'), nullable=False)
    producto_codigo = Column(Integer(), ForeignKey('productos.codigo'), nullable=False)
    cantidad = Column(Integer())
