class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Store:
    def __init__(self):
        self.products = [
            Product("Dators", 1000, "Elektronika"), Product("Tālrunis", 500, "Elektronika"), Product("Austiņas", 100, "Elektronika"),
            Product("Monitors", 250, "Elektronika"), Product("Tastatūra", 70, "Piederumi"), Product("Pele", 50, "Piederumi"),
            Product("Printeris", 200, "Elektronika"), Product("Mikrofons", 120, "Piederumi"), Product("Webkamera", 80, "Piederumi"),
            Product("USB zibatmiņa", 30, "Datu nesēji"), Product("Ārējais cietais disks", 150, "Datu nesēji"),
            Product("Planšetdators", 600, "Elektronika"), Product("Portatīvais lādētājs", 40, "Piederumi"),
            Product("Smartwatch", 300, "Elektronika"), Product("VR brilles", 400, "Elektronika"),
            Product("Datora korpuss", 180, "Komponentes"), Product("Operatīvā atmiņa (RAM)", 130, "Komponentes"),
            Product("Mātesplate", 250, "Komponentes"), Product("Procesors", 350, "Komponentes"),
            Product("Videokarte", 800, "Komponentes"), Product("Barošanas bloks", 100, "Komponentes"),
            Product("Dzesētājs", 60, "Komponentes"), Product("Tīkla maršrutētājs", 90, "Tīklošana"),
            Product("Bluetooth austiņas", 150, "Elektronika"), Product("Spēļu kontrolieris", 200, "Piederumi"),
            Product("Datora skaļruņi", 120, "Elektronika"), Product("HDMI kabelis", 25, "Piederumi"),
            Product("Ethernet kabelis", 20, "Tīklošana"), Product("SD karte", 35, "Datu nesēji"),
            Product("Kārtridžs printerim", 50, "Piederumi")
        ]
        self.cart = []

    # Funkcija, kas izdrukā tekstu zaļā krāsā
    def print_green(self, message):
        return f"\033[32m{message}\033[0m"

    # Funkcija, kas izdrukā tekstu dzeltenā krāsā
    def print_yellow(self, message):
        return f"\033[33m{message}\033[0m"

    # Funkcija, kas izdrukā tekstu sarkanā krāsā
    def print_red(self, message):
        return f"\033[31m{message}\033[0m"

    # Parāda produktus
    def show_products(self, category=None):
        if category:
            filtered_products = [p for p in self.products if p.category == category]
            for idx, product in enumerate(filtered_products, start=1):
                print(f"{self.print_yellow(f'{idx}. {product.name}')} - {self.print_green(f'{product.price:.2f} EUR')}")
            return filtered_products

        categories = list(set(product.category for product in self.products))
        print(self.print_green("Pieejamās kategorijas:"))
        for idx, category in enumerate(categories, start=1):
            print(f"{self.print_yellow(f'{idx}. {category}')}")

        choice = input(self.print_yellow("Izvēlieties kategorijas numuru vai 'q', lai izietu: ")).strip()
        if choice.lower() == 'q':
            return None

        if choice.isdigit():
            category_index = int(choice)
            if 1 <= category_index <= len(categories):
                selected_category = categories[category_index - 1]
                print(self.print_green(f"\nProdukti kategorijā: {selected_category}"))
                return self.show_products(selected_category)
            else:
                print(self.print_red("Nederīgs kategorijas numurs!"))
        else:
            print(self.print_red("Lūdzu, ievadiet derīgu skaitli vai 'q', lai izietu."))
        return None

    # Pievieno produktus grozam
    def add_to_cart(self):
        while True:
            selected_products = self.show_products()
            if not selected_products:
                return

            choice = input(self.print_yellow("Ievadiet produkta numuru vai 'q', lai izietu: ")).strip()

            if choice.lower() == 'q':
                break

            if choice.isdigit():
                product_index = int(choice)
                if 1 <= product_index <= len(selected_products):
                    self.cart.append(selected_products[product_index - 1])
                    print(self.print_green(f"{selected_products[product_index - 1].name} pievienots grozam."))
                else:
                    print(self.print_red("Nederīgs produkta numurs!"))
            else:
                print(self.print_red("Lūdzu, ievadiet derīgu skaitli vai 'q', lai izietu."))

    # Apskatīt grozu
    def view_cart(self):
        if not self.cart:
            print(self.print_red("Jūsu grozs ir tukšs!"))
        else:
            print(self.print_green("\nJūsu grozs:"))
            total = 0
            for product in self.cart:
                print(f"{self.print_yellow(f'{product.name}')} - {self.print_green(f'{product.price:.2f} EUR')}")
                total += product.price
            print(f"Kopējā summa: {self.print_green(f'{total:.2f} EUR')}")

    # Apmaksāt
    def checkout(self):
        if not self.cart:
            print(self.print_red("Jūsu grozs ir tukšs! Nekas netika iegādāts."))
        else:
            self.view_cart()
            print(self.print_green("Paldies par pirkumu!"))
            self.cart = []

def main():
    store = Store()
    while True:
        print(store.print_green("\n1. Apskatīt produktus"))
        print(store.print_green("2. Pievienot produktu grozam"))
        print(store.print_green("3. Apskatīt grozu"))
        print(store.print_green("4. Apmaksāt"))
        print(store.print_green("5. Iziet"))

        choice = input(store.print_yellow("Izvēlieties darbību: ")).strip()

        if choice == "1":
            store.show_products()
        elif choice == "2":
            store.add_to_cart()
        elif choice == "3":
            store.view_cart()
        elif choice == "4":
            store.checkout()
        elif choice == "5":
            print(store.print_green("Paldies! Uz redzēšanos!"))
            break
        else:
            print(store.print_red("Nederīga izvēle, mēģiniet vēlreiz!"))

if __name__ == "__main__":
    main()
