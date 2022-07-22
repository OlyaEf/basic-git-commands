# Команды командной строки для работы в GIT
# $ cd - перейти в нужную папку
# $ ls (dir - для windows) - посмотреть содержимое папки
# $ cd.. - вернуться в первоначальную папку

# Для клонирования репозитория:
# $ git clone https://github.com/OlyaEf/basic-git-commands.git

# Синхронизация проектов:
# Создадим новый файл index.py в наш репозиторий
# переходим внутрь папки репозитория
# $ git status - покажет нам статус нашего проекта

# мы видим, что наш файл создан но его нет в репозитории, что бы
# Внести наш файл в репозиторий:
# $ git add index.py  - наш файл в будет находится в стадии преддобавления

# что бы его добавть нужно будет ввести следующую команду:
# $ git commit -m "Add index.py"
# $ git push

# Cкачать файлы из облако себе на локальную папку:
# $ git pull

# Залить несколько файлов в репозиторий:
# $ git add -A
# далее введя $ git status мы видим что наши файлы готовы к изменением
# на репозитории
# $ git commit -m "Made some changes"  - внести измениния, файлы уже будут готовы к перемещению
# $ git remote add terminal-cmm-bas-.py https://github.com/OlyaEf/basic-git-commands.git
# $ git push terminal-cmm-bas-.py

# !ГИД далее запросит имя и пароль!

# Если хотим увидеть файлы у себя
# $ git pull

# Работая в Git в команде первым делоМ:
# $ git pull
# а, далее вносим измения

# Если вы попали в окно с ошибкой, то выйти из него можно следущим образом:
# нажать Esc внизу написать двоеточие и прописать wq >> (:wq)
# после этого вы можете выйти из этого окошка

# $ git init - лицензирует репозиторий
