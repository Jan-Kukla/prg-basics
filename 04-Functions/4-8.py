def time_string(hours, minutes, time_format):
    format = int(time_format)
    if minutes < 10:
        minuta = f'0{minutes}'
    else:
        minuta = minutes
    if format == 12:
        if hours >= 12 and hours < 24:
            przyrostek = "pm"
        else:
            przyrostek = "am"
        if hours == 12 or hours == 24 or hours == 0:
            godzina = 12
        else:
            godzina = hours % format
    else:
        godzina = hours
        przyrostek = ''
    calosc = f'{godzina}:{minuta}{przyrostek}'
    return calosc

ktota = time_string(12, 46, '12')
print(ktota)

#blad w cwiczeniu