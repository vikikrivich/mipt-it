import re
from translate import Translator

def translate_word(s, lang):
    translator = Translator(to_lang=lang)
    return translator.translate(s)


s = "Hello"

english_pattern = r'[a-zA-Z]'
russian_pattern = r'[а-яА-ЯёЁ]'
en_count = len(re.findall(english_pattern, s))
ru_count = len(re.findall(russian_pattern, s))


if en_count > ru_count:
    res = translate_word(s, 'ru')
else:
    res = translate_word(s, 'en')

print(res)
