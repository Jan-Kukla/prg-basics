####
# Functions to read any data type from the keyboard
#
def input_string(message):
    mes = input(message)
    return str(mes)

def input_integer(message):
    mes = input(message)
    return int(mes)

def input_real(message):
    mes = input(message)
    return float(mes)

def input_boolean(message):
    mes = input(message)
    if mes == "y":
        co = True
    else:
        co = False
    return (co)