from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Definição da classe InsumoCategorias
class InsumoCategorias(db.Model):
    __tablename__ = 'insumo_categoria'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    insumos = db.relationship('Insumos', backref='insumo_categoria', lazy=True)

    def __repr__(self):
        return f'<InsumoCategorias {self.id}>'
