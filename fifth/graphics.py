import math 
import csv 
import matplotlib.pyplot as plt
import pandas as pd
import requests

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)


def get_close_trade_day(data):
    close_trade_day = []
    for el in data[1:]:
        close_trade_day.append(int(el[-1]))
    return close_trade_day

# 4.2
def graphcic_close_trade_day(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data)
    plt.title('График цен закрытия')
    plt.xlabel('Временной период')
    plt.ylabel('Цена закрытия')
    plt.grid(True, alpha=0.3)
    plt.show()


# 4.3
def graphcic_moving_average(data, window=3):
    moving_avg = []
    for i in range(len(data)):
        if i < window - 1:
            moving_avg.append(None)
        else:
            window_data = data[i - window + 1:i + 1]
            avg = sum(window_data) / window
            moving_avg.append(avg)
    
    plt.figure(figsize=(12, 6))
    # plt.plot(data, label='Цены закрытия', alpha=0.7)
    plt.plot(moving_avg, label=f'Скользящее среднее (окно={window})', linewidth=2)
    plt.title('График скользящего среднего')
    plt.xlabel('Временной период')
    plt.ylabel('Цена')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

    return moving_avg

# 4.4
def graphcic_weighted_moving_average(data, window=3):
    weighted_moving_avg = []
    for i in range(len(data)):
        if i < window - 1:
            weighted_moving_avg.append(None)
        else:
            window_data = data[i - window + 1:i + 1]
            weights = list(range(1, window + 1))
            total_weight = sum(weights)
            weighted_sum = sum(price * weight for price, weight in zip(window_data, weights))
            print(weighted_sum, total_weight)
            wma = weighted_sum / total_weight
            weighted_moving_avg.append(wma)
    
    plt.figure(figsize=(12, 6))
    # plt.plot(data, label='Цены закрытия', alpha=0.7)
    plt.plot(weighted_moving_avg, label=f'Взвешенное СС (окно={window})', linewidth=2)
    plt.title('График взвешенного скользящего среднего')
    plt.xlabel('Временной период')
    plt.ylabel('Цена')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

    return weighted_moving_avg


# 5
def find_ma_crossovers(data, ma, wma, window=3):
    
    crossovers = []
    for i in range(window, len(data)):
        if ma[i] is not None and wma[i] is not None:
            if (ma[i-1] < wma[i-1] and ma[i] > wma[i]):
                el = {'type': 'BUY', 'index': i, 'price': data[i], 'ma': ma[i], 'wma': wma[i]}
                print(el)
                crossovers.append(el)
            elif (ma[i-1] > wma[i-1] and ma[i] < wma[i]):
                el = {'type': 'SELL', 'index': i, 'price': data[i], 'ma': ma[i], 'wma': wma[i]}
                print(el)
                crossovers.append(el)
    
    return crossovers


def get_btc_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    data = response.json()
    return data['bitcoin']['usd']


# треееейд
def trading_strategy(crossovers, sum_btc, sum_usd):
    trades = []
    course = get_btc_price()
    
    for crossover in crossovers:
        if crossover['type'] == 'BUY' and sum_usd > 0:
            sum_btc += sum_usd / course
            sum_usd = 0
            trades.append(('BUY', crossover['index'], crossover['price'], sum_btc, sum_usd))
        elif crossover['type'] == 'SELL' and sum_btc > 0:
            sum_usd += sum_btc * course
            sum_btc = 0
            trades.append(('SELL', crossover['index'], crossover['price'], sum_btc, sum_usd))
    
    print(sum_btc, sum_usd, len(trades))
    


if __name__ == "__main__":
    data = read_csv('BTC_data.csv')
    close_trade_day = get_close_trade_day(data)
    graphcic_close_trade_day(close_trade_day)
    ma = graphcic_moving_average(close_trade_day)
    wma = graphcic_weighted_moving_average(close_trade_day)

    crossovers = find_ma_crossovers(close_trade_day, ma, wma)

    trading_strategy(crossovers, 10.0, 0.0)

