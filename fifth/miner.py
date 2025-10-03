import os
import hashlib
import random
import time
import requests
from dotenv import load_dotenv

load_dotenv()

class Miner:
    def __init__(self, miner_id):
        self.server_url = os.getenv('SERVER_URL')
        self.miner_id = miner_id
        
    def get_sha256(self, text):
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

    def mine_block(self, task):
        parts = task.split(':')
        complexity, name, prev_hash = parts
        complexity = int(complexity)
        counter = 0

        print('start mining')

        while True: 
            block = f"{complexity}:{name}:{prev_hash}:{self.miner_id}:{counter}"
            block_hash = self.get_sha256(block)

            if block_hash[:complexity] == '0' * complexity:
                print(f'block mined: {block_hash}')
                return block
            
            counter += 1

    def start_mining(self):
        print(f'miner {self.miner_id} started')

        while True:
            try:
                res = requests.get(f'{self.server_url}/future-block')
                task = res.text.strip()

                if not task:
                    print('no task')
                    break
                
                mined_block = self.mine_block(task)

                if mined_block:
                    print('send mined block to server')
                    post_data = {
                        'block': mined_block
                    }
                    res = requests.post(f'{self.server_url}/future-block', data=post_data)

                    if res.status_code == 200:
                        print('block sent to server')
                    else:
                        print(f'server rejected block: {res.status_code}')
            except Exception as e:
                print(f'error: {e}')
                break


if __name__ == "__main__":
    miner_id = f"miner_{random.randint(1000, 9999)}"

    miner = Miner(miner_id)
    miner.start_mining()
