class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Store:
    def __init__(self):
        self.products = [
            Product("Dators", 1000),
            Product("Tālrunis", 500),
            Product("Austiņas", 100)
        ]
        self.cart = []
    
    def show_products(self):
        print("Pieejamie produkti:")
        for idx, product in enumerate(self.products, start=1):
            print(f"{idx}. {product.name} - {product.price} EUR")
    
    def add_to_cart(self):
        while True:
            self.show_products()
            choice = input("Ievadiet produkta numuru vai 'q', lai izietu: ")
            
            if choice.lower() == 'q':
                break
            
            try:
                product_index = int(choice)
                if 1 <= product_index <= len(self.products):
                    self.cart.append(self.products[product_index - 1])
                    print(f"{self.products[product_index - 1].name} pievienots grozam.")
                else:
                    print("Nederīgs produkta numurs!")
            except ValueError:
                print("Lūdzu, ievadiet derīgu skaitli vai 'q', lai izietu.")
    
    def view_cart(self):
        if not self.cart:
            print("Grozs ir tukšs!")
        else:
            print("Jūsu grozs:")
            total = 0
            for product in self.cart:
                print(f"{product.name} - {product.price} EUR")
                total += product.price
            print(f"Kopējā summa: {total} EUR")
    
    def checkout(self):
        if not self.cart:
            print("Grozs ir tukšs! Neko nav iespējams iegādāties.")
        else:
            self.view_cart()
            print("Paldies par pirkumu!")
            self.cart = []

def main():
    store = Store()
    while True:
        print("\n1. Apskatīt produktus")
        print("2. Pievienot produktu grozam")
        print("3. Apskatīt grozu")
        print("4. Apmaksāt")
        print("5. Iziet")
        
        choice = input("Izvēlieties darbību: ")
        
        if choice == "1":
            store.show_products()
        elif choice == "2":
            store.add_to_cart()
        elif choice == "3":
            store.view_cart()
        elif choice == "4":
            store.checkout()
        elif choice == "5":
            print("Paldies! Uz redzēšanos!")
            break
        else:
            print("Nederīga izvēle, mēģiniet vēlreiz!")

if __name__ == "__main__":
    main()
