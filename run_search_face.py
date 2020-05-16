from scipy.spatial import distance
import shelve
import time


# Для копирования файлов при наличии фотографий
# from copy_file import copy_photo


def photo_search(coefficient):
    def result_photo(photo_name, first_photo_dig, second_photo_load):
        # Сравнение фотогрфий
        a = distance.euclidean(first_photo_dig, second_photo_load)
        a = float(a)
        if a <= coefficient:
            # a = str('{:.3}'.format(a))
            print("Найдено совпадение искомой фотографии с {}".format(photo_name))
        # При наличии фотографий для копирования файлов
        # copy_photo(photo_name, a)
        # print("Файл скопирован в result_photo")

    # main()
    with shelve.open('./index_first_photo\\index_first_photo') as index_first_dec:
        first_photo_dig = index_first_dec['fp']
    try:
        with shelve.open('index_base_photo_ais\\index_base_photo_ais', 'r') as testfile:
            if testfile:
                start_time = time.time()
                for unloading_name, unloading_data in testfile.items():
                    photo_name = unloading_name
                    second_photo_load = unloading_data
                    result_photo(photo_name, first_photo_dig, second_photo_load)
                print("--- %s seconds ---" % (time.time() - start_time))
    except:
        print("Отсутствуют изображения для сравнения")
