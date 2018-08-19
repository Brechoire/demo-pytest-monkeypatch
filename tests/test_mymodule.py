from demo.mymodule import f


def test_f(monkeypatch, mocker):
    choice_mock = mocker.Mock()
    choice_mock.return_value = "réponse renvoyée par le mock de random.choice"
    monkeypatch.setattr(
        'demo.mymodule.choice', 
        choice_mock
    )
    assert f([1,2,3,4,5]) == choice_mock()
