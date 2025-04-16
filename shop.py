class Shop:
    def __init__(self, products):
        self.products = products
        self.cart = cart()
        self.products.load_from_csv(products)
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
                categories = self.products.get_categories()
                self.show_categories()

                try:
                    cat_choice = int(input("Izvēlies kategoriju: "))
                    if 1 <= cat_choice <= len(categories):
                        selected = categories[cat_choice - 1]
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
