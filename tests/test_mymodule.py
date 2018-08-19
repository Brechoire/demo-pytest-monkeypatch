from demo.mymodule import f


def test_f(monkeypatch, mocker):
    # Creation of a mock with the pytest-mock plugin to replace the 
    # random.choice function used in the demo.mymodule module.
    choice_mock = mocker.Mock()
    choice_mock.return_value = "réponse renvoyée par le mock de random.choice"

    # The monkeypatch fixture allows to patch the choice function in 
    # in demo.mymodule
    monkeypatch.setattr(
        'demo.mymodule.choice', 
        choice_mock
    )

    # f() will now return the same value as choice_mock()
    assert f([1,2,3,4,5]) == choice_mock()
