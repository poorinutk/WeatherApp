from weather_app.models import City


def test_index_route_GET(client):
    """
    Go to the blank url,
    check the status code,
    check if text is in data
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"How\'s the weather today?" in response.data


def test_index_route_with_empty_city_POST(client):
    """
    Go to the blank url,
    send a post request with blank data,
    check the status code
    """
    city_data = {"city": ""}
    response = client.post("/", data=city_data)
    assert response.status_code == 302

    # Check if city got added to the db
    assert len(City.query.all()) == 0


def test_index_route_with_actual_city_POST(client):
    """
    Go to the blank url,
    send a post request with data,
    check the status code
    """
    city_data = {"city": "Manhattan"}
    response = client.post("/", data=city_data)
    assert response.status_code == 302

    # Check if city got added to the db
    assert len(City.query.all()) == 1

    # Check if added city is lowercase
    assert str(City.query.all()[0]) == "manhattan"


def test_index_route_with_duplicate_city_POST(client):
    """
    Go to the blank url,
    send a post request with duplicate data,
    check the status code
    """
    city_data = {"city": "Manhattan"}
    response = client.post("/", data=city_data)
    assert response.status_code == 302

    # Check if city got added to the db
    assert len(City.query.all()) == 1


def test_index_route_with_fake_city_POST(client):
    """
    Go to the blank url,
    send a post request with fake data,
    check the status code
    """
    city_data = {"city": "Imaginaryland"}
    response = client.post("/", data=city_data)
    assert response.status_code == 302

    # Check if city didn't get added
    # (Manhattan city is still in db,
    # so we check if len is 1)
    assert len(City.query.all()) == 1


def test_delete_city_route(client):
    """
    Go to delete city url,
    check status code
    """
    response = client.get("/delete/manhattan")
    assert response.status_code == 302

    # Check if Manhattan city got deleted
    assert len(City.query.all()) == 0
