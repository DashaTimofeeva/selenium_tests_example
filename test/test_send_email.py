# -*- coding: utf-8 -*-
from model.message import Message


def test_send_message(app):
    app.session.login(login="dariatimofeevatest@gmail.com", password="Bl@Sl56Er23!!7")
    app.message.create(Message(addressee="timofeyevadasha@gmail.com", theme="test", body="test"))
    app.session.logout()


def test_send_empty_message(app):
    app.session.login(login="dariatimofeevatest@gmail.com", password="Bl@Sl56Er23!!7")
    app.message.create(Message(addressee="timofeyevadasha@gmail.com", theme="test", body=""))
    app.session.logout()

