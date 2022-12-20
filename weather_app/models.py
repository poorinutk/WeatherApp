from weather_app import db


class City(db.Model):
    city_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return str(self.name)
