import re

fi = open('states.txt','w')

fr = open("mohfwscraped.txt", "r")

tot = 0 
count = 0

for text in fr :
    count += 1
    if count == 1 or count == 2 :
        continue
    else :
        fi.write(text[4:len(text)-6])
        fi.write(' ')
    if count == 6 :
        fi.write('\n')
        count = 0
        tot += 1
    if tot == 33 :
        break
        
fi.close()
fr.close()