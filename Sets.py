######################Set##########################
# 1- Unordered
# 2- Unique Variable !!!!!
# 3- Dynamic(Changeable)
# 4- Can take different type of variable
#
"""TEST1
list =['Mehmet','Ahmet',56]
set = set(list)
print(set)
"""
"""TEST2
mehmet = 'mehmet_go_away_my_friend'
s = set(mehmet)
print(s)
list = ['Mehmet','Go','Away','Go','Friend','go']
s = set(list)
print(s)
"""
"""TEST3
list = ['Mehmet','Friend']
s=set(list)
print(s)
s.add('My')
print(s)
s.add('My')
print(s)
s.add('My')
print(s)
s.remove('My') # If 'My' is already not exist on the set , this command give an error,
               # if you don't want this you can write (discard) command
               # this command:if 'My' exist on the set , it delete(remove) this,
               # But if not exits on the set this command do nothing
print(s)
s.add('My')
print(s)
s.discard('My')
print(s)
s.discard('My')
print(s)
"""
# difference() the difference between the two set or '-' symbol
# intersection() intersection of two set or "&" symbol
# union() unite of two sets
# symmetric_difference() both of them non exits
"""TEST4
set1 = set([1,3,5])
set2 = set([1,2,3])

print(set1.difference(set2))
print(set2.difference(set1))

print(set1.symmetric_difference(set2))

print(set1-set2)
print(set2-set1)
"""
"""TEST5
set1 = set([1,3,5])
set2 = set([1,2,3])

print(set1.intersection(set2))
print(set2.intersection(set1))

print(set1&set2)

print(set1.union(set2))
print(set2.union(set1))

print(set1|set2)

print('***********************************')
print(set1)
set1.intersection_update(set2)
print(set1)
"""
"""TEST6
set1 = set([10,11,12,13])
set2 = set([4,5,6,7,8,9])

print(set1.isdisjoint(set2)) #This command means if the intersection of these sets are empty return 'True'
                             # if have any intersection item return 'Flase'
set1.add(9)
print(set1.isdisjoint(set2))

print('**********************************')

print(set1.issubset(set2)) # If set1 is a subset of set2 return 'True'
print(set2.issubset(set1)) # If set2 is a subset of set1 return 'True'

print('**********************************')

set3 =set([5,6,7,8])

print(set3.issubset(set1))
print(set3.issubset(set2))

print('**********************************')

print(set3.issuperset(set2)) #If set3 is a superset of set2 return 'Ture' if not 'False'
print(set2.issuperset(set3))
"""