############################TUPLE###############################
# 1- inclusive
# 2- ordered
# 3- Static variable(Unchangeable)
#
"""TEST1
t =('Ali','Veli',32)
print(type(t))
t1 =('Ali')
print(type(t1))
t1 =('Ali',)
print(type(t1))
"""
############################DICTIONARY###############################
# 1- inclusive
# 2- unordered
# 3- dynamic variable(Changeable)
#
"""TEST1
dictionaty = {'MEG' : 'nonsence',
              'TKS' : 'sense',
              'GHJ' : 32,
              43    : 76}
print(dictionaty)
print(len(dictionaty))
print(dictionaty['MEG'])
print(dictionaty['TKS'])
print(dictionaty['GHJ'])
print(dictionaty[43])
"""
"""TEST2
dictionaty = {'MEG' : {'NSNC' : 880,
                       'NPROP': 676,
                       'POPR' : 'GLK'},
              'TKS' : ['SNC',78],
              'GHJ' : ['JHK','KKS'],
              43    : ['PKS',990]}
print(dictionaty)
print(dictionaty['MEG']['POPR'])
"""
"""TEST3
dictionaty = {'MEG' : 'nonsence',
              'TKS' : 'sense',
              'GHJ' : 32,
              43    : 76}
print(dictionaty)
dictionaty['KGB'] ='Wolves Valley'
print(dictionaty)
dictionaty['KGB'] ='Volves Valley Ambush'
print(dictionaty)
"""
#!!!!!!!!!!!dictionary{KEY :[What do you want]}!!!!!!!!!!!!!!!
#                      ^^^
#                      There is so important , you cn write only static verable on there so
#                      you cant write dynamic verable on there (list etc.)
