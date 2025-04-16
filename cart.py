class CartItem:
    def __init__(self, product, size, color):
        self.name = product.name
        self.price = product.price
        self.size = size
        self.color = color

    def display_info(self):
        return f"{self.name:<20}{self.size:<10}{self.color:<15}{self.price:<10.2f}"


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item: CartItem):
        self.items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            return self.items.pop(index)

    def is_empty(self):
        return len(self.items) == 0

    def view(self):
        if self.is_empty():
            print("Tavs grozs ir tukšs.")
            return

        print("\nTavs grozs:")
        print(f"{'#':<5}{'Prece':<20}{'Izmērs':<10}{'Krāsa':<15}{'Cena':<10}")
        print("-" * 60)
        total = 0
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx:<5}{item.display_info()}")
            total += item.price
        print(f"\nKopējā summa: {total:.2f}€")

    def checkout(self):
        if self.is_empty():
            print("Groziņš ir tukšs!")
            return
        total = sum(item.price for item in self.items)
        print(f"\nTavs kopējais pirkums ir: {total:.2f}€")
        print("Paldies par iepirkšanos!")
        self.items.clear()
