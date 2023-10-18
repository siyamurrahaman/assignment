'''
Make a template using the dictionary data.
Your Template must have at least two sentences.
USD must be converted to BDT
example Output: Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT
'''
mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Russia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
            }
test = mobile_data.keys()
#print(test)
i = 0
while i <= 5:
    mobile_name = mobile_data['data'][i]['name']
    mobile_price = mobile_data['data'][i]['price']
    mobile_usd = float(mobile_price[:4])
    location_made = mobile_data['data'][i]['made']
    exchnage_rate = 110
    price = mobile_usd * exchnage_rate
    print(f'{mobile_name} is made in {location_made}. The price is {mobile_price} which is almost equal to {price} BDT')
    i+=1


#print(f'{mobile_name} is made in {location_made}. The price is {mobile_price} which is almost equal to {price} BDT')



