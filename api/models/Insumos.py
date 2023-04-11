from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Definição da classe Insumos
class Insumos(db.Model):
    __tablename__ = 'insumos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    insumo_categoria_id = db.Column(db.Integer, db.ForeignKey('insumo_categoria.id'), nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False, default=0)
    preco = db.Column(db.Float(precision=2), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    categoria = db.relationship('InsumoCategoria', back_populates='insumos')

    def __init__(self, nome, descricao, insumo_categoria_id, quantidade_estoque, preco, status):
        self.nome = nome
        self.descricao = descricao
        self.insumo_categoria_id = insumo_categoria_id
        self.quantidade_estoque = quantidade_estoque
        self.preco = preco
        self.status = status

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'insumo_categoria_id': self.insumo_categoria_id,
            'quantidade_estoque': self.quantidade_estoque,
            'preco': self.preco,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
