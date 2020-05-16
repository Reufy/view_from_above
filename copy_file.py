from shutil import copyfile


def copy_photo(photo_name, a):
    try:
        copyfile(r'./base_photo_ais\{}'.format(photo_name), r'./result_photo\{}--{}'.format(a, photo_name))
    except IOError:
        print("Ошибка копирования файла")
