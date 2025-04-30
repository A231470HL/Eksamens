from colorama import Fore, Style  # Importējam krāsu bibliotēku
from cart import Cart  # Importējam Cart klasi no cart.py
from product import ProductCollection  # Importējam ProductCollection klasi no products.py

class Shop:
    def __init__(self, products):
        self.products = products
        self.cart = Cart()  # Izveidojam Cart objektu
        self.categories = self.products.get_categories()
        self.categories.sort()

        # Kategoriju-krāsu kartējums
        self.category_colors = {
            "Apģērbi": Fore.CYAN,
            "Apavi": Fore.GREEN,
            "Aksesuāri": Fore.MAGENTA,
            "Elektronika": Fore.YELLOW,
            "Cits": Fore.WHITE,
        }

    def run(self):
        while True:
            print(Fore.CYAN + "\n--- Mūsu veikals ---" + Style.RESET_ALL)
            print(Fore.YELLOW + "1. Apskatīt visas pieejamās preces" + Style.RESET_ALL)
            print(Fore.BLUE + "2. Apskatīt grozu" + Style.RESET_ALL)
            print(Fore.RED + "3. Pievienot preci grozam pēc kategorijas" + Style.RESET_ALL)
            print(Fore.BLUE + "4. Noņemt preci no groza" + Style.RESET_ALL)
            print(Fore.CYAN + "5. Veikt pirkumu" + Style.RESET_ALL)
            print(Fore.GREEN + "6. Iziet" + Style.RESET_ALL)

            choice = input(Fore.GREEN + "\nIzvēlies darbību (1-6): " + Style.RESET_ALL).strip()

            if choice == '1':
                available_products = [p for p in self.products.products if p.is_available()]
                if available_products:
                    self.display_products(available_products)
                else:
                    print(Fore.RED + "Nav nevienas pieejamas preces." + Style.RESET_ALL)

            elif choice == '2':
                self.cart.view()

            elif choice == '3':
                self.show_categories()

                try:
                    cat_choice = int(input(Fore.YELLOW + "Izvēlies kategoriju: " + Style.RESET_ALL))
                    if 1 <= cat_choice <= len(self.categories):
                        selected = self.categories[cat_choice - 1]
                        filtered = self.products.filter_by_category(selected)

                        if filtered:
                            self.display_products(filtered)
                            self.handle_add_to_cart(filtered)
                        else:
                            print(Fore.RED + "Šajā kategorijā nav pieejamu preču." + Style.RESET_ALL)
                    else:
                        print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + "Lūdzu, ievadi skaitli!" + Style.RESET_ALL)

            elif choice == '4':
                self.handle_remove_from_cart()

            elif choice == '5':
                self.cart.checkout()
                break

            elif choice == '6':
                print(Fore.MAGENTA + "Paldies, ka apmeklējāt mūsu veikalu!" + Style.RESET_ALL)
                break

            else:
                print(Fore.RED + "Nepareiza izvēle! Lūdzu, izvēlies no 1 līdz 6." + Style.RESET_ALL)

    def display_products(self, products):
        print(Fore.CYAN + f"\n{'Prece':<20}{'Cena':<10}{'Izmērs':<20}{'Krāsa':<30}" + Style.RESET_ALL)
        print(Fore.YELLOW + "-" * 80 + Style.RESET_ALL)
        for product in products:
            category = getattr(product, 'category', None).strip()  # Noņemam liekās baltās vietas
            color_code = self.category_colors.get(category, Style.RESET_ALL)  # Default krāsa
            line = product.display_info()
            print(f"{color_code}{line}{Style.RESET_ALL}")  # Pievienojam krāsu ar colorama

    def handle_add_to_cart(self, products):
        try:
            prod_choice = int(input(Fore.GREEN + "Izvēlies preci, kuru pievienot grozam (norādi skaitli): " + Style.RESET_ALL)) - 1
            if 0 <= prod_choice < len(products):
                selected_product = products[prod_choice]
                size = input(Fore.YELLOW + f"Izvēlies izmēru ({', '.join(selected_product.sizes.keys())}): " + Style.RESET_ALL).strip()
                color = input(Fore.YELLOW + f"Izvēlies krāsu ({', '.join(selected_product.colors)}): " + Style.RESET_ALL).strip()

                self.cart.add_item(CartItem(selected_product, size, color))
                print(Fore.GREEN + f"Prece '{selected_product.name}' pievienota grozam." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Lūdzu, ievadi skaitli!" + Style.RESET_ALL)

    def handle_remove_from_cart(self):
        self.cart.view()
        try:
            item_to_remove = int(input(Fore.YELLOW + "Norādi numuru, lai noņemtu preci no groza: " + Style.RESET_ALL)) - 1
            self.cart.remove_item(item_to_remove)
            print(Fore.GREEN + "Prece noņemta no groza." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)

    def show_categories(self):
        print(Fore.CYAN + "\nPieejamās kategorijas:" + Style.RESET_ALL)
        for idx, category in enumerate(self.categories, start=1):
            color_code = self.category_colors.get(category, Style.RESET_ALL)
            print(f"{color_code}{idx}. {category}{Style.RESET_ALL}")
        print(Fore.YELLOW + "Izvēlies kategoriju, ievadot tās numuru." + Style.RESET_ALL)

class CartItem:
    def __init__(self, product, size, color):
        self.name = product.name
        self.price = product.price
        self.size = size
        self.color = color

    def display_info(self):
        return f"{self.name:<20}{self.price:<10.2f}{self.size:<20}{self.color:<30}"