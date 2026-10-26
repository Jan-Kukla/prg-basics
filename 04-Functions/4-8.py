def time_string(hours, minutes, time_format):
    #godzina = ''
    #minuta = ''
    #przyrostek = ''
    format = int(time_format)
    if minutes < 10:
        minuta = f'0{minutes}'
    else:
        minuta = minutes
    if format == 12:
        if hours >= 12:
            przyrostek = "pm"
        else:
            przyrostek = "am"
        godzina = hours % format
    else:
        godzina = hours
        przyrostek = ''
    calosc = f'{godzina}:{minuta}{przyrostek}'
    return calosc

ktota = time_string(19, 2, '12')
print(ktota)

#blad w cwiczeniu