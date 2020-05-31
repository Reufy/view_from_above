from scipy.spatial import distance
import shelve
import time


# Для копирования файлов при наличии фотографий
# from copy_file import copy_photo


def photo_search(coefficient):
    def result_photo(photo_name_f, first_photo_dig_f, second_photo_load_f):
        # Сравнение фотогрфий
        a = distance.euclidean(first_photo_dig_f, second_photo_load_f)
        a = float(a)
        if a <= coefficient:
            if a <= 0.30:
                a = 100
            elif 0.30 < a <= 0.40:
                a = 98
            elif 0.40 < a <= 0.45:
                a = 96
            elif 0.45 < a <= 0.47:
                a = 95
            elif 0.47 < a <= 0.49:
                a = 92
            elif 0.49 < a <= 0.51:
                a = 88
            elif 0.51 < a <= 0.55:
                a = 85
            elif 0.55 < a <= 0.59:
                a = 80
            elif 0.59 < a <= 0.60:
                a = 75
            elif 0.60 < a <= 0.62:
                a = 73
            elif 0.62 < a <= 0.64:
                a = 71
            elif 0.64 < a <= 0.66:
                a = 65
            elif 0.66 < a <= 0.68:
                a = 60
            elif 0.68 < a <= 0.70:
                a = 50
            else:
                a = 1 - coefficient
            a = str(a)
            res_name = a + "% совпадение  c фотографией пользователя л/н: " + photo_name_f
            return res_name
            # print("Найдено совпадение искомой фотографии с {}  ".format(photo_name_f) + a)
        else:
            pass
        # При наличии фотографий для копирования файлов
        # copy_photo(photo_name, a)
        # print("Файл скопирован в result_photo")

    # main()
    arr_result = []
    with shelve.open('./index_first_photo/index_first_photo') as index_first_dec:
        first_photo_dig = index_first_dec['fp']
    try:
        with shelve.open('index_base_photo_ais/index_base_photo_ais', 'r') as photo_file:
            if photo_file:
                start_time = time.time()
                for unloading_name, unloading_data in photo_file.items():
                    photo_name = unloading_name
                    second_photo_load = unloading_data
                    ret_app_arr = result_photo(photo_name, first_photo_dig, second_photo_load)
                    if ret_app_arr:
                        arr_result.append(ret_app_arr)
                arr_result.sort()
                for x in arr_result:
                    print(x)
                print("--- %s seconds ---" % (time.time() - start_time))
    except:
        print("Отсутствуют изображения для сравнения")
