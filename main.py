import csv

def read_products(filename):
    products = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sizes = {}
            for size_entry in row['sizes'].split(';'):
                size, qty = size_entry.split('=')
                sizes[size.strip()] = int(qty)
            products.append({
                'name': row['name'],
                'price': float(row['price']),
                'category': row['category'],
                'sizes': sizes,
                'colors': row['colors'].split(',')
            })
    return products

def display_products_by_category(products, selected_category=None):
    categories = set(product['category'] for product in products)

    if selected_category:
        categories = {selected_category}

    print("\nPreces pēc kategorijām:")
    filtered = []

    for category in categories:
        print(f"\n{category.capitalize()}:")
        category_products = [p for p in products if p['category'].lower() == category.lower()]

        if not category_products:
            print("Nav preču šajā kategorijā.")
            continue

        print(f"{'#':<5}{'Nosaukums':<20}{'Cena':<10}{'Izmēri':<20}{'Krāsas':<30}")
        print("-" * 85)
        for idx, product in enumerate(category_products, start=1):
            sizes_display = ", ".join(
                f"{size} ({qty})" for size, qty in product['sizes'].items() if qty > 0
            ) or "Nav pieejams"
            colors_display = ", ".join(product['colors'])
            print(f"{idx:<5}{product['name']:<20}{product['price']:<10.2f}{sizes_display:<20}{colors_display:<30}")
        filtered.extend(category_products)

    return filtered

def add_to_cart(cart, products):
    try:
        choice = int(input("\nIzvēlies preci (ievadi skaitli): "))
        if 1 <= choice <= len(products):
            product = products[choice - 1]
            available_sizes = {s: q for s, q in product['sizes'].items() if q > 0}
            if not available_sizes:
                print("Šī prece nav pieejama nevienā izmērā.")
                return

            print(f"Ir pieejami izmēri: {', '.join(available_sizes.keys())}")
            size_choice = input("Izvēlies izmēru: ").strip().upper()
            if size_choice in available_sizes:
                print(f"Pieejamās krāsas: {', '.join(product['colors'])}")
                color_choice = input("Izvēlies krāsu: ").strip()
                if color_choice not in product['colors']:
                    print("Nepareiza krāsa vai nav pieejama.")
                    return
                cart.append({
                    'name': product['name'],
                    'price': product['price'],
                    'size': size_choice,
                    'color': color_choice
                })
                product['sizes'][size_choice] -= 1
                print(f"{product['name']} ({size_choice}, {color_choice}) ir pievienota grozam!")
            else:
                print("Nepareizs izmērs vai nav pieejams.")
        else:
            print("Nepareiza izvēle!")
    except ValueError:
        print("Lūdzu, ievadi skaitli!")

def remove_from_cart(cart):
    if not cart:
        print("Groziņš ir tukšs.")
        return

    print("\nTavs grozs:")
    print(f"{'#':<5}{'Prece':<20}{'Izmērs':<10}{'Krāsa':<15}{'Cena':<10}")
    print("-" * 60)
    for idx, item in enumerate(cart, start=1):
        print(f"{idx:<5}{item['name']:<20}{item['size']:<10}{item['color']:<15}{item['price']:<10.2f}")

    try:
        choice = int(input("\nIzvēlies preci, kuru vēlies noņemt no groza (ievadi skaitli): "))
        if 1 <= choice <= len(cart):
            removed = cart.pop(choice - 1)
            print(f"{removed['name']} ({removed['size']}, {removed['color']}) ir noņemta no groza.")
        else:
            print("Nepareiza izvēle!")
    except ValueError:
        print("Lūdzu, ievadi skaitli!")

def view_cart(cart):
    if not cart:
        print("Tavs grozs ir tukšs.")
        return

    print("\nTavs grozs:")
    print(f"{'#':<5}{'Prece':<20}{'Izmērs':<10}{'Krāsa':<15}{'Cena':<10}")
    print("-" * 60)
    total = 0
    for idx, item in enumerate(cart, start=1):
        print(f"{idx:<5}{item['name']:<20}{item['size']:<10}{item['color']:<15}{item['price']:<10.2f}")
        total += item['price']

    print(f"\nKopējā summa: {total:.2f}€")

def purchase_product(cart):
    if not cart:
        print("Groziņš ir tukšs!")
        return
    total = sum(item['price'] for item in cart)
    print(f"\nTavs kopējais pirkums ir: {total:.2f}€")
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

        if choice in ['1', '3']:
            categories = list(set(p['category'] for p in products))
            print("\nKategorijas:")
            for idx, cat in enumerate(categories, start=1):
                print(f"{idx}. {cat}")
            try:
                cat_choice = int(input("Izvēlies kategoriju: "))
                if 1 <= cat_choice <= len(categories):
                    selected = categories[cat_choice - 1]
                    filtered_products = display_products_by_category(products, selected)
                    if choice == '3':
                        add_to_cart(cart, filtered_products)
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