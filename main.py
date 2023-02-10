documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def check_name(documents_list, name):
    for document in documents_list:
        if name == document["name"]:
            return True
    else:
        return False

def check_number(directories_dict, number):
    for directory, content in directories_dict.items():
        if number in content:
            return True
    else:
        return False
        
def check_shelf(directories_dict, shelf_number):
    if shelf_number not in directories_dict.keys():
        return False  
    else:
        return True
   

def people(documents_list, number):
    for document in documents_list:
        if number == document["number"]:
            return document["name"]

def shelf(directories_dict, number):
    for directory, content in directories_dict.items():
        if number in content:
            return directory
 
def list_doc(documents_list):
    for document in documents_list:
        print(f'{document["type"]} {document["number"]} {document["name"]}')
    return

def add_to_list(documents_list, type, number, name):
    new_doc = {"type": type, "number":number, "name":name}
    documents_list.append(new_doc)
    return

def add_to_dict(directories_dict, number, shelf_number):
    directories_dict[shelf_number].append(number)
    return

def add(documents_list, directories_dict, type, number, name, shelf_number):
    add_to_list(documents_list, type, number, name)
    add_to_dict(directories_dict, number, shelf_number)
    return

def del_from_list(documents_list, number):
    for document in documents_list[:]:
        if number == document["number"]:
            documents_list.remove(document)
            return
        
def del_from_dict(directories_dict, number):
    for value in list(directories_dict.values()):
        if number in value:
            value.remove(number)                 
            return directories_dict

def move(directories_dict, number, shelf_number):  
    del_from_dict(directories_dict, number)
    add_to_dict(directories_dict, number, shelf_number)
    return directories_dict

def add_shelf(directories_dict, shelf_number):
    directories_dict[shelf_number] = []
    return

def main(documents_list, directories_dict):
    while True:
        command = input("Введите команду: ")
        
        if command == "p":
            number = str(input("Введите номер документа: "))
            if check_number(directories_dict, number) == False:
                print("Неверный номер документа")
            else:
                print(people(documents_list, number))
            
        elif command == "s":
            number = str(input("Введите номер документа: "))
            if check_number(directories_dict, number) == False:
                print("Неверный номер документа")
            else:
                print(f"Документ с номером {number} находится на полке {shelf(directories_dict, number)}")
                            
        elif command == "l":
            list_doc(documents_list)
            
        elif command == "a":
            shelf_number = str(input("Введите номер полки: "))
            if check_shelf(directories_dict, shelf_number) == False:
                print("Неверный номер полки")
            else:
                type = str(input("Введите тип документа: "))
                number = str(input("Введите номер документа: "))
                name = str(input("Введите имя автора: "))
                add(documents_list, directories_dict, type, number, name, shelf_number)
                print(f"Документ с номером {number} успешно добавлен на полку {shelf_number}")
                print(documents_list)
                print(directories_dict)
                        
        elif command == "d":
            number = str(input("Введите номер документа: "))
            if check_number(directories_dict, number) == False:
                print("Неверный номер документа")
            else:
                del_from_list(documents_list, number)
                del_from_dict(directories_dict, number)
                print(f"Документ с номером {number} успешно удален")
                print(documents_list)
                print(directories_dict)

        elif command == "m":
            number = str(input("Введите номер документа: "))
            if check_number(directories_dict, number) == False:
                print("Неверный номер документа")
            else:
                shelf_number = str(input("Введите номер полки: "))
                if check_shelf(directories_dict, shelf_number) == False:
                    print("Неверный номер полки")
                else:
                    move(directories_dict, number, shelf_number)
                    print(f"Документ с номером {number} успешно перемещен на полку {shelf_number}")
                    print(directories_dict)

        elif command == "as":
            shelf_number = str(input("Введите номер полки: "))
            if check_shelf(directories_dict, shelf_number) == True:
                print("Полка с таким номером уже существует")
            else:
                add_shelf(directories_dict, shelf_number)
                print(f'Полка номер {shelf_number} успешно добавлена')
                print(directories_dict)                
        
        elif command == "q":
            print("Завершение работы")
            return

# main(documents, directories)

if __name__ == '__main__':
    main(documents, directories)
