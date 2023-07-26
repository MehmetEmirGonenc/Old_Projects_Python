############################LIST###############################
# 1- inclusive
# 2- ordered
# 3- dynamic variable(Changeable)
#
"""***TEST1***
list1 =[90,80,60,40]
print(list1)
print(type(list1))

list2=['Mehmet',19.15,0.6577654566545,list1]
print(list2)
print(type(list2))
print(len(list2))
print(type(list2[0]))
print(type(list2[1]))
print(type(list2[2]))
print(type(list2[3]))
print('************************************')
print(list2[0])
print(list2[0:2])
print(list2[:3])
print(list2[2:])
print(list2[3][2])
"""
"""TEST2
list = ['Ali','Fuat','Mehmet','Tufan','Naci']
print(list)
list[1] = 'Kazım'
print(list)
list[3:5] = 'Zehra', 'Gamze'
print(list)
list += ['Alperen', 'Nurhan']
print(list)
del list[4]
print(list)
"""
"""TEST3
list = ['Ali','Fuat','Mehmet','Tufan','Naci']
print(dir(list))
print(list)
list.append('Mustafa')
print(list)
list.remove('Ali')
print(list)
"""
"""TEST4
list = ['Ali','Fuat','Mehmet','Tufan','Naci']
print(list)
list.insert(2,'Nuraullah')
print(list)
list.insert(len(list),'Niyazi')
print(list)
list.pop(1)
print(list)
"""
"""TEST5
list = ['Ali','Fuat','Mehmet','Tufan','Naci','Mehmet','Mehmet','Mehmet','Ali']
print(list)
print(list.count('Ali'))
print(list.count('Mehmet'))
print(list.count('Naci'))
print(list.count('Hikmet'))
"""
"""TEST6
list = ['Ali','Fuat','Mehmet','Tufan','Naci','Mehmet','Mehmet','Mehmet','Ali']
print(list)
list_backup=list.copy()
print(list_backup)
"""
"""TEST7
list = ['Ali','Fuat','Mehmet','Tufan','Naci']
print(list)
list.extend(['Harun',786,78.90])
print(list)
"""
"""TEST8
list = ['Ali','Fuat','Mehmet','Tufan','Naci']
print(list)
print(list.index('Mehmet'))
print(list.index('Naci'))
"""
"""TEST9
list = ['Ali','Fuat','Mehmet','Tufan','Naci']
print(list)
list.reverse()
print(list)
"""
"""TEST10
list = ['Ali','Fuat','Mehmet','Tufan','Naci']
print(list)
list.clear()
print(list)
"""
##############################################