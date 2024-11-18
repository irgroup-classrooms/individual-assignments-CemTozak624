import re
from collections import Counter

def main():
    
    # CSV-Datei mit Produktbestellungen lesen
    with open('C:/Uni/DIS08/individual-assignments-piaa0802/assignments/04/csv/orders.csv') as file:
        content = file.read()

    # Reguläre Ausdrücke definieren
    digit_pattern = r'\d+'
    order_id_pattern = r'Order #(\d+)'  # Aufgabe 1
    product_pattern = r'Product: (\w+)'  # Aufgabe 2
    price_pattern = r'Price: (\$\d+\.\d{2})'  # Aufgabe 3
    date_pattern = r'Date: (\d{4}-\d{2}-\d{2})'  # Aufgabe 4

    # Reguläre Ausdrücke auf den Text anwenden
    all_digits = re.findall(digit_pattern, content)
    order_ids = re.findall(order_id_pattern, content)  # Aufgabe 1
    product_list = re.findall(product_pattern, content)  # Aufgabe 2
    price_list = re.findall(price_pattern, content)  # Aufgabe 3
    order_dates = re.findall(date_pattern, content)  # Aufgabe 4

    high_value_products = []  # Aufgabe 5
    for price in price_list:
        amount = float(price.replace('$', ''))
        if amount > 500:
            high_value_products.append(amount)
    
    formatted_dates = []  # Aufgabe 6
    for date in order_dates:
        new_date_format = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', date)
        formatted_dates.append(new_date_format)

    long_name_products = []  # Aufgabe 7
    for product in product_list:
        if len(product) > 6:
            long_name_products.append(product)
    
    product_frequency = Counter(product_list)  # Aufgabe 8

    prices_with_99 = re.findall(r'Product: [A-Za-z]+, Price: \$\d+\.99', content)  # Aufgabe 9
    
    lowest_price = min(price_list)  # Aufgabe 10
    lowest_price_value = float(lowest_price.replace('$', ''))

    # Ergebnisse ausgeben
    print(all_digits)
    print("Alle Bestellnummern: ", order_ids)  # Aufgabe 1
    print("Alle Produktnamen: ", product_list)  # Aufgabe 2
    print("Alle Preise: ", price_list)  # Aufgabe 3
    print("Alle Bestelldaten: ", order_dates)  # Aufgabe 4
    print("Produkte über $500: ", high_value_products)  # Aufgabe 5
    print("Formatiertes Bestelldatum: ", formatted_dates)  # Aufgabe 6
    print("Produkte mit mehr als 6 Zeichen: ", long_name_products)  # Aufgabe 7
    print("Anzahl der Produkte: ", product_frequency)  # Aufgabe 8
    print("Bestellungen mit Preisen, die auf .99 enden: ", prices_with_99)  # Aufgabe 9
    print("Günstigstes Produkt: ", lowest_price_value)  # Aufgabe 10
    

if __name__ == '__main__':
    main()
