# from scipy.spatial import distance
import cv2
import dlib
import time
from multiprocessing import Process

# neural-network
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('./neural_network/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('./neural_network/dlib_face_recognition_resnet_model_v1.dat')

descriptors_video = []
start = time.time()


def detect(frame, video):
    dets_second_photo = detector(frame, 1)
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
        print(k)



# Загрузка видеофайла
vid = cv2.VideoCapture('videoplayback.mp4')

while vid.isOpened():
    i = 0
    arr_process = []
    # Чтение видеофайла
    ret, frame = vid.read()
    # Преобразование изображниея в серый цвет
    video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Трансляция видео
    cv2.imshow('frame', video)
    # Определения лиц
    if i == 0 or i % 1000000 == 0:
        subproc = Process(target=detect, args=(frame, video))
        arr_process.append(subproc)
        subproc.start()
    i += 1

    key = cv2.waitKey(1)
    # нажатия кнопки Esc для выхода из окна
    if key == 27:
        end = time.time()
        print(end - start)
        break
end = time.time()
print(end - start)
# закрытие видео файла и всех окон
vid.release()
cv2.destroyAllWindows()
