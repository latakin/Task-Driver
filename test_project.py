from project import getResponse, getInput
import pytest

def test_response(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert getResponse() == 3
    monkeypatch.setattr("builtins.input", lambda _: "food")
    assert getResponse() == None
