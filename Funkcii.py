foreign_sum = 1542.52
exchange_rate = 2.32

def convert_currency(rate, amount):
    return amount * rate
a = convert_currency(exchange_rate, foreign_sum)
print(a)
print()
costs = 1264.91
revenue = 2784.7

def calculate_roi(costs, revenue):
    roi = (revenue-costs)/costs
    return roi
print(round(calculate_roi(costs, revenue),2))
print()

total_costs = 2801.57
total_clicks = 705

def calculate_cpc(total_costs, total_clicks):
    return round(total_costs/total_clicks,2)
print(calculate_cpc(total_costs, total_clicks))
print()

total_visitors = 2729
buyers = 1579

def calculate_conversion(total_visitors, buyers):
    return round((buyers/total_visitors)*100,2)
print(calculate_conversion(total_visitors, buyers))