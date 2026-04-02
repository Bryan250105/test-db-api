from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class PortCodeList(db.Model):
    __tablename__ = "port_code_list"

    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    
    change: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    country: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    location: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    name: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    namewodiacritics: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    subdivision: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    status: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    function: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    date: so.Mapped[int] = so.mapped_column(sa.BigInteger, nullable=True)
    iata: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    coordinates: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    remarks: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class AirportCodeList(db.Model):
    __tablename__ = "airport_code_list"

    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    
    ident: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    type: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    name: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    elevation_ft: so.Mapped[int] = so.mapped_column(sa.BigInteger, nullable=True)
    continent: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    iso_country: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    iso_region: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    municipality: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    icao_code: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    iata_code: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    gps_code: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    local_code: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)
    coordinates: so.Mapped[str] = so.mapped_column(sa.Text, nullable=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Log(db.Model):
    __tablename__ = "logs"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(255), nullable=False)
    timestamp: so.Mapped[datetime] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc), nullable=False
    )

    def __repr__(self):
        return f"<Log {self.timestamp}: {self.description}>"
