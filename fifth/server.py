from flask import Flask
from flask import request
from hashlib import sha256
from time import time

mining_time = []
block_time = 5#sec
get_256 = lambda x: sha256(x.encode('utf-8')).hexdigest()
app = Flask(__name__)
names, blocks, cur_blk_num, last_sha, сomplexity, extra_сomp = 'Adams,Baker,Clark,Davis,Evans,Frank,Ghosh,Hills,Irwin,Jones,Klein,Lopez,Mason,Nalty,Ochoa,Patel,Quinn,Reily,Smith,Trott,Usman,Valdo,White,Xiang,Yakub'.split(','), [], 0, '0'*64, 4, 0
fut_block = lambda *x: f'{сomplexity+extra_сomp}:{names[cur_blk_num]}:{last_sha}' if len(blocks) < len(names) else ''
def extra_сomplexity():
  num_times = len(mining_time)
  if num_times > 1:
    global extra_сomp
    if sum([mining_time[i] - mining_time[i-1] for i in range(1, num_times)])/(num_times-1) > block_time:
      if extra_сomp > 0:
        extra_сomp -= 1
    else:
      extra_сomp += 1

@app.route('/')
def main():
  return '<br>'.join([f'{i+1} ➡ {b}'for i, b in enumerate(blocks)][::-1])

@app.route('/future-block', methods=['GET'])
def future_block():
  return fut_block()

@app.route('/future-block', methods=['POST'])
def post_future_block():
  block = request.form['block']
  block256 = get_256(block)
  print(block)
  if ((sum([1 for i in block256[:сomplexity+extra_сomp] if i=='0'])==сomplexity+extra_сomp) and (block.count(':')==4) and (fut_block() in block) and (len(blocks) < len(names))):
    blocks.append(block)
    global cur_blk_num
    cur_blk_num += 1
    global last_sha
    last_sha = block256
    mining_time.append(int(time()))
    extra_сomplexity()
    return 'Success', 201 
  return 'Invalid', 403

app.run(host='0.0.0.0', port=8080)
