from colorama import init, Fore, Style  # Importējam krāsu bibliotēku
from product import ProductCollection  # Importējam ProductCollection
from shop import Shop  # Importējam Shop

def main():
    init(autoreset=True)  # Initialize colorama with autoreset
    print(Fore.WHITE + "Laipni lūdzam mūsu veikalā!" + Style.RESET_ALL)

    # Izveidojam ProductCollection objektu
    print(Fore.WHITE + "Ielādējam produktus no CSV faila..." + Style.RESET_ALL)
    products = ProductCollection()
    products.load_from_csv('products.csv')  # Ielādējam produktus no CSV faila

    # Izveidojam Shop objektu
    print(Fore.RED + "Inicializējam veikalu..." + Style.RESET_ALL)
    shop = Shop(products)

    # Sākam veikala darbību
    print(Fore.RED + "Sākam veikala darbību!" + Style.RESET_ALL)
    shop.run()

    print(Fore.WHITE + "Paldies, ka izmantojāt mūsu veikalu!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()