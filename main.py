# В системе создан пользователь
#
# 1	Аутентификация пользователя с корректными полями:
# 	Выполнить GET-запрос на /api/key с корректными полями email и password
# 	Логин	igor_chunaev@gmail.com
# 	Пароль	igorCh.78.
#
# 2	Аутентификация пользователя с некорректными полями:
# 	Выполнить GET-запрос на /api/key с некорректными полями email и password
# 	Логин	igor@mail.ru
# 	Пароль	password_123
#
# 3	Аутентификация пользователя с пустыми полями:
# 	Выполнить GET-запрос на /api/key с некорректными полями email и password
# 	Логин	-
# 	Пароль	-
#
# 4	Получение списка всех питомцев:
# 	Выполняем GET-запрос на /api/pets
#
# 5	Получение списка питомцев c пустым значением api ключа:
# 	Выполняем GET-запрос на /api/pets.
#
# 6	Добавление питомца cat_01 (с фото, все поля заполнены корректно):
# 	Выполнить POST-запрос на /api/pets
# 	Имя	Мечтатель
# 	Порода	Котейка
# 	Возраст	1
# 	Фото	cat_01.jpg
#
# 7	Добавление питомца cat_02 (с фото, поля не заполнены):
# 	Выполнить POST-запрос на /api/pets
# 	Имя	-
# 	Порода	-
# 	Возраст	-
# 	Фото	cat_02
#
# 8	Изменение данных питомца cat_02 (без фото, все поля заполнены некорректно):
# 	Выполнить PUT-запрос на /api/pets/{pet_id} с некорректными параметрами
# 	Имя	9999999999999999АБВГДЕЖЗИКЛМНОПРСТ
# 	Порода	9999999999999999АБВГДЕЖЗИКЛМНОПРСТ
# 	Возраст	9999999999999999АБВГДЕЖЗИКЛМНОПРСТ
# 	Фото	-
#
# 9	Удаление первого добавленного питомца cat_02:
# 	Выполнить DELETE-запрос на /api/pets/{pet_id} на удаление добавленного питомца
#
# 10	Добавление питомца dog_01 (без фото, все поля заполнены не корректно):
# 	Выполнить POST-запрос на /api/pets
# 	Имя	!"№;%:?*
# 	Порода	!"№;%:?*
# 	Возраст	-0,1
# 	Фото	-
#
# 11	Изменение данных питомца dog_01 (без фото, все поля заполнены корректно):
# 	Выполнить PUT-запрос на /api/pets/{pet_id} с корректными параметрами
# 	Имя	Красавчик
# 	Порода	Коржик
# 	Возраст	2
# 	Фото	-
#
# 12	Изменение данных питомца dog_01 (добавление фото):
# 	Выполнить POST-запрос на /api/pets/set_photo/{pet_id}
# 	Фото	dog_01.jpg
#
# 13	Добавление питомца (без фото, все поля не заполнены):
# 	Выполнить POST-запрос на /api/pets
# 	Имя	-
# 	Порода	-
# 	Возраст	-
# 	Фото	-
#
# 14	Удаление последнего добавленного питомца:
# 	Выполнить DELETE-запрос на /api/pets/{pet_id} на удаление добавленного питомца
