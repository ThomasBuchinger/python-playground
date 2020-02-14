from collections import defaultdict

filename = '../data/accounting.csv'
csv_seperator = "\t"
debug = True

# Setup stuff
# Reorganize data into Array of Dicts
with open(filename, 'r') as f:
  raw_data = []
  for line in f:
    cc, product, string_amount = line.split(csv_seperator)
    amount = float(string_amount.strip())
    raw_data.append( {'costcenter': cc.strip(), 'product': product.strip(), 'amount': amount} )
if debug:
  print(raw_data)

# Calc relevant sttistics
stats = dict()
for entry in raw_data:
  curr_amount = stats.get(entry['product'], 0)
  stats[entry['product']] = curr_amount + entry['amount']
if debug:
  print("Statistics: ", stats)

# Print the table
print('{:10} | {:10} | {:8}'.format('costcenter', 'product', 'amount'))
print("=" * 32)
for entry in raw_data:
    print('{:10} | {:10} | {:6.2f}'.format(entry['costcenter'], entry['product'], entry['amount']))
print("=" * 32)

# Print the sums
for key, value in stats.items():
  print('{:10}: {:6.2f}'.format(key, value))




