from skimage import io
import dlib
import shelve
import os
import sys


def pause_exit():
    os.system('pause')
    sys.exit()


def digit_photo_search(result_search_photo):
    array_search_photo = result_search_photo[1]
    if result_search_photo[0] > 1:
        print("В папке для поиска находтся более одной фотографии")
        pause_exit()
    for x in array_search_photo:
        search_photo_name = x
    # Загрузка нейросети
    sp = dlib.shape_predictor('./neural_network/shape_predictor_68_face_landmarks.dat')
    facerec = dlib.face_recognition_model_v1('./neural_network/dlib_face_recognition_resnet_model_v1.dat')
    # Загрузка модуля распознавания лица
    detector = dlib.get_frontal_face_detector()
    # Загрузка искомого фото
    try:
        img = io.imread("./search_object/{}".format(search_photo_name))
    except FileNotFoundError:
        print("Отсутствует фотография для поиска")
        pause_exit()
    except UnboundLocalError:
        print("Отсутствует фотография для поиска")
        pause_exit()
    # Для отображения изображений и наложения маски
    try:
        win1 = dlib.image_window()
        win1.clear_overlay()
        win1.set_image(img)
        dets = detector(img, 1)
        # определение позиций контрольных точек
        for k, d in enumerate(dets):
            shape = sp(img, d)
            # Для отображения изображений и наложения маски
            win1.clear_overlay()
            win1.add_overlay(d)
            win1.add_overlay(shape)
        # Получение дискриптора первой фотографии
        try:
            face_descriptor1 = facerec.compute_face_descriptor(img, shape)
            id_photo = 'fp'
            first_index = shelve.open("./index_first_photo/index_first_photo", 'n')
            first_index[id_photo] = face_descriptor1
            first_index.close()
        except UnboundLocalError:
            print("Лицо на фотографии " + search_photo_name + "не распознано! Измените данную фотографию, либо загрузите "
                                                              "другую")
            pause_exit()
    except TypeError:
        print("Необходимо преобразовать фотоизображение в формат .jpg")
        pause_exit()