#!/bin/bash

echo "🪙 Bitcoin Mining Pool - Демонстрация curl команд"
echo "=============================================="
echo ""

echo "📋 1. Получение задания на майнинг (GET request):"
echo "curl https://your-site.repl.co/future-block"
echo ""

echo "🧪 Тестирование локально:"
curl http://localhost:8080/future-block
echo ""
echo ""

echo "📋 2. Отправка добытого блока (POST request):"
echo "curl -X POST -d 'block=4:Adams:0000000000000000000000000000000000000000000000000000000000000000:My:23882' https://your-site.repl.co/future-block"
echo ""

echo "🧪 Тестирование локально с валидным блоком:"
echo "Найдем валидный блок с 4 нулями..."

# Найдем простой валидный блок
python3 -c "
import hashlib
import sys

complexity = 4
name = 'Adams'
last_hash = '0000000000000000000000000000000000000000000000000000000000000000'
miner_id = 'test_miner'

for nonce in range(1, 1000000):
    block = f'{complexity}:{name}:{last_hash}:{miner_id}:{nonce}'
    block_hash = hashlib.sha256(block.encode('utf-8')).hexdigest()
    
    if block_hash.startswith('0' * complexity):
        print(f'Валидный блок найден:')
        print(f'Блок: {block}')
        print(f'Хеш: {block_hash}')
        print(f'')
        print(f'curl команда:')
        print(f'curl -X POST -d \"block={block}\" http://localhost:8080/future-block')
        break
else:
    print('Не удалось найти валидный блок')
"
