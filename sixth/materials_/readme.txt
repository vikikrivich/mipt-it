1-2) Создать страничку, которая покажет хеш введёной строки
SHA256, MD5, CRC-32
https://www.youtube.com/watch?v=xV8USnjKGCU

1.1 Создать новую страничку
def hash_page
url: /hash
request type: get
template: hash.html
form с одним input type="text"

1.2 Создать страничку для POST запроса
def post_hash_page
url: /hash
request type: post
template: hash.html
Принять и вернуть ту же строку

1.3 Пусть форма вернёт SHA256

1.4 Теперь MD5 и CRC-32
import zlib
get_crc = lambda x: hex(zlib.crc32(x.encode('utf-8')))[2:]

1.5 Проверьте правильность хешей
https://emn178.github.io/online-tools/crc32.html

***

3-5) Работа с файлами

3) Разархивируйте docx файл
#https://stackoverflow.com/questions/3451111/unzipping-files-in-python
4) Пройдитесь по всем xml файлам и найдите файл с Hello!11111
#https://realpython.com/get-all-files-in-directory-python/
5) Hello!11111 замените на Hi, YOUR_NAME и добавьте картинку schedule.png
Заархивируйте обратно в .docx и откройте в Open Office или Google Docs
#https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory

and photos
