import csv

class Product:
    # Kategoriju-krāsu kartējums
    CATEGORY_COLORS = {
        "Apģērbi": '\033[96m',  # Cyan
        "Apavi": '\033[92m',    # Green
        "Aksesuāri": '\033[35m',  # Magenta
        "Elektronika": '\033[93m',  # Yellow
        "Cits": '\033[97m',  # White (default),
        "krekli": '\033[96m',   # Cyan
        "šorti": '\033[96m',    # Cyan
        "džemperi": '\033[96m', # Cyan
        "bikses": '\033[96m',   # Cyan
    }
    RESET_COLOR = '\033[0m'  # Reset krāsa (balta)

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
            return True
        return False

    def display_info(self):
        sizes_display = ", ".join(f"{s} ({q})" for s, q in self.sizes.items() if q > 0) or "Nav pieejams"
        colors_display = ", ".join(self.colors)
        color_code = self.CATEGORY_COLORS.get(self.category, self.RESET_COLOR)
        return f"{self.name:<20}{self.price:<10.2f}{sizes_display:<20}{colors_display:<30}{self.RESET_COLOR}"

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
        
    def filter_by_price_range(self, min_price, max_price):
        """Jauna metode filtrēšanai pēc cenas diapazona"""
        return [p for p in self.products 
                if p.is_available() and min_price <= p.price <= max_price]
                
    def filter_by_size(self, size):
        """Jauna metode filtrēšanai pēc izmēra"""
        return [p for p in self.products 
                if p.is_available() and size in p.sizes and p.sizes[size] > 0]
                
    def filter_by_color(self, color):
        """Jauna metode filtrēšanai pēc krāsas"""
        return [p for p in self.products 
                if p.is_available() and any(color.lower() in c.lower() for c in p.colors)]
                
    def get_available_sizes(self):
        """Atgriež visus pieejamos izmērus"""
        sizes = set()
        for product in self.products:
            for size, qty in product.sizes.items():
                if qty > 0:
                    sizes.add(size)
        return sorted(list(sizes))
        
    def get_available_colors(self):
        """Atgriež visas pieejamās krāsas"""
        colors = set()
        for product in self.products:
            if product.is_available():
                for color in product.colors:
                    colors.add(color.strip())
        return sorted(list(colors))