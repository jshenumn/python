#==============   List comprehension ================

office = [1907,1908,1903]

office.append(1901)
print('append 1901',office)
office.append(1902)
print('append 1902',office)
office.extend(office)
print('extend list by duplicate elements',office)
office.insert(1,1903)
print('insert 1903 at position 1',office)
office.remove(1901)
print('remove first 1901',office)
id = office.index(1901)
print('index the remaining 1901', office, id)
office.sort(reverse=False)
print('sort the list ascending',office)
office.reverse()
print('list reversing',office)
cnt = office.count(1902)
print('count occurrence of elements', office, cnt)
office_copy = office.copy()
print('shallow copy', office_copy)
print('Test completed')



