import pytest
from fixture.application import Application

LOGIN = "dariatimofeevatest@gmail.com"
PASSWORD = "Bl@Sl56Er23!!7"


@pytest.fixture()
def app(request):
    fixture = Application()
    fixture.session.login(login=LOGIN, password=PASSWORD)
    request.addfinalizer(fixture.destroy)
    return fixture
