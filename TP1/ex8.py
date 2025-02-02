def somme_varargs(*args):
    result=0
    for x in args:
        result +=x
    return result
print(somme_varargs(1,2,3,4))        

