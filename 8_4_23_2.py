a=list(map(int,input().split()))
length=a[0]
width=a[1]
square=a[2]

def length_count(length,square):

    i=0
    while(length>0):
        length=length-square
        i+=1
    return i
        
    return(i)
def width_count(width,square):
    j=0
    while(width>0):
        width=width-square
        j+=1
    return j
result=length_count(length,square)*width_count(width,square)
print(result)
    
    
