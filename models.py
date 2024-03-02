from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE_URL = "https://cdn-icons-png.freepik.com/512/8211/8211733.png"

db = SQLAlchemy()

class Pet(db.Model):
    """Pet for adoption"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def get_image(self):
        """Get/Return image for pet, otherwise return default"""
        return self.photo_url or DEFAULT_IMAGE_URL

def connect_db(app):
    """Connect db to app"""
    db.app = app
    db.init_app(app)