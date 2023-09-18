#we an add unlimted data in list and we an change also

frd = ['baki', 'chika', 'yujiro', 'jack']
num = [1, 2,  3, 4, 5]

#this append cmd is use to add the new element in the list insed of add attribute
frd.append('goku')
 
# This insert cmd is use to like the index find and insert the new element in list 
frd.insert(2, 'pikchu')

# This md is use to remove and delete the list
frd.remove('jack')
num.clear()

print (frd + num)
