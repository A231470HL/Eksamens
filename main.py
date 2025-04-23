from shop import Shop
from product import ProductCollection

def main():
    products = ProductCollection()
    products.load_from_csv('products.csv')  # Ielādējam CSV
    shop = Shop(products)  # Dodam Shop klasei pareizu objektu
    shop.run()  # Sākam visu

if __name__ == "__main__":
    main()
