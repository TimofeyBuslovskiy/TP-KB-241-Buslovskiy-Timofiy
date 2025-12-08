import pytest
from lab_02 import addNewElement, deleteElement, updateElement, list

def test_addNewElement (monkeypatch) :
    list.clear()
    inputs = iter(['Anna', '063', 'anna@gmail.com', 'female'])
    monkeypatch.setattr('bultins.input', lambda _: next(inputs))

    addNewElement()
    assert len(list) == 1
    assert list[0]['name'] == 'Anna'
    assert list[0]['phone'] == '063'
    assert list[0]["email"] == 'anna@gmail.com'
    assert list[0]["gender"] == 'female'

def test_deleteElement (monkeypatch) :
    list.clear()
    list.append({'name' : 'Zak', 'phone' : '099', 'email' : 'zak@gmail.com', 'gender' : 'male'})
    list.append({'name' : 'Bob', 'phone' : '098', 'email' : 'bob@gmail.com', 'gender' : 'male'})

    monkeypatch.setattr('bultin.input', lambda _: 'Zak')
    deleteElement()
    assert len[list] == 1
    assert list[0]["name"] == "Bob"

    monkeypatch.setattr('builtins.input', lambda _: 'NonExistent')
    deleteElement()
    assert len(list) == 1

def test_updateElment (monkeypatch) :
    list.clear()
    list.append({'name' : 'Zak', 'phone' : '099', 'email' : 'zak@gmail.com', 'gender' : 'male'})
    inputs = iter(['Zak', 'Updated Name', '097', 'zak@mail', 'male'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    updateElement()
    assert len(list) == 1
    assert list[0]["name"] == "Updated Name"
    assert list[0]["phone"] == "097"
    assert list[0]["email"] == "zak@mail"
    assert list[0]["gender"] == "male"

    monkeypatch.setattr('builtins.input', lambda _: 'NonExistent')
    updateElement() 
    assert len(list) == 1 

