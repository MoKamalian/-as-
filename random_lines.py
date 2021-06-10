from time import sleep

the_file = open("/Users/mokamalian/Downloads/[as]/GSE167643_Expression_Gene.txt", "r")

for lines in the_file:
    print(the_file.readline())
    sleep(0.30)




