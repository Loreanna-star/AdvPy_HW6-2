import pytest

from fixtures import (fixture_doc,
    fixture_dir,
    fixture_check_name, 
    fixture_check_number, 
    fixture_check_shelf, 
    fixture_people, 
    fixture_shelf, 
    fixture_add_to_list,
    fixture_del_from_dict,
    fixture_move)

from main import (check_name, check_number, check_shelf, people, shelf, add_to_list, del_from_dict, move)

@pytest.mark.parametrize("list_doc, name, exp_result", fixture_check_name())
def test_check_name(list_doc, name, exp_result):
    result = check_name(list_doc, name)
    assert result == exp_result

@pytest.mark.parametrize("dict_doc, number, exp_result", fixture_check_number())
def test_check_number(dict_doc, number, exp_result):
    result = check_number(dict_doc, number)
    assert result == exp_result

@pytest.mark.parametrize("dict_doc, number, exp_result", fixture_check_shelf())
def test_check_shelf(dict_doc, number, exp_result):
    result = check_shelf(dict_doc, number)
    assert result == exp_result

@pytest.mark.parametrize("list_doc, number, exp_result", fixture_people())
def test_people(list_doc, number, exp_result):
    result = people(list_doc, number)
    assert result == exp_result

@pytest.mark.parametrize("dict_doc, doc_number, shelf_number", fixture_shelf())
def test_shelf(dict_doc, doc_number, shelf_number):
    result = shelf(dict_doc, doc_number)
    assert result == shelf_number

def test_add_to_list():
    list_docum = []
    add_to_list(list_docum, "некий документ", "1234567", "некий юзер")
    assert list_docum == fixture_add_to_list()

def test_del_from_dict():
    new_dict = fixture_dir()
    del_from_dict(new_dict, "11-2")
    assert new_dict == fixture_del_from_dict()

def test_move():
    new_dict = fixture_dir()
    move(new_dict, "11-2", "3")
    assert new_dict == fixture_move()

    

