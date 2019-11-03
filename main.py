from taxfree import TaxFree
from vinmonopolet import Vinmonopolet
import sqlite3
import datetime


def get_vm_product_price(tf_name, tf_barcode):
    for vm_product in vm.search(tf_name):
        vm_name = vm_product['basic']['productLongName']
        vm_barcodes = vm_product['logistics']['barcodes']
        if len(vm_product['prices']) >= 1:
            vm_price = vm_product['prices'][0]['salesPrice']
        else:
            return None, None

        for vm_barcode in vm_barcodes:
            if vm_barcode['gtin'] == tf_barcode:
                return vm_name, vm_price
    return None, None


def lookup_and_store_search(tf_search_result, tf_search_category, tf_search_sub_category):
    for tf_product in tf_search_result:
        tf_name = tf_product['name']
        tf_barcode = tf_product['ean']
        tf_price = tf_product['price']['value']
        vm_name, vm_price = get_vm_product_price(tf_name, tf_barcode)

        if vm_price is not None:
            diff_price = vm_price - tf_price
            perc_diff_price = (diff_price/vm_price)*100
        else:
            diff_price = None
            perc_diff_price = None

        print('Product name TaxFree: {}'.format(tf_name))
        print('Product price TaxFree: {}.00'.format(tf_price))
        print('Product name Vinmonopolet: {}'.format(vm_name))
        print('Product price Vinmonopolet: {}'.format(vm_price))

        print('')
        print('************************************')

        cursor.execute('''INSERT INTO products(timestamp, barcode, category, sub_category, tf_name, vm_name, tf_price, vm_price, diff_price, perc_diff_price)
                          VALUES(?,?,?,?,?,?,?,?,?,?)''', (datetime.datetime.now().isoformat(), tf_barcode, tf_search_category, tf_search_sub_category, tf_name, vm_name, tf_price, vm_price, diff_price, perc_diff_price))
        db.commit()


vm = Vinmonopolet()
tf = TaxFree()

db = sqlite3.connect('database')
cursor = db.cursor()


for vine_type in ['Rødvin', 'Hvitvin', 'Rosévin', 'Dessertvin', 'Musserende', 'Sterkvin', 'Perlende vin']:
    category = 'vin'
    tf_search = tf.search('', category, vine_type)
    lookup_and_store_search(tf_search, category, vine_type)

for fortified_vine_type in ['Aperitiff', 'Bitter', 'Eplebrennevin', 'Grappa', 'Tequila & Mezcal', 'Likør', 'Akevitt', 'Brandy', 'Cognac', 'Gin', 'Rom', 'Vodka', 'Armagnac', 'Whisky', 'Brennevin under 22%']:
    category = 'brennevin'
    tf_search = tf.search('', category, fortified_vine_type)
    lookup_and_store_search(tf_search, category, fortified_vine_type)

for beer_type in ['Lager og pils', 'Hveteøl', 'Ale', 'Belgisk stil', 'Stout og porter', 'Sider', 'Øvrige']:
    category = 'øl'
    tf_search = tf.search('', category, beer_type)
    lookup_and_store_search(tf_search, category, beer_type)

db.close()
