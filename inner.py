def mult_add(*args):
    def add(*args):
        res=0
        for n in args:
            res+=n
        return res

    def mult(*args):
        return args[0] * args[1]

    if len( args) >2:
        return add( *args)
    else:
        return mult( *args)




print( mult_add(2,3,4))
print( mult_add(2,3))