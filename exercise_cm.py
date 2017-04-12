import random, time, datetime

glob_bvg_corp_exch = [
    {'TEA': {'Type': 'Common', 'Last Dividend': 0, 'Fixed Dividend': None, 'Par Value': 100}},
    {'POP': {'Type': 'Common', 'Last Dividend': 8, 'Fixed Dividend': None, 'Par Value': 100}},
    {'ALE': {'Type': 'Common', 'Last Dividend': 23, 'Fixed Dividend': None, 'Par Value': 60}},
    {'GIN': {'Type': 'Preferred', 'Last Dividend': 8, 'Fixed Dividend': 0.02, 'Par Value': 100}},
    {'JOE': {'Type': 'Common', 'Last Dividend': 13, 'Fixed Dividend': None, 'Par Value': 250}}
]

selected_stock = random.choice(glob_bvg_corp_exch)

for stock in selected_stock:
    stock_name = stock
    stock_value = selected_stock[stock]

while True:
    input_price = raw_input('Please input a price for stock ' + stock_name + ': ')
    try:
        price = float(input_price)
    except ValueError:
        print '*Please input a numeric value*'
        continue
    if price <= 0:
        print '*Please input a positive value*'
        continue
    else:
        break

if stock_value['Type'] == 'Common':
    dividend_yield = stock_value['Last Dividend'] / price
elif stock_value['Type'] == 'Preferred':
    dividend_yield = stock_value['Fixed Dividend'] * stock_value['Par Value'] / price
print 'Dividend Yield = ', dividend_yield

if stock_value['Last Dividend'] == 0:
    p_e_ratio = 0
else:
    p_e_ratio = price / stock_value['Last Dividend']
print 'P/E Ratio = ', p_e_ratio

trade_type = ['buy', 'sell']
a_trade_record = {
        stock_name: {'time': datetime.datetime.now(), 'quantity': random.randrange(1, 20),
                     'action': random.choice(trade_type), 'traded_price': random.randrange(60, 100)}
    }
print 'a trade record:', a_trade_record

trade_minute = 15
trade_frequency = 60
trade_history = []
start_time = time.time()
while (time.time() - start_time) < trade_minute * 60:
    time.sleep(trade_frequency)
    trade = {
        stock_name: {'time': datetime.datetime.now(), 'quantity': random.randrange(1, 20),
                     'action': random.choice(trade_type), 'traded_price': random.randrange(60, 100)}
    }
    trade_history.append(trade)

total_quantity = 0
total_cost = 0
for item in trade_history:
    for key in item:
        item_value = item[key]
    total_quantity += item_value['quantity']
    total_cost += item_value['traded_price'] * item_value['quantity']

volume_weighted_stock_price = float(total_cost) / total_quantity
print 'Volume Weighted Stock Price = ', volume_weighted_stock_price

price_product = 1
for item in glob_bvg_corp_exch:
    for key in item:
        item_value = item[key]
    price_product *= item_value['Par Value']
geometric_mean = price_product ** (1./len(glob_bvg_corp_exch))
print 'Geometric Mean = ', geometric_mean
