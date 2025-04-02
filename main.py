import csv

def read_products(filename):
    products = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            name, price, category = row
            products.append({'name': name, 'price': float(price), 'category': category})
    return products

def display_products_by_category(products, selected_category=None):
    categories = set(product['category'] for product in products)
    
    if selected_category:
        categories = {selected_category}  # Filter to show only the selected category
    
    unique_idx = 1  # Start unique index for each product
    print("\nPreces pēc kategorijām:")
    
    for category in categories:
        print(f"\n{category}:")
        filtered_products = [p for p in products if p['category'].lower() == category.lower()]
        if not filtered_products:
            print(f"Nav preču kategorijā: {category}")
        else:
            for product in filtered_products:
                print(f"{unique_idx}. {product['name']} - {product['price']}€")
                unique_idx += 1  # Increment the unique index for each product

def add_to_cart(cart, products):
    try:
        choice = int(input("\nIzvēlies preci (ievadi skaitli): "))
        if 1 <= choice <= len(products):
            product = products[choice - 1]
            cart.append(product)
            print(f"{product['name']} ir pievienota grozam!")
        else:
            print("Nepareiza izvēle!")
    except ValueError:
        print("Lūdzu, ievadi skaitli!")

def remove_from_cart(cart):
    if not cart:
        print("Groziņš ir tukšs.")
        return
    
    print("\nTavs grozs:")
    for idx, product in enumerate(cart, start=1):
        print(f"{idx}. {product['name']} - {product['price']}€")
    
    try:
        choice = int(input("\nIzvēlies preci, kuru vēlies noņemt no groza (ievadi skaitli): "))
        if 1 <= choice <= len(cart):
            product = cart.pop(choice - 1)
            print(f"{product['name']} ir noņemta no groza.")
        else:
            print("Nepareiza izvēle!")
    except ValueError:
        print("Lūdzu, ievadi skaitli!")

def view_cart(cart):
    if not cart:
        print("Tavs grozs ir tukšs.")
    else:
        print("\nTavs grozs:")
        total = 0
        for product in cart:
            print(f"{product['name']} - {product['price']}€")
            total += product['price']
        print(f"\nKopējā summa: {total}€")

def purchase_product(cart):
    if not cart:
        print("Groziņš ir tukšs!")
        return
    
    total = sum(item['price'] for item in cart)
    print(f"\nTavs kopējais pirkums ir: {total}€")
    print("Paldies par iepirkšanos!")

def main():
    products = read_products('products.csv')
    cart = []

    while True:
        print("\n--- Mūsu veikals ---")
        print("1. Apskatīt preces")
        print("2. Apskatīt grozu")
        print("3. Pievienot preci grozam")
        print("4. Noņemt preci no groza")
        print("5. Veikt pirkumu")
        print("6. Iziet")
        
        choice = input("\nIzvēlies darbību (1-6): ")

        if choice == '1' or choice == '3':  # Apvienota izvēle 1 un 3
            print("\nKategorijas:")
            categories = set(product['category'] for product in products)
            for idx, category in enumerate(categories, start=1):
                print(f"{idx}. {category}")
            category_choice = input("\nIzvēlies kategoriju (ievadi skaitli): ")
            try:
                category_choice = int(category_choice)
                if 1 <= category_choice <= len(categories):
                    selected_category = list(categories)[category_choice - 1]
                    display_products_by_category(products, selected_category)
                    add_to_cart(cart, products)  # After displaying, ask to add product to cart
                else:
                    print("Nepareiza izvēle!")
            except ValueError:
                print("Lūdzu, ievadi skaitli!")
        elif choice == '2':
            view_cart(cart)
        elif choice == '4':
            remove_from_cart(cart)
        elif choice == '5':
            purchase_product(cart)
            break
        elif choice == '6':
            print("Paldies, ka apmeklējāt mūsu veikalu!")
            break
        else:
            print("Nepareiza izvēle! Lūdzu, izvēlies no 1 līdz 6.")

if __name__ == "__main__":
    main()
