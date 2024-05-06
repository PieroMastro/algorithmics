import pickle

shoplist_file = 'shoplist.dat'

shoplist = [
    'apples',
    'oranges',
    'bananas'
]

with open(shoplist_file, 'wb') as file:
    pickle.dump(shoplist, file)
    
with open(shoplist_file, 'rb') as file:
    stored_list = pickle.load(file)
    
print(stored_list)