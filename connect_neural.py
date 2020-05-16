import dlib

# Загрузка нейросети
sp = dlib.shape_predictor('./neural_network/shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('./neural_network/dlib_face_recognition_resnet_model_v1.dat')
# Загрузка модуля распознавания лица
detector = dlib.get_frontal_face_detector()
