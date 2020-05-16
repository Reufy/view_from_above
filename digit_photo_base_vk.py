from name_photo_base import name_photo_in_base_vk
from skimage import io
import shelve
import dlib
import time



def digit_photo_base_vk():
    # Загрузка нейросети
    sp = dlib.shape_predictor('./neural_network/shape_predictor_68_face_landmarks.dat')
    facerec = dlib.face_recognition_model_v1('./neural_network/dlib_face_recognition_resnet_model_v1.dat')
    # Загрузка модуля распознавания лица
    detector = dlib.get_frontal_face_detector()

    def values_digit(photo_name):
        descriptors_vk = []
        # Загрузка базы фотографий и получения значения Евклидового пространства
        # Разместите фотографии для сравнения в папку ./base_photo_ais
        img = io.imread('./base_photo_vk\\{}'.format(photo_name))
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

    def digitization(descriptors_vk, file_vk, photo_name):
        # Отцифровка поступающего фото фото
        i = 1
        for descriptor in descriptors_vk:
            file_vk[str(i) + "_" + photo_name] = descriptor
            i = i + 1

    # main()
    # Сохрание оцифрованных фотографий в бинарный файл
    start_time = time.time()
    with shelve.open("index_base_photo_vk\\index_base_photo_vk", flag='n') as file_vk:
        name_file = name_photo_in_base_vk()
        for x in name_file[1]:
            try:
                digitization(values_digit(x), file_vk, x)
            except UnboundLocalError:
                print("Лицо на фотографии " + x + " не распознано! Измените данную фотографию, либо загрузите другую")
                continue
    print("--- %s seconds ---" % (time.time() - start_time))

