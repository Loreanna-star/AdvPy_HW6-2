import pytest

def fixture_doc():
    return [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

def fixture_dir():
    return {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def fixture_check_name():
    fixture_document = fixture_doc()
    return [
        (fixture_document, "Василий Гупкин", True),
        (fixture_document, "Василий Гупкин", True),
        (fixture_document, "Василий Гупкин", True),
        (fixture_document, "левый юзер", False)
    ]

def fixture_check_number():
    fixture_directories = fixture_dir()
    return [
        (fixture_directories, "2207 876234", True),
        (fixture_directories, "11-2", True),
        (fixture_directories, "10006", True),
        (fixture_directories, "левый номер", False),
    ]

def fixture_check_shelf():
    fixture_directories = fixture_dir()
    return [
        (fixture_directories, "1", True),
        (fixture_directories, "2", True),
        (fixture_directories, "3", True),
        (fixture_directories, "4", False),
    ]

def fixture_people():
    fixture_document = fixture_doc()
    return [
        (fixture_document, "2207 876234", "Василий Гупкин"),
        (fixture_document, "11-2", "Геннадий Покемонов"),
        (fixture_document, "10006", "Аристарх Павлов"),
        (fixture_document, "12345", None),
    ]

def fixture_shelf():
    fixture_directories = fixture_dir()
    return [
        (fixture_directories, "2207 876234", "1"),
        (fixture_directories, "11-2", "1"),
        (fixture_directories, "10006", "2"),
        (fixture_directories, "12345", None),
    ]

def fixtures_add_to_list():
    return [
        "some_document",
        "1234567",
        "левый юзер",
        [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "some_document", "number": "1234567", "name": "левый юзер"}]
      ]
