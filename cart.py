class Cart:
    HEADER_COLOR = '\033[96m'  # Cyan
    ITEM_COLOR = '\033[92m'    # Green
    TOTAL_COLOR = '\033[93m'   # Yellow
    RESET_COLOR = '\033[0m'    # Reset color

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        return None

    def is_empty(self):
        return len(self.items) == 0
        
    def get_item_count(self):
        """Atgriež preču skaitu grozā"""
        return len(self.items)
        
    def get_total_price(self):
        """Atgriež kopējo cenu bez atlaides un piegādes"""
        return sum(item.price for item in self.items)

    def view(self):
        if self.is_empty():
            print(self.HEADER_COLOR + "Tavs grozs ir tukšs." + self.RESET_COLOR)
            return

        print(self.HEADER_COLOR + "\nTavs grozs:" + self.RESET_COLOR)
        print(self.HEADER_COLOR + f"{'#':<5}{'Prece':<20}{'Izmērs':<10}{'Krāsa':<15}{'Cena':<10}" + self.RESET_COLOR)
        print(self.HEADER_COLOR + "-" * 60 + self.RESET_COLOR)
        total = 0
        for idx, item in enumerate(self.items, start=1):
            print(self.ITEM_COLOR + f"{idx:<5}{item.display_info()}" + self.RESET_COLOR)
            total += item.price
        print(self.TOTAL_COLOR + f"\nKopējā summa: {total:.2f}€" + self.RESET_COLOR)
        print(self.HEADER_COLOR + f"Preču skaits: {self.get_item_count()}" + self.RESET_COLOR)
        
    def checkout(self):
        """Veikt pirkumu un iztukšot grozu"""
        if self.is_empty():
            print(self.HEADER_COLOR + "Nevar veikt pirkumu, grozs ir tukšs." + self.RESET_COLOR)
            return False
            
        # Veikt pirkumu
        print(self.TOTAL_COLOR + "\nPaldies par pirkumu!" + self.RESET_COLOR)
        print(self.HEADER_COLOR + f"Veiksmīgi iegādātas {self.get_item_count()} preces!" + self.RESET_COLOR)
        
        # Iztukšot grozu
        self.items.clear()
        return True