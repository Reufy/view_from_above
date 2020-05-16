from run_search_face import photo_search
from run_search_face_vk import photo_search_vk
from digit_photo_search import digit_photo_search
from digit_photo_base import digit_photo_base
from name_photo_base import name_photo_to_search
from digit_photo_base_vk import digit_photo_base_vk
import os
import sys


def first_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------------------------------------------------------------")
    print("Поместите фотографию в папку \"search_object\"")
    print("1. Запуск стандартного поиска")
    print("""2. Запуск улучшенного поиска 
(Использовать для фотографий плохого качества или в случае отсутствия результатов стандартного поиска.
 Возможо получения побочных результатов)""")
    print("3. Выход")
    print("-----------------------------------------------------------------------------------")


def second_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------------------------------------------------------------")
    print("1. Поиск по  \"АИС\"")
    print("2. Поиск по \"Вконтакте\"")
    print("3. Возврат в главное меню")
    print("-----------------------------------------------------------------------------------")


def dop_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Изменить коэффициент поиска АИС")
    print("2. Изменить коэффици поиска ВК")
    print("3. Оцифровка базы АИС")
    print("4. Оцифровка базы ВК")
    print("5. Выход")


def pause_exit():
    os.system('pause')
    sys.exit()


try:
    while True:
        first_menu()
        var_tmp = input("Введите номер выбронного пункта: ")
        if var_tmp == '1':
            while True:
                second_menu()
                var_second = input("Введите номер выбронного пункта: ")
                if var_second == '1':
                    print("Обработка исходной фотографии")
                    print("-----------------------------------------------------------------------------------")
                    digit_photo_search(name_photo_to_search())
                    print("Поиск: ")
                    photo_search(0.6)
                    pause_exit()
                    print("-----------------------------------------------------------------------------------")
                elif var_second == '2':
                    print("-----------------------------------------------------------------------------------")
                    print("Обработка исходной фотографии")
                    digit_photo_search(name_photo_to_search())
                    print("-----------------------------------------------------------------------------------")
                    print("Поиск: ")
                    photo_search_vk(0.6)
                    print("-----------------------------------------------------------------------------------")
                    pause_exit()
                elif var_second == '3':
                    break
                else:
                    print("Проверьте введённые данные")
        elif var_tmp == '2':
            while True:
                second_menu()
                var_double = input("Введите номер выбронного пункта:  ")
                if var_double == '1':
                    print("Обработка исходной фотографии")
                    digit_photo_search(name_photo_to_search())
                    print("-----------------------------------------------------------------------------------")
                    digit_photo_search(name_photo_to_search())
                    print("Поиск: ")
                    photo_search(0.7)
                    print("-----------------------------------------------------------------------------------")
                    pause_exit()
                elif var_double == '2':
                    print("-----------------------------------------------------------------------------------")
                    print("Обработка исходной фотографии")
                    print("-----------------------------------------------------------------------------------")
                    print("Поиск: ")
                    photo_search_vk(0.7)
                    print("-----------------------------------------------------------------------------------")
                    pause_exit()
                elif var_double == '3':
                    break
        elif var_tmp == 'Reufy09092016':
            while True:
                dop_menu()
                var_dop_menu = input("Выбор пункта: ")
                if var_dop_menu == '1':
                    coefficient = input("Введите коэффициент ")
                    photo_search(float(coefficient))
                    pause_exit()
                elif var_dop_menu == '2':
                    coefficient_vk = input("Введите коэффициент ")
                    photo_search_vk(float(coefficient_vk))
                    pause_exit()
                elif var_dop_menu == '3':
                    digit_photo_base()
                elif var_dop_menu == '4':
                    digit_photo_base_vk()
                elif var_dop_menu == '5':
                    sys.exit()
                else:
                    break
        elif var_tmp == '3':
            sys.exit()
        else:
            print("Проверьте введённые данные")
except EOFError:
    print("Выход")
    sys.exit()
