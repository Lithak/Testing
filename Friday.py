file = open('/home/user/Desktop/Friday.txt', 'w+')
file.writelines("I'm a poet\n")
file.writelines("I'm bored asf\n")
file. write("I Love Fat Cakes\n")
file.write("I miss my Mother\n")
file.write("I'm so obsessed with Clothes\n")
file.close()
file = open('/home/user/Desktop/Friday.txt', 'r+')
for each in file:
    print(each)