import pytest
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    fixture.session.login(login="dariatimofeevatest@gmail.com", password="Bl@Sl56Er23!!7")
    request.addfinalizer(fixture.destroy)
    return fixture
