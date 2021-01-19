list1 = []
# mkaes a list
openfile = open('FemaleNames.txt')
# opens felmale file
openfile2 = open('MaleNames.txt')
# opens male file
file = openfile.readlines()
# reads line by line
file2 = openfile2.readlines()
# reads list line by line
for name in file:
    if '\n' in name:
        list1.append(name[0:len(name) - 1])
#appends the name and adds to the list
    else:
        list1.append(name)
for name in file2:
    if '\n' in name:
        list1.append(name[0:len(name) - 1])
#appends the name and adds to the list
    else:
        list1.append(name)
openfile.close()
# closes file
openfile2.close()
# closes files
list1.sort()
#sorts list

for name in list1:
    print(name)
# prints list
firstBabyName = open("babyNamesAtoI.txt", "a")
# opens a new file
secondBabyName = open("babyNamesJtoR.txt", "a")
# opens a new file
thirdBabyName = open("babynamesStoZ.txt", "a")
# makes the last file

for x in range(0, 186):
#declares a range
    firstBabyName.write(list1[x] + "\n")
#writes the names in the file
for x in range(187, 349):
#declares a range
    secondBabyName.write(list1[x] + "\n")
#writes the names in the file
for x in range(350, 400):
#declares a range
    thirdBabyName.write(list1[x] + "\n")
#writes the names in the file
firstBabyName.close()
# closes file
secondBabyName.close()
# closes file
thirdBabyName.close()
# closes file
