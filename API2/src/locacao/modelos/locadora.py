import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm
from locacao.modelos.modelo_base import ModeloBase

class Locadora(ModeloBase):
    __tablename__ = "locadora"

    uuid: orm.Mapped[str] = orm.mapped_column(sa.String(36), primary_key=True)
    nome: orm.Mapped[str] = orm.mapped_column(sa.String(100))
    horario_abertura: orm.Mapped[datetime.time] = orm.mapped_column(sa.Time)
    horario_fechamento: orm.Mapped[datetime.time] = orm.mapped_column(sa.Time)
    endereco: orm.Mapped[str] = orm.mapped_column(sa.String(255))

    def __repr__(self) -> str:
        return (f"Locadora(uuid={self.uuid}, nome={self.nome}, " + 
                f"horario_abertura={self.horario_abertura}, " + 
                f"horario_fechamento={self.horario_fechamento}, " + 
                f"endereco={self.endereco})")