from weather_app.utils import get_weather_data


def test_get_weather_data():
    """
    GIVEN a chosen city name
    WHEN a data is gathered
    THEN check status code
    """
    assert get_weather_data("Manhattan")["cod"] == 200
    # OpenWeatherAPI gives the 404 error as a string,
    # so we check if the code is a "404"
    assert get_weather_data("Imaginaryland")["cod"] == "404"
