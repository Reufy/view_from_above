# view_from_above
Система для поиска лица на фотографии и его сравнение с лицами на фотографиях из Вашей БД.
Сравнения обнаружения и сравнения лиц происходит по средствам использования библиотеки dlib интегрированной в Python.
С целью ускорения обработки больших объёмов данных перед началом сравнения фотографий необходимо провести их оцифровку и сохранить полученные данные в бинарный файл.
Для запуска и использования данного приложения после установки всех зависимостей, необходимо поместить искомое изображение с суфиксом .jpg в каталог search_object, а изображения для базы данных в формате .jpg в каталог base_photo. после размещения данных приложений запустить файл digit_photo_base.py. Время отработки данного файла зависит от колличества фотографий и характеристик вашей ПЭВМ. 
После отработки данного файла, осуществить запуск приложения из main.py



A system for searching for faces in photographs and comparing them with faces in photographs from your database 
Face detection and comparison comparisons are made using the dlib library integrated in Python 
In order to speed up the processing of large volumes of data, before comparing photographs, it is necessary to digitize them and save the received data in a binary file. 
To run and use this application after installing all the dependencies, you must place the desired image with the suffix .jpg in the search_object directory, and the images for the database in .jpg format in the base_photo directory. After placing these applications, run the digit_photo_base.py file. The processing time of this file depends on the number of photos and the characteristics of your PC. 
After working out this file, launch the application from main.py.
