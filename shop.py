from colorama import Fore, Style  # Importējam krāsu bibliotēku
from cart import Cart  # Importējam Cart klasi no cart.py
from product import ProductCollection  # Importējam ProductCollection klasi no products.py
import os

class Shop:
    def __init__(self, products):
        self.products = products
        self.cart = Cart()  # Izveidojam Cart objektu
        self.categories = self.products.get_categories()
        self.categories.sort()
        
        # Piegādes opcijas
        self.shipping_options = {
            "Standarta piegāde": 2.99,
            "Ātrā piegāde": 5.99,
            "Bezmaksas piegāde": 0.00
        }
        self.selected_shipping = "Standarta piegāde"  # Noklusētā piegāde
        
        # Atlaižu opcijas
        self.discount_types = {
            "Bez atlaides": 0,
            "Jaunā klienta atlaide": 10,  # 10% atlaide
            "Lojalitātes atlaide": 15,    # 15% atlaide
            "Akcijas atlaide": 20         # 20% atlaide
        }
        self.selected_discount = "Bez atlaides"  # Noklusētā atlaide

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
        # Clear the screen at the start of the loop
            os.system('cls' if os.name == 'nt' else 'clear')

            print(Fore.WHITE + "\n--- Mūsu veikals ---" + Style.RESET_ALL)
            print(Fore.RED + "1. Apskatīt visas pieejamās preces" + Style.RESET_ALL)
            print(Fore.WHITE + "2. Apskatīt grozu" + Style.RESET_ALL)
            print(Fore.RED + "3. Pievienot preci grozam pēc kategorijas" + Style.RESET_ALL)
            print(Fore.WHITE + "4. Noņemt preci no groza" + Style.RESET_ALL)
            print(Fore.RED + "5. Filtrēt preces" + Style.RESET_ALL)  # Jauna opcija
            print(Fore.WHITE + "6. Piegādes un atlaižu iestatījumi" + Style.RESET_ALL)  # Jauna opcija
            print(Fore.RED + "7. Veikt pirkumu" + Style.RESET_ALL)
            print(Fore.WHITE + "8. Iziet" + Style.RESET_ALL)

            choice = input(Fore.RED + "\nIzvēlies darbību (1-8): " + Style.RESET_ALL).strip()

            if choice == '1':
                available_products = [p for p in self.products.products if p.is_available()]
                if available_products:
                    self.display_products(available_products)
                else:
                    print(Fore.RED + "Nav nevienas pieejamas preces." + Style.RESET_ALL)
                input(Fore.WHITE + "\nNospied Enter, lai turpinātu..." + Style.RESET_ALL)

            elif choice == '2':
                self.cart.view()
                # Parādām papildu aprēķinus
                self.display_cart_summary()
                input(Fore.RED + "\nNospied Enter, lai turpinātu..." + Style.RESET_ALL)

            elif choice == '3':
                self.show_categories()

                try:
                    cat_choice = int(input(Fore.WHITE + "Izvēlies kategoriju: " + Style.RESET_ALL))
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
                input(Fore.RED + "\nNospied Enter, lai turpinātu..." + Style.RESET_ALL)

            elif choice == '4':
                self.handle_remove_from_cart()
                input(Fore.RED + "\nNospied Enter, lai turpinātu..." + Style.RESET_ALL)

            elif choice == '5':
                self.filter_products()
                input(Fore.RED + "\nNospied Enter, lai turpinātu..." + Style.RESET_ALL)

            elif choice == '6':
                self.configure_shipping_and_discounts()
                input(Fore.RED + "\nNospied Enter, lai turpinātu..." + Style.RESET_ALL)

            elif choice == '7':
                self.cart.view()
                self.display_cart_summary()
                confirm = input(Fore.RED + "\nVai vēlies pabeigt pirkumu? (j/n): " + Style.RESET_ALL).lower()
                if confirm == 'j':
                    self.cart.checkout()
                    input(Fore.RED + "\nNospied Enter, lai turpinātu..." + Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED + "Pirkums atcelts." + Style.RESET_ALL)

            elif choice == '8':
                print(Fore.RED + "Paldies, ka apmeklējāt mūsu veikalu!" + Style.RESET_ALL)
                break

            else:
                print(Fore.RED + "Nepareiza izvēle! Lūdzu, izvēlies no 1 līdz 8." + Style.RESET_ALL)
                input(Fore.RED + "\nNospied Enter, lai turpinātu..." + Style.RESET_ALL)

        # Clear the screen after completing the action
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def filter_products(self):
        """Jauna funkcija preču filtrēšanai"""
        print(Fore.RED + "\n--- Preču filtrēšana ---" + Style.RESET_ALL)
        print(Fore.WHITE + "1. Filtrēt pēc cenas" + Style.RESET_ALL)
        print(Fore.RED + "2. Filtrēt pēc pieejamiem izmēriem" + Style.RESET_ALL)
        print(Fore.WHITE + "3. Filtrēt pēc krāsas" + Style.RESET_ALL)
        print(Fore.RED + "4. Atgriezties galvenajā izvēlnē" + Style.RESET_ALL)
        
        filter_choice = input(Fore.WHITE + "\nIzvēlies filtrēšanas veidu (1-4): " + Style.RESET_ALL).strip()
        
        if filter_choice == '1':
            self.filter_by_price()
        elif filter_choice == '2':
            self.filter_by_size()
        elif filter_choice == '3':
            self.filter_by_color()
        elif filter_choice == '4':
            return
        else:
            print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)
    
    def filter_by_price(self):
        """Filtrēšana pēc cenas"""
        try:
            min_price = float(input(Fore.WHITE + "Ievadi minimālo cenu (€): " + Style.RESET_ALL))
            max_price = float(input(Fore.RED + "Ievadi maksimālo cenu (€): " + Style.RESET_ALL))
            
            filtered_products = [p for p in self.products.products 
                                if p.is_available() and min_price <= p.price <= max_price]
            
            if filtered_products:
                print(Fore.WHITE + f"\nPreces cenu diapazonā no {min_price}€ līdz {max_price}€:" + Style.RESET_ALL)
                self.display_products(filtered_products)
                
                # Piedāvājam iespēju pievienot kādu no atlasītajām precēm grozam
                add_to_cart = input(Fore.RED + "\nVai vēlies pievienot kādu no šīm precēm grozam? (j/n): " + Style.RESET_ALL).lower()
                if add_to_cart == 'j':
                    self.handle_add_to_cart(filtered_products)
            else:
                print(Fore.RED + "Nav atrasta neviena prece šajā cenu diapazonā." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Lūdzu, ievadi korektu cenas vērtību!" + Style.RESET_ALL)
    
    def filter_by_size(self):
        """Filtrēšana pēc izmēra"""
        available_sizes = set()
        for product in self.products.products:
            for size, qty in product.sizes.items():
                if qty > 0:
                    available_sizes.add(size)
        
        if not available_sizes:
            print(Fore.RED + "Nav pieejams neviens izmērs." + Style.RESET_ALL)
            return
        
        print(Fore.WHITE + "\nPieejamie izmēri:" + Style.RESET_ALL)
        sizes_list = sorted(list(available_sizes))
        for idx, size in enumerate(sizes_list, start=1):
            print(Fore.RED + f"{idx}. {size}" + Style.RESET_ALL)
        
        try:
            size_choice = int(input(Fore.WHITE + "\nIzvēlies izmēru (ievadi numuru): " + Style.RESET_ALL))
            if 1 <= size_choice <= len(sizes_list):
                selected_size = sizes_list[size_choice - 1]
                
                filtered_products = [p for p in self.products.products 
                                    if p.is_available() and selected_size in p.sizes and p.sizes[selected_size] > 0]
                
                if filtered_products:
                    print(Fore.RED + f"\nPreces ar izmēru {selected_size}:" + Style.RESET_ALL)
                    self.display_products(filtered_products)
                    
                    add_to_cart = input(Fore.WHITE + "\nVai vēlies pievienot kādu no šīm precēm grozam? (j/n): " + Style.RESET_ALL).lower()
                    if add_to_cart == 'j':
                        self.handle_add_to_cart(filtered_products)
                else:
                    print(Fore.RED + f"Nav atrasta neviena prece ar izmēru {selected_size}." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Lūdzu, ievadi skaitli!" + Style.RESET_ALL)
    
    def filter_by_color(self):
        """Filtrēšana pēc krāsas"""
        available_colors = set()
        for product in self.products.products:
            if product.is_available():
                for color in product.colors:
                    available_colors.add(color.strip())
        
        if not available_colors:
            print(Fore.RED + "Nav pieejama neviena krāsa." + Style.RESET_ALL)
            return
        
        print(Fore.WHITE + "\nPieejamās krāsas:" + Style.RESET_ALL)
        colors_list = sorted(list(available_colors))
        for idx, color in enumerate(colors_list, start=1):
            print(Fore.RED + f"{idx}. {color}" + Style.RESET_ALL)
        
        try:
            color_choice = int(input(Fore.WHITE + "\nIzvēlies krāsu (ievadi numuru): " + Style.RESET_ALL))
            if 1 <= color_choice <= len(colors_list):
                selected_color = colors_list[color_choice - 1]
                
                filtered_products = [p for p in self.products.products 
                                    if p.is_available() and any(selected_color.lower() in c.lower() for c in p.colors)]
                
                if filtered_products:
                    print(Fore.RED + f"\nPreces ar krāsu {selected_color}:" + Style.RESET_ALL)
                    self.display_products(filtered_products)
                    
                    add_to_cart = input(Fore.WHITE + "\nVai vēlies pievienot kādu no šīm precēm grozam? (j/n): " + Style.RESET_ALL).lower()
                    if add_to_cart == 'j':
                        self.handle_add_to_cart(filtered_products)
                else:
                    print(Fore.RED + f"Nav atrasta neviena prece ar krāsu {selected_color}." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Lūdzu, ievadi skaitli!" + Style.RESET_ALL)
    
    def configure_shipping_and_discounts(self):
        """Jauna funkcija piegādes un atlaižu konfigurēšanai"""
        print(Fore.RED + "\n--- Piegādes un atlaižu iestatījumi ---" + Style.RESET_ALL)
        print(Fore.WHITE + "1. Izvēlēties piegādes veidu" + Style.RESET_ALL)
        print(Fore.RED + "2. Piemērot atlaidi" + Style.RESET_ALL)
        print(Fore.WHITE + "3. Atgriezties galvenajā izvēlnē" + Style.RESET_ALL)
        
        config_choice = input(Fore.RED + "\nIzvēlies opciju (1-3): " + Style.RESET_ALL).strip()
        
        if config_choice == '1':
            self.select_shipping()
        elif config_choice == '2':
            self.select_discount()
        elif config_choice == '3':
            return
        else:
            print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)
    
    def select_shipping(self):
        """Piegādes veida izvēle"""
        print(Fore.WHITE + "\nPieejamie piegādes veidi:" + Style.RESET_ALL)
        shipping_options = list(self.shipping_options.items())
        for idx, (option, price) in enumerate(shipping_options, start=1):
            print(Fore.RED + f"{idx}. {option}: {price}€" + Style.RESET_ALL)
        
        try:
            shipping_choice = int(input(Fore.WHITE + "\nIzvēlies piegādes veidu (ievadi numuru): " + Style.RESET_ALL))
            if 1 <= shipping_choice <= len(shipping_options):
                self.selected_shipping = shipping_options[shipping_choice - 1][0]
                print(Fore.RED + f"Izvēlēts piegādes veids: {self.selected_shipping} ({self.shipping_options[self.selected_shipping]}€)" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Lūdzu, ievadi skaitli!" + Style.RESET_ALL)
    
    def select_discount(self):
        """Atlaides izvēle"""
        print(Fore.WHITE + "\nPieejamās atlaides:" + Style.RESET_ALL)
        discount_options = list(self.discount_types.items())
        for idx, (option, percentage) in enumerate(discount_options, start=1):
            print(Fore.RED + f"{idx}. {option}: {percentage}%" + Style.RESET_ALL)
        
        try:
            discount_choice = int(input(Fore.WHITE + "\nIzvēlies atlaidi (ievadi numuru): " + Style.RESET_ALL))
            if 1 <= discount_choice <= len(discount_options):
                self.selected_discount = discount_options[discount_choice - 1][0]
                print(Fore.RED + f"Izvēlēta atlaide: {self.selected_discount} ({self.discount_types[self.selected_discount]}%)" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Lūdzu, ievadi skaitli!" + Style.RESET_ALL)
    
    def display_cart_summary(self):
        """Parāda papildu aprēķinus par grozu"""
        if self.cart.is_empty():
            return
        
        # Aprēķināt kopējo summu bez atlaides
        subtotal = sum(item.price for item in self.cart.items)
        
        # Aprēķināt atlaidi
        discount_percentage = self.discount_types[self.selected_discount]
        discount_amount = subtotal * (discount_percentage / 100)
        
        # Pievienot piegādes izmaksas
        shipping_cost = self.shipping_options[self.selected_shipping]
        
        # Aprēķināt kopējo summu ar atlaidi un piegādi
        total = subtotal - discount_amount + shipping_cost
        
        # Parādīt kopējo preču skaitu grozā
        items_count = len(self.cart.items)
        
        print(Fore.CYAN + "\n----- Groza kopsavilkums -----" + Style.RESET_ALL)
        print(Fore.WHITE + f"Preču skaits grozā: {items_count}" + Style.RESET_ALL)
        print(Fore.RED + f"Kopējā summa (bez atlaides): {subtotal:.2f}€" + Style.RESET_ALL)
        
        if discount_percentage > 0:
            print(Fore.WHITE + f"Atlaide ({discount_percentage}%): -{discount_amount:.2f}€" + Style.RESET_ALL)
        
        print(Fore.RED + f"Piegāde ({self.selected_shipping}): {shipping_cost:.2f}€" + Style.RESET_ALL)
        print(Fore.CYAN + f"KOPĀ APMAKSAI: {total:.2f}€" + Style.RESET_ALL)
        
        # Papildu aprēķins - vidējā preces cena grozā
        if items_count > 0:
            average_price = subtotal / items_count
            print(Fore.WHITE + f"Vidējā preces cena grozā: {average_price:.2f}€" + Style.RESET_ALL)
    
    def display_products(self, products):
        print(Fore.RED + f"\n{'Prece':<20}{'Cena':<10}{'Izmērs':<20}{'Krāsa':<30}" + Style.RESET_ALL)
        print(Fore.RED + "-" * 80 + Style.RESET_ALL)
        for idx, product in enumerate(products, start=1):
            category = getattr(product, 'category', None).strip()  # Noņemam liekās baltās vietas
            color_code = self.category_colors.get(category, Style.RESET_ALL)  # Default krāsa
            line = product.display_info()
            print(f"{color_code}{idx}. {line}{Style.RESET_ALL}")  # Pievienojam numuru un krāsu ar colorama

    def handle_add_to_cart(self, products):
        try:
            prod_choice = int(input(Fore.RED + "Izvēlies preci, kuru pievienot grozam (norādi skaitli): " + Style.RESET_ALL))
            if 1 <= prod_choice <= len(products):
                selected_product = products[prod_choice - 1]
                
                # Parādām pieejamos izmērus ar atlikušo daudzumu
                available_sizes = {size: qty for size, qty in selected_product.sizes.items() if qty > 0}
                print(Fore.WHITE + "\nPieejamie izmēri:" + Style.RESET_ALL)
                for size, qty in available_sizes.items():
                    print(Fore.RED + f"{size} (pieejami: {qty})" + Style.RESET_ALL)
                
                size = input(Fore.RED + f"Izvēlies izmēru: " + Style.RESET_ALL).strip()
                
                # Pārbaudām vai izvēlētais izmērs eksistē un ir pieejams
                if size in available_sizes and available_sizes[size] > 0:
                    # Parādam pieejamās krāsas
                    print(Fore.WHITE + f"\nPieejamās krāsas: {', '.join(selected_product.colors)}" + Style.RESET_ALL)
                    color = input(Fore.RED + f"Izvēlies krāsu: " + Style.RESET_ALL).strip()
                    
                    # Pārbaudam vai izvēlētā krāsa ir pieejama
                    if any(color.lower() == c.lower().strip() for c in selected_product.colors):
                        # Pievienojam izvēlēto preci grozam
                        self.cart.add_item(CartItem(selected_product, size, color))
                        
                        # Samazinām pieejamo daudzumu
                        selected_product.reduce_stock(size)
                        
                        print(Fore.GREEN + f"Prece '{selected_product.name}' pievienota grozam." + Style.RESET_ALL)
                    else:
                        print(Fore.RED + f"Krāsa '{color}' nav pieejama!" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"Izmērs '{size}' nav pieejams!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Lūdzu, ievadi skaitli!" + Style.RESET_ALL)

    def handle_remove_from_cart(self):
        """Uzlabota funkcija preces noņemšanai no groza"""
        if self.cart.is_empty():
            print(Fore.RED + "Grozs ir tukšs!" + Style.RESET_ALL)
            return
            
        self.cart.view()
        
        print(Fore.WHITE + "\nKo vēlies darīt?" + Style.RESET_ALL)
        print(Fore.RED + "1. Noņemt vienu preci" + Style.RESET_ALL)
        print(Fore.WHITE + "2. Noņemt vairākas preces" + Style.RESET_ALL)
        print(Fore.RED + "3. Iztukšot visu grozu" + Style.RESET_ALL)
        print(Fore.WHITE + "4. Atgriezties galvenajā izvēlnē" + Style.RESET_ALL)
        
        remove_choice = input(Fore.RED + "\nIzvēlies darbību (1-4): " + Style.RESET_ALL).strip()
        
        if remove_choice == '1':
            try:
                item_to_remove = int(input(Fore.WHITE + "Norādi numuru, lai noņemtu preci no groza: " + Style.RESET_ALL)) - 1
                removed_item = self.cart.remove_item(item_to_remove)
                if removed_item:
                    print(Fore.RED + f"Prece '{removed_item.name}' noņemta no groza." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Lūdzu, ievadi skaitli!" + Style.RESET_ALL)
                
        elif remove_choice == '2':
            try:
                items_to_remove = input(Fore.WHITE + "Ievadi preces numurus, kuras vēlies noņemt (piem., 1,3,5): " + Style.RESET_ALL)
                indices = [int(x.strip()) - 1 for x in items_to_remove.split(',') if x.strip().isdigit()]
                
                # Sortējam indeksus dilstošā secībā, lai noņemšana neizmainītu indeksus
                indices.sort(reverse=True)
                
                removed_count = 0
                for idx in indices:
                    removed_item = self.cart.remove_item(idx)
                    if removed_item:
                        removed_count += 1
                        
                if removed_count > 0:
                    print(Fore.RED + f"No groza noņemtas {removed_count} preces." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "Neviena prece netika noņemta. Pārliecinieties, ka ievadītie numuri ir pareizi." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Lūdzu, ievadi korektus skaitļus, atdalītus ar komatiem!" + Style.RESET_ALL)
                
        elif remove_choice == '3':
            confirm = input(Fore.WHITE + "Vai tiešām vēlies iztukšot visu grozu? (j/n): " + Style.RESET_ALL).lower()
            if confirm == 'j':
                items_count = len(self.cart.items)
                self.cart.items.clear()
                print(Fore.RED + f"Grozs iztukšots. Noņemtas {items_count} preces." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Groza iztukšošana atcelta." + Style.RESET_ALL)
                
        elif remove_choice == '4':
            return
            
        else:
            print(Fore.RED + "Nepareiza izvēle!" + Style.RESET_ALL)

    def show_categories(self):
        print(Fore.RED + "\nPieejamās kategorijas:" + Style.RESET_ALL)
        for idx, category in enumerate(self.categories, start=1):
            color_code = self.category_colors.get(category, Style.RESET_ALL)
            print(f"{color_code}{idx}. {category}{Style.RESET_ALL}")
        print(Fore.RED + "Izvēlies kategoriju, ievadot tās numuru." + Style.RESET_ALL)

class CartItem:
    def __init__(self, product, size, color):
        self.name = product.name
        self.price = product.price
        self.size = size
        self.color = color

    def display_info(self):
        return f"{self.name:<20}{self.price:<10.2f}{self.size:<15}{self.color:<30}"