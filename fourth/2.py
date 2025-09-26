import requests

def get_exchange_rate(currency_sym):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    if currency_sym == '$':
        currency_type='USD'
    elif currency_sym == '₽':
        currency_type='RUB'

    try:
        res = requests.get(url)
        if res.status_code == 200:
            from xml.etree import ElementTree as ET
            root = ET.fromstring(res.text)
            
            for valute in root.findall('Valute'):
                char_code = valute.find('CharCode').text
                if char_code == currency_type:
                    value = valute.find('Value').text
                    nominal = valute.find('Nominal').text
                    rate = float(value.replace(',', '.')) / float(nominal)
                    return rate
            
            print(f"{currency_type} hasn't found")
            return None
        else:
            print(res.status_code)
            return None
        
    except Exception as e:
        print(e)
        return None
    

def convert_currency(amount_s):
    amount = float(amount_s[1:])
    usd_rate = get_exchange_rate(amount_s[0])
    
    return amount * usd_rate

s = '$100'
amount = convert_currency(s)
print(amount)