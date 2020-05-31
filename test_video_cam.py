from imutils.video import VideoStream
# from scipy.spatial import distance
import cv2
import dlib

# neural-network
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('./neural_network/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('./neural_network/dlib_face_recognition_resnet_model_v1.dat')

descriptors_ais = []

# Запуск видео потока
video_stream = VideoStream(src=0).start()

while True:
    # чтение видеопотока
    frame = video_stream.read()
    # преобразование видеопотока в серый цвет
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Определение лиц
    dets_second_photo = detector(img, 1)
    # обработка лиц и их выделение k - колличество лиц d - координаты лица
    for k, d in enumerate(dets_second_photo):
        # запись координат лица
        shape = sp(img, d)
        # получение координат для отрисовки квадрата
        x1 = d.left()
        y1 = d.top()
        x2 = d.right()
        y2 = d.bottom()
        # отрисовка квадрата по углам, цвет квадрата, толщина линии
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
        # if not descriptors_ais:
        #     face_descriptor = facerec.compute_face_descriptor(frame, shape)
        #     descriptors_ais.append((face_descriptor))
        #     print("В контейнер добавленно первое лицо")
        # else:
        #     face_descriptor = facerec.compute_face_descriptor(frame, shape)
        #     for x in descriptors_ais:
        #         a = distance.euclidean(x, face_descriptor)
        #         a = float(a)
        #         if a <= 0.7:
        #             pass
        #         else:
        #             descriptors_ais.append((face_descriptor))

    # Вывод преобразованного видеопотока
    cv2.imshow("frame", frame)

    # время ожидания следующего кадра (1мс)
    key = cv2.waitKey(1)
    # нажатия кнопки Esc для выхода из окна
    if key == 27:
        break
