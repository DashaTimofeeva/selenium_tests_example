# -*- coding: utf-8 -*-
import pytest
from test.model.message import Message
from faker import Faker

fake = Faker()

parameters = [
    ("timofeyevadasha@gmail.com", fake.text(max_nb_chars=10), fake.text(max_nb_chars=50)),
    (fake.email(), "", fake.text(max_nb_chars=50)),
    (fake.email(), fake.text(max_nb_chars=10), "")
]


@pytest.mark.parametrize('addressee, theme, body', parameters)
def test_send_message(app, addressee, theme, body):
    app.message.create(Message(addressee, theme, body))
    app.session.logout()
