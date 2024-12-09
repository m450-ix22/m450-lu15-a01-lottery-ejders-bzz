from authenticate import login, load_people


def test_load_people():
    people = load_people()

    assert len(people) == 3

    assert people[0].givenname == 'Inga'
    assert people[0].password == 'geheim'
    assert people[0].balance == 14.00


def test_login_successful(monkeypatch):
    attempts = iter(['wrongpass', 'geheim'])
    monkeypatch.setattr('builtins.input', lambda _: next(attempts))
    person = login()

    assert person is not None
    assert person.givenname == 'Inga'
    assert person.password == 'geheim'
    assert person.balance == 14.00


def test_login_failure(monkeypatch):
    attempts = iter(['wrongpass', 'anotherwrong'])
    monkeypatch.setattr('builtins.input', lambda _: next(attempts))
    person = login()

    assert person is None
