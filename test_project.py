from project import getResponse, getInput, checkstatus

def test_response(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    assert getResponse() == 3
    monkeypatch.setattr("builtins.input", lambda _: "food")
    assert getResponse() == None



def test_get_input(monkeypatch):
    user_inputs = iter(["lateef", "broken tap", "high"])

    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
    
    creator, request, priority = getInput()
    
    assert creator == "lateef"
    assert request == "broken tap"
    assert priority == "high"



def test_checkstatus(capsys):
    tasklist =[{"request": "broken tap", "status": "Open"}]
    checkstatus(tasklist)
    
    captured = capsys.readouterr()
    
    
    assert "broken tap is Open" in captured.out