# we have tiles count = tc = 20 X 20
def dfs_action():
    l = ['r', 'r', 'r', 'r', 'd', 'l', 'l', 'l', 'l', 'd', 'r', 'r', 'r', 'r', 'd', 'l', 'l', 'l', 'l', 'd', 'r', 'r', 'r', 'r']
    ret = []
    for i in l:
        if(i == 'u'):
            ret.append(8)
        if(i == 'd'):
            ret.append(2)
        if(i == 'l'):
            ret.append(4)
        if(i == 'r'):
            ret.append(6)
    return(ret)