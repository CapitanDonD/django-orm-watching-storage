# Пульт охраны банка
Это внутренний репозиторий для сотрудников охраны банка "Сияние". Если вы попали на этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но вы можете спокойно использовать код вёрстки или посмотреть как релизованы запросы к ДБ.

### Как установить
Если вы хотите запустить сайт, вам необходимо наличие файла ```.env```.
В нём должны такие значения как ```DATABASE_PASSWORD``` - пароль к базе данных, ```DATABASE_PORT``` - порт базы данных, ```DATABASE_HOST``` - хост базы данных, ```SECRET_KEY``` - секретный ключ, ```DATABASE_NAME``` - имя базы данных, ```DATABASE_USER``` - юзер охранника, ```DEBUG_VALUE``` - значение отладочной консоли, ```ALLOWED_HOSTS``` - допустимые хосты.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
