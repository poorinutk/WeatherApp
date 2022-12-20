from weather_app.models import City


def test_city_model_repr_method():
    """
    GIVEN a City model
    WHEN a City model is created
    THEN check if string conversion of new_city
    is equal to given city name
    """
    new_city = City(name="city")
    assert str(new_city) == "city"
