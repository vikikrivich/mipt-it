import bottle
import hashlib
import zlib

@bottle.route('/mul')
def mul_page():
  return bottle.template('mul.html')

@bottle.post('/mul')
def post_mul():
  a = bottle.request.forms.get('a')
  b = bottle.request.forms.get('b')
  try:
    c = int(a) * int(b)
  except:
    c = ''
  return bottle.template('mul.html', a=a, b=b, c=c)

@bottle.route('/hash')
def hash_page():
  return bottle.template('hash.html')

@bottle.post('/hash')
def post_hash_page():
  text = bottle.request.forms.get('text', '')
  sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
  md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
  crc32_hash = format(zlib.crc32(text.encode('utf-8')) & 0xffffffff, '08x')
  return bottle.template('hash.html', text=text, sha256=sha256_hash, md5=md5_hash, crc32=crc32_hash)

@bottle.route('/') 
def index():
  return 'Site is up!'

bottle.run(host='0.0.0.0', port=8080)