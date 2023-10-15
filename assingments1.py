# Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT

mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchange_rate': 107.25
}
for mobiles in mobile_data.get('data'):
    USD = float(mobiles.get('price').split()[0])
    BDT =  USD*  mobile_data.get('exchange_rate')
    print(f"{mobiles.get('name')} made in {mobiles.get('made')}. The price is {USD} USD which is almost equal to {BDT} BDT ")