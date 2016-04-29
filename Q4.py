from Q4Moudle import UnorderedList
mylist = UnorderedList()

print(mylist.isEmpty())
mylist.add(3323)
mylist.add('melon')
mylist.add(1024)
print(mylist.size())        #['melon',3323,1024]
mylist.append(555)
print(mylist.search(555))   #['melon',3323,1024,555]
print(mylist.size())
mylist.remove(1024)         #['melon',3323,555]
print(mylist.size())
print(mylist.index(555))
mylist.insert(2,44)         #['melon',3323,44,555]
print(mylist.index(44))
mylist.pop()                #['melon',3323,44]
print(mylist.search(555))
mylist.pop(1)               #['melon',44]
print(mylist.search(3323))
