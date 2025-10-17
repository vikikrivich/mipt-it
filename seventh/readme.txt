https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=apple
https://en.wikipedia.org/w/api.php?action=parse&prop=text&page=San_Francisco&format=json

https://en.wikipedia.org/w/api.php?action=parse&prop=text&pageid=49728&format=json
https://pypi.org/project/requests/
https://requests.readthedocs.io/en/master/user/quickstart/#passing-parameters-in-urls

https://bottlepy.org/docs/dev/stpl.html#embedded-python-code

% for page in get('wpages', ''):
    <li>{{page['title']}}</li>
% end


1. Поиск по Википедии. Работа с api.
- Перейти по ссылке https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=apple
- Скопировать json и вставить на сайт http://jsonviewer.stack.hu/
- Нажать кнопку Format. Увидеть какую структуру имеют данные
- Создать временный проект repl.it с Python и далее писать код в main.py
- Импортировать библиотеку для запросов https://pypi.org/project/requests/
- Сделать GET запрос по ссылке https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=apple , используя библиотеку requests и оформив входные параметры правильно. Как показано здесь https://requests.readthedocs.io/en/master/user/quickstart/#passing-parameters-in-urls
- Строку json превратить в данные (десериализация - deserialize). Как показано здесь https://pypi.org/project/requests/
- Вытащить из данных все title и создать отдельный список из этих title

2. Создать сайт со списком title-ов
2.1 Создать сайт на Bottle
- Создать проект repl.it с Bottle
- Создать вьюшку с роутом /wiki
- Создать static/wiki.html и static/base.html как с прошлого занятия.
- В wiki.html создать форму с одним полем и кнопкой submit. Тоже можно копипастнуть с прошлого занятия.
- Пусть имя для поля будет называться srsearch. <input name="srsearch"
- Создать вьюшку с роутом /wiki для POST запросов, которая будет принимать srsearch с формы

2.2 Вывести список title-ов
- Скопировать во вьюшку весь код с пункта 1.1
- srsearch вставлять параметром в запрос к api Википедии
- Передать на рендер список title-ов
- В wiki.html написать цикл for для вывода списка. Наподобие такого:
% for page in get('wpages', ''):
    <li>{{page}}</li>
% end

2.3 Проверить, что поиск работает и список меняется

3. Вывод страницы с Википедии
3.1 Меняем список на список ссылок
- Заменить список title-ов на список словарей с ключами title и pageid
Вот для примера вывод title-ов из списка словарей:
% for page in get('wpages', ''):
    <li>{{page['title']}}</li>
% end
- В wiki.html список заменить на список ссылок /page/<pageid>

4. Страница Википедии
4.1 Работа с api. Аналогично пункту 1.1!
- https://en.wikipedia.org/w/api.php?action=parse&prop=text&pageid=49728&format=json
- Вытащить title и text

4.2 Страница вики
- Создать вьюшку /page/<pageid>
- Скопировать код с 2.1 и вставить во вьюшку /page/<pageid>
- Убрать экранирование с text
- title оформить как <h1>

4.3 Проверить, что через поиск можно открывать разные страницы

5. Кэш
- Создать словарь в глобальной области видимости main.py
- При запросе списка по srsearch (1.), проверять есть ли такой ключ в словаре. Если есть, то вернуть содержимое (список) на рендер, иначе сделать запрос по api и сохранить список в словарь.
- Так надо кэшировать списки из 2.2 и страницы из 4.2













