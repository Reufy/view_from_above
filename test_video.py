# from scipy.spatial import distance
import cv2
import dlib
import time

# neural-network
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('./neural_network/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('./neural_network/dlib_face_recognition_resnet_model_v1.dat')

descriptors_video = []
start = time.time()

i = 0
# Загрузка видеофайла
vid = cv2.VideoCapture('videoplayback.mp4')

while vid.isOpened():
    # Чтение видеофайла
    ret, frame = vid.read()
    # Преобразование изображниея в серый цвет
    video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Трансляция видео
    cv2.imshow('frame', video)
    # Определения лиц
    if i == 0 or i % 40 == 0:
        dets_second_photo = detector(frame, 1)
        # обработка лиц и их выделение k - колличество лиц d - координаты лица
        for k, d in enumerate(dets_second_photo):
            # запись координат лица
            shape = sp(video, d)
            # получение координат для отрисовки квадрата
            x1 = d.left()
            y1 = d.top()
            x2 = d.right()
            y2 = d.bottom()
            # отрисовка квадрата по углам, цвет квадрата, толщина линии
            cv2.rectangle(video, (x1, y1), (x2, y2), (0, 255, 0), 1)
            # отображение квадрата на видео
            cv2.imshow('frame', video)
            # извлечение дискриптора лица

            face_descriptor = facerec.compute_face_descriptor(frame, shape)
            print(list(face_descriptor))
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

        # время ожидания следующего кадра (1мс)
        key = cv2.waitKey(1)
        # нажатия кнопки Esc для выхода из окна
        if key == 27:
            end = time.time()
            print(end - start)
            break
    key = cv2.waitKey(1)
    # нажатия кнопки Esc для выхода из окна
    if key == 27:
        end = time.time()
        print(end - start)
        break
    i += 1
end = time.time()
print(end - start)
# закрытие видео файла и всех окон
vid.release()
cv2.destroyAllWindows()
