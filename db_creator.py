import sqlite3

db = sqlite3.connect('database')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE products(id INTEGER PRIMARY KEY, timestamp TEXT, barcode TEXT, category TEXT, sub_category TEXT, tf_name TEXT, vm_name TEXT,
                       tf_price REAL, vm_price REAL, diff_price REAL, perc_diff_price REAL)
''')
db.commit()
db.close()
