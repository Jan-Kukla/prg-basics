def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inches(n):
    return n*0.39

def feet_to_cm(n):
    return n*30.48

def inches_to_cm(n):
    return n/0.39

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'532cm = {cm_to_inches(532)} inches')
    print(f'532 feet = {feet_to_cm(532)}cm')
    print(f'532 inches = {inches_to_cm(532)}cm')

