from typing import TextIO


def clear_names(file_name: str) ->list:
    """Функция для очистки имен от лишних символов"""
    new_list_names = list()
    with open('data/' + file_name, 'r', encoding='utf8') as file:
         names_list = file.read().split()
         for name_items in names_list:
             new_name = ""
             for item in name_items:
                 if item.isalpha():
                     new_name += item
             if new_name.isalpha():
                 new_list_names.append(new_name)




    return new_list_names


if __name__ == "__main__":
   clear_name = clear_names('names.txt')

   for i in clear_name:
       print(i)

