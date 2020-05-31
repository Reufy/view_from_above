from name_photo_base import name_photo_in_base_vk
from skimage import io
import multiprocessing
import shelve
import dlib
import time


def digit_photo_base_vk(sub_name_file_f, dop_f):
    # Загрузка нейросети
    sp = dlib.shape_predictor('./neural_network/shape_predictor_68_face_landmarks.dat')
    facerec = dlib.face_recognition_model_v1('./neural_network/dlib_face_recognition_resnet_model_v1.dat')
    # Загрузка модуля распознавания лица
    detector = dlib.get_frontal_face_detector()

    def values_digit(photo_name):
        descriptors_vk = []
        # Загрузка базы фотографий и получения значения Евклидового пространства
        # Разместите фотографии для сравнения в папку ./base_photo_ais
        img = io.imread('./base_photo_vk/{}'.format(photo_name))
        # Для отображения изображений и наложения маски
        # win2 = dlib.image_window()
        # win2.clear_overlay()
        # win2.set_image(img)
        dets_second_photo = detector(img, 1)
        # определение позиций контрольных точек
        for k, d in enumerate(dets_second_photo):
            shape = sp(img, d)
            # Для отображения изображений и наложения маски
            # win2.clear_overlay()
            # win2.add_overlay(d)
            # win2.add_overlay(shape)
            # Получение дискриптора фотографий из базы
            face_descriptor_vk = facerec.compute_face_descriptor(img, shape)
            descriptors_vk.append(face_descriptor_vk)
        return descriptors_vk

    def digitization(descriptors_vk, file_vk_f, photo_name):
        # Отцифровка поступающего фото фото
        i = 1
        for descriptor in descriptors_vk:
            file_vk_f[str(i) + "_" + photo_name] = descriptor
            i = i + 1

    # main()
    # Сохрание оцифрованных фотографий в бинарный файл
    start_time = time.time()
    column = dop_f
    with shelve.open("index_base_photo_vk/index_base_photo_vk", flag='ab') as file_vk:
        ost = len(sub_name_file_f)
        print("Всего фото обнаружено: " + str(ost))
        for x in sub_name_file_f:
            try:
                digitization(values_digit(x), file_vk, x)
                print("Фотографий обработано: " + str(column) + "\t" + "Осталось: " + str(ost))
                print("--- %s seconds ---" % (time.time() - start_time))
                ost = ost - 1
                column = column + 1
            except UnboundLocalError:
                print("Лицо на фотографии " + x + " не распознано! Измените данную фотографию, либо загрузите другую")
                print("Фотограффий обработано: " + str(column) + "\t" + "Осталось: " + str(ost))
                ost = ost - 1
                column = column + 1
                print("--- %s seconds ---" % (time.time() - start_time))
                continue
            except TypeError:
                print("Ошибка в фотографии: " + x)
                print("Фотограффий обработано: " + str(column) + "\t" + "Осталось: " + str(ost))
                ost = ost - 1
                column = column + 1
                print("--- %s seconds ---" % (time.time() - start_time))
                continue
    print("--- %s seconds ---" % (time.time() - start_time))

def start_digit_photo_vk():
    arr_process = []  # Список для хранения процессов
    name_file = name_photo_in_base_vk()  # namefile[0] - кол.фото namefile[1] - имена фото
    for dop in range(0, name_file[0], 50000):  # Колличество фото для каждого процесса
        sub_name_file = name_file[1][
                        dop:dop + 49999]  # sub_name_file = колличество имён
        subthread = multiprocessing.Process(target=digit_photo_base_vk, args=(sub_name_file, dop))
        arr_process.append(subthread)
        subthread.start()  # запуск процессов
