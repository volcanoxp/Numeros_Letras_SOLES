
UNIDADES = ['CERO',
            'UNO',
            'DOS',
            'TRES',
            'CUATRO',
            'CINCO',
            'SEIS',
            'SIETE',
            'OCHO',
            'NUEVE']

DECENAS = ['',
            'DIEZ',
            'VEINTE',
            'TREINTA',
            'CUARENTA',
            'CINCUENTA',
            'SESENTA',
            'SETENTA',
            'OCHENTA',
            'NOVENTA']

CENTENAS = ['',
            'CIENTO',
            'DOSCIENTOS',
            'TRESCIENTOS',
            'CUATROCIENTOS',
            'QUINIENTOS',
            'SEISCIENTOS',
            'SETECIENTOS',
            'OCHOCIENTOS',
            'NOVECIENTOS']

NUMBERS = [UNIDADES, DECENAS, CENTENAS]

def letterDecimal(price: str) -> str:
    return 'CON '+ price.split(".")[1][0] + '0/100 SOLES'


def letterEnteros(price: str) -> str:

    final_price_letter = ''

    flag, final_price_letter = especialCases(price)
    if flag: 
        return final_price_letter

    for index, number in enumerate(reversed(price)):
        if index == 0 and int(number) != 0:
            final_price_letter = NUMBERS[index][int(number)]
    
        if index == 1:
            if final_price_letter == '':
                final_price_letter = NUMBERS[index][int(number)]
            else:
                if int(number) != 0:
                    final_price_letter = NUMBERS[index][int(number)]+ ' Y '+ final_price_letter
    
        if index == 2:
            if final_price_letter == '':
                final_price_letter = NUMBERS[index][int(number)]
            else:
                final_price_letter = NUMBERS[index][int(number)]+ ' '+ final_price_letter

    return final_price_letter


def especialCases(price: str) -> tuple:
    price = int(price)
    value_allow = [11,12,13,14,15,16,17,18,19,100]
    price_letter = ''

    if price not in value_allow:
        return False, price_letter

    if price == 11:
        price_letter = 'ONCE'
    elif price == 12:
        price_letter = 'DOCE'
    elif price == 13:
        price_letter = 'TRECE'
    elif price == 14:
        price_letter = 'CATORCE'
    elif price == 15:
        price_letter = 'QUINCE'
    elif price == 16:
        price_letter = 'DIECISEIS'
    elif price == 17:
        price_letter = 'DIECISIETE'
    elif price == 18:
        price_letter = 'DIECIOCHO'
    elif price == 19:
        price_letter = 'DIECINUEVE'
    elif price == 100:
        price_letter = 'CIEN'
    
    return True, price_letter


def price2Letter(price: float) -> str:
    price = str(float(price))
    enteros = price.split(".")[0]
    
    centenas = enteros[::-1][:3][::-1]
    miles = enteros[::-1][3:6][::-1]
    
    if len(enteros) > 6:
        return "-"

    r_miles = letterEnteros(miles)
    r_centenas = letterEnteros(centenas)
    r_decimales =  letterDecimal(price)
    
    if r_miles == "UNO":
        r_miles = "MIL "
    elif r_miles == "":
        pass
    else:
        r_miles += " MIL "

    return r_miles + r_centenas + ' ' + r_decimales

if  __name__ == "__main__":
    print(price2Letter(501123.1))
