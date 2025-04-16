import csv

class Product:
    def __init__(self, name, price, category, sizes, colors):
        self.name = name
        self.price = price
        self.category = category
        self.sizes = sizes  # dict of sizes and quantities
        self.colors = colors  # list of colors

    def is_available(self):
        return any(qty > 0 for qty in self.sizes.values())

    def reduce_stock(self, size):
        if self.sizes.get(size, 0) > 0:
            self.sizes[size] -= 1

    def display_info(self):
        sizes_display = ", ".join(f"{s} ({q})" for s, q in self.sizes.items() if q > 0) or "Nav pieejams"
        colors_display = ", ".join(self.colors)
        return f"{self.name:<20}{self.price:<10.2f}{sizes_display:<20}{colors_display:<30}"


class ProductCollection:
    def __init__(self):
        self.products = []

    def load_from_csv(self, filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                sizes = {
                    size.strip(): int(qty)
                    for size_qty in row['sizes'].split(';')
                    for size, qty in [size_qty.split('=')]
                }
                product = Product(
                    name=row['name'],
                    price=float(row['price']),
                    category=row['category'],
                    sizes=sizes,
                    colors=row['colors'].split(',')
                )
                self.products.append(product)

    def get_categories(self):
        return list(set(p.category for p in self.products))

    def filter_by_category(self, category):
        return [p for p in self.products if p.category.lower() == category.lower()]
