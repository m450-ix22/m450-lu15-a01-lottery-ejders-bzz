from menu import select_menu


def test_select_menu_successful(monkeypatch):
    attempts = iter(['X', 'A'])  # Erste Eingabe ist ungültig, zweite ist gültig
    monkeypatch.setattr('builtins.input', lambda _: next(attempts))

    selection = select_menu()

    assert selection == 'A'