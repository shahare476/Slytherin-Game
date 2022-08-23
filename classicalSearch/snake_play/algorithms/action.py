# we have tiles count = tc = 20 X 20
def action(list_direction):
    ret = []
    for i in list_direction:
        if(i == 'u'):
            ret.append(8)
        if(i == 'd'):
            ret.append(2)
        if(i == 'l'):
            ret.append(4)
        if(i == 'r'):
            ret.append(6)
    return(ret)
