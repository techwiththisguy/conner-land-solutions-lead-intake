from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lead(db.Model):
    __tablename__ = "leads"
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=True) 
    
    service_type = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    
    timeline = db.Column(db.String(80), nullable=True) 
    notes = db.Column(db.Text, nullable=False)
    
    status = db.Column(db.String(30), nullable=False, default="NEW")