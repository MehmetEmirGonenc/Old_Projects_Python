"""TEST1
def test(x,y=2): #y have default value
    print(x**y)
test(6,8)
test(6)
test(y=7,x=3)
"""
"""TEST2
def test(x,y,z):
    print( x*y/z)

print(test(56,43,86))
print('************************')
def test(x,y,z):
    return ( x*y/z)

print(test(56,43,86))
"""

"""TEST3

#####################################################
x=[]                                                #
##############################                      #
def add(y):                  #                      #
    x.append(y)              #######LOCAL AREA      ############GLOBAL AREA
    print(str(y)+ ' Added')  #                      #
##############################                      #
add(57)                                             #
print(x)                                            #
                                                    #
#####################################################
###IF u write variable without local variable name fuction looks for global variable!!


"""
def maas_hesaplama(x):
    if x>=3000:
        return x10/100+x
    else:
        return x20/100+x

def ekleme(x,y):
    return x.append(y)

kisi_sayisi=int(input("şirkette kaç kişi çalıştığını giriniz: "))
i=0
maaslar=[]

while(i<kisi_sayisi):
    maaslar.append(int(input("maaşı giriniz: ")))
    i+=1

print(maaslar)
yeni_maaslar=[]
for i in maaslar:
    a=maas_hesaplama(i)
    yeni_maaslar.append(a)


print(yeni_maaslar)
