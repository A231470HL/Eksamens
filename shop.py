from cart import Cart  # Importējam Cart klasi
from product import ProductCollection  # Importējam ProductCollection klasi

class Shop:
    def __init__(self, products):
        self.products = products
        self.cart = Cart()  # Tagad Python zin Cart klasi
        self.categories = self.products.get_categories()
        self.categories.sort()

    def show_categories(self):
        print("\nPieejamās kategorijas:")
        for idx, category in enumerate(self.categories, start=1):
            print(f"{idx}. {category}")

    def display_products(self, products):
        print("\nPieejamās preces:")
        print(f"{'Prece':<20}{'Cena':<10}{'Izmērs':<20}{'Krāsa':<30}")
        print("-" * 80)
        for product in products:
            print(product.display_info())

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
                available_products = [p for p in self.products.products if p.is_available()]
                if available_products:
                    self.display_products(available_products)
                else:
                    print("Nav nevienas pieejamas preces.")

            elif choice == '2':
                self.cart.view()

            elif choice == '3':
                self.show_categories()  # Parādām kategorijas

                try:
                    cat_choice = int(input("Izvēlies kategoriju: "))
                    if 1 <= cat_choice <= len(self.categories):
                        selected_category = self.categories[cat_choice - 1]
                        filtered_products = self.products.filter_by_category(selected_category)

                        if filtered_products:
                            self.display_products(filtered_products)
                            self.handle_add_to_cart(filtered_products)
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
