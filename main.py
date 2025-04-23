# main.py faila saturs

from product import ProductCollection  # Importējam ProductCollection
from shop import Shop  # Importējam Shop

def main():
    # Izveidojam ProductCollection objektu
    products = ProductCollection()
    products.load_from_csv('products.csv')  # Ielādējam produktus no CSV faila

    # Izveidojam Shop objektu
    shop = Shop(products)

    # Sākam veikala darbību
    shop.run()

if __name__ == "__main__":
    main()
