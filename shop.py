# shop.py faila saturs

from cart import Cart  # Importējam Cart klasi no cart.py
from product import ProductCollection  # Importējam ProductCollection klasi no products.py

class Shop:
    def __init__(self, products):
        self.products = products
        self.cart = Cart()  # Izveidojam Cart objektu
        self.categories = self.products.get_categories()
        self.categories.sort()

    def run(self):
        while True:
            print("\n--- Mūsu veikals ---")
            print("1. Apskatīt visas pieejamās preces")
            print("2. Apskatīt grozu")
            print("3. Pievienot preci grozam pēc kategorijas")
            print("4. Noņemt preci no groza")
            print("5. Veikt pirkumu")
            print("6. Iziet")

            choice = input("\nIzvēlies darbību (1-6): ").strip()

            if choice == '1':
                # Apskatīt visas preces, kuras ir pieejamas
                available_products = [p for p in self.products.products if p.is_available()]
                if available_products:
                    self.display_products(available_products)
                else:
                    print("Nav nevienas pieejamas preces.")

            elif choice == '2':
                self.cart.view()

            elif choice == '3':
                # Parādīt kategorijas
                self.show_categories()

                try:
                    cat_choice = int(input("Izvēlies kategoriju: "))
                    if 1 <= cat_choice <= len(self.categories):
                        selected = self.categories[cat_choice - 1]
                        filtered = self.products.filter_by_category(selected)

                        if filtered:
                            self.display_products(filtered)
                            self.handle_add_to_cart(filtered)
                        else:
                            print("Šajā kategorijā nav pieejamu preču.")
                    else:
                        print("Nepareiza izvēle!")
                except ValueError:
                    print("Lūdzu, ievadi skaitli!")

            elif choice == '4':
                self.handle_remove_from_cart()

            elif choice == '5':
                self.cart.checkout()
                break

            elif choice == '6':
                print("Paldies, ka apmeklējāt mūsu veikalu!")
                break

            else:
                print("Nepareiza izvēle! Lūdzu, izvēlies no 1 līdz 6.")

    def display_products(self, products):
        print(f"\n{'Prece':<20}{'Cena':<10}{'Izmērs':<20}{'Krāsa':<30}")
        print("-" * 80)
        for product in products:
            print(product.display_info())

    def handle_add_to_cart(self, products):
        try:
            prod_choice = int(input("Izvēlies preci, kuru pievienot grozam (norādi skaitli): ")) - 1
            if 0 <= prod_choice < len(products):
                selected_product = products[prod_choice]
                size = input(f"Izvēlies izmēru ({', '.join(selected_product.sizes.keys())}): ").strip()
                color = input(f"Izvēlies krāsu ({', '.join(selected_product.colors)}): ").strip()

                # Pievienojam preci grozam
                self.cart.add_item(CartItem(selected_product, size, color))
                print(f"Prece '{selected_product.name}' pievienota grozam.")
            else:
                print("Nepareiza izvēle!")
        except ValueError:
            print("Lūdzu, ievadi skaitli!")

    def handle_remove_from_cart(self):
        self.cart.view()
        try:
            item_to_remove = int(input("Norādi numuru, lai noņemtu preci no groza: ")) - 1
            self.cart.remove_item(item_to_remove)
            print("Prece noņemta no groza.")
        except ValueError:
            print("Nepareiza izvēle!")
    
    def show_categories(self):
        print("\nPieejamās kategorijas:")
        for idx, category in enumerate(self.categories, start=1):
            print(f"{idx}. {category}")

class CartItem:
    def __init__(self, product, size, color):
        self.name = product.name
        self.price = product.price
        self.size = size
        self.color = color

    def display_info(self):
        return f"{self.name:<20}{self.size:<10}{self.color:<15}{self.price:<10.2f}"
