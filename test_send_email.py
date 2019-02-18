# -*- coding: utf-8 -*-
import pytest
from application import Application
from message import Message


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_send_message(app):
    app.login(login="dariatimofeevatest@gmail.com", password="Bl@Sl56Er23!!7")
    app.create_message(Message(addressee="timofeyevadasha@gmail.com", theme="test", body="test"))
    app.logout()


def test_send_empty_message(app):
    app.login(login="dariatimofeevatest@gmail.com", password="Bl@Sl56Er23!!7")
    app.create_message(Message(addressee="timofeyevadasha@gmail.com", theme="test", body=""))
    app.logout()


