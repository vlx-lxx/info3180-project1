from . import db

class Property(db.Model):
    
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    property_title = db.Column(db.String(80))
    property_description = db.Column(db.Text)
    num_rooms = db.Column(db.Integer)
    num_bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    property_type = db.Column(db.String(50))
    location = db.Column(db.String(100))
    photo = db.Column(db.String(100), nullable=True)

    def __init__(self, property_title, property_description, num_rooms, num_bathrooms, price, property_type, location, photo):
        self.property_title = property_title
        self.property_description = property_description
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
        self.photo = photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.property_title)
    

    
