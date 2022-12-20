from weather_app import app, db


if __name__ == '__main__':
    # Create database if one doesn't exist yet
    db.create_all()
    app.run(debug=True)
