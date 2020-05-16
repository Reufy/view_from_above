from os import listdir
import os
import sys


def name_photo_in_base():
    # Получение имён фотографий из базы
    path_name = listdir('base_photo_ais')
    if path_name:
        result_name_photo = [len(path_name), path_name]
        return result_name_photo
    else:
        print("В папке './base_photo_ais' Отсутствуют фотографии для обработки")
        os.system('pause')
        sys.exit()


def name_photo_in_base_vk():
    # Получение имён фотографий из базы
    path_name = listdir('./base_photo_vk')
    if path_name:
        result_name_photo = [len(path_name), path_name]
        return result_name_photo
    else:
        print("В папке './base_photo_vk' Отсутствуют фотографии для обработки")
        os.system('pause')
        sys.exit()


def name_photo_to_search():
    # Получение имени искомого фото
    path_name = listdir('./search_object')
    result_search_photo = [len(path_name), path_name]
    return result_search_photo
