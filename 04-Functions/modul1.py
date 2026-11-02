def w_zakresie(x,y,co):
    if x < y:
        if y >= co and x <= co:
            return True
        else:
            return False
    else:
        if y <= co and x >= co:
            return True
        else:
            return False