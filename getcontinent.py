import re

fi = open('continents.txt','w')

fr = open('worldometersscraped.txt' , 'r')

fl = 0 
count = 0

for text in fr :
    x=text.strip();
    fl += 1
    if fl == 1 or fl == 2 or fl == 4 or fl == 16 or fl == 17 :
        continue;
    elif fl == 3 :
        ch = 1 
        for y in x :
            if y == '<' :
                ch =0
            elif y == '>' :
                ch =1
            elif ch == 1 :
                fi.write(y)
        fi.write(' ')
    elif fl == 18 :
        fl = 0 
        count += 1
        fi.write('\n')
    else :
        if len(x) == 9 :
            fi.write('N.A.')
        else :
            ch = 1 
            for y in x :
                if y == '<' :
                    ch =0
                elif y == '>' :
                    ch =1
                elif ch == 1 :
                    fi.write(y)
            fi.write(' ')
    if count == 6 :
        break
    
fi.close()
fr.close()