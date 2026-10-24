czas_format_24 = input("Enter time (24-hour format): ")
godzina_format_24 = int(czas_format_24[0:-3])
kiedy_godzina = ""
if godzina_format_24 < 12:
    kiedy_godzina = "am"
else:
    kiedy_godzina = "pm"
godzina_format_12 = godzina_format_24 % 12
#print(godzina_format_24)
minuta_format_24 = int(czas_format_24[-2:])
czas_format_12 = "Time in 12-hour format: " + str(godzina_format_12) + ":" + str(minuta_format_24) + kiedy_godzina
print(czas_format_12)