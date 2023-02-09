import pytest

from fixtures import (fixture_doc, 
    fixture_check_name, 
    fixture_check_number, 
    fixture_check_shelf, 
    fixture_people, 
    fixture_shelf, 
    fixture_add_to_list, 
    fixtures_data_add_to_list)

from main import (check_name, check_number, check_shelf, people, shelf, add_to_list)

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

# @pytest.mark.parametrize("type, number, name", fixture_add_to_list)
# def test_add_to_list(type, number, name):
#     result = add_to_list(fixture_doc(), type, number, name)
#     assert result == fixture_add_to_list()


