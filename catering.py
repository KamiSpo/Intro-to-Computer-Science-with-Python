lowest_price = 57

while lowest_price > 1:
    compared_price = int(input('Cena do porównania: '))
    if compared_price < lowest_price:
        lowest_price = compared_price

    print('Dotychczasowa najnizsza cena:', lowest_price)
    