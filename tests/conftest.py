import pytest

from weather_app import app, db


@pytest.fixture(scope="module")
def application():
    """
    Setup the Flask's app for testing
    """

    # Setup
    app.config.update({
        "TESTING": True,
    })
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db',
    })

    db.create_all()

    # The testing itself
    yield app

    # Teardown
    db.drop_all()


@pytest.fixture()
def client(application):
    """
    Returns Flask's test client to send requests with
    """
    return application.test_client()
