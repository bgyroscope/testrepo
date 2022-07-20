

def simple():
    try:
        simple.counter += 1 
    except AttributeError : 
        simple.counter = 1 


    return simple.counter

# simple.counter = 0 
for j in range(5): 
    print( simple()  ) 


quit() 


def myfun(n): 
    for j in range(n): 
        if j %2 == 0 : 
            yield( j, j//2) 


for j,j2 in myfun(10): 
    print( j, j2 ) 


print( list( myfun(20) ) ) 


# try: 
# 
#     # x = [3,2,4] + 4
# 
#     y = x + 2 
# 
# except TypeError: 
#     print( 'oops. oh well. ' ) 
# 
# except: 
#     print( 'something else.') 
# 
# 





