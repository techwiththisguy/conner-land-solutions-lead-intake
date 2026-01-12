from app import create_app
from app.models import Lead

app = create_app()

with app.app_context():
    count = Lead.query.count()
    print("DB lead count:", count)
    
    latest = Lead.query.order_by(Lead.id.desc()).first()
    print("Latest lead:", latest)