import re

fi = open('countries.txt','w')

fr = open('worldometersscraped.txt' , 'r')

fl = 0 
count = 0
c2 = 0
c3 = 0

for text in fr :
    x=text.strip();
    if x == '<tr class="total_row_world">' :
        fl = 1 ;
        fi.write('World ')
        continue ;
    elif fl == 1 and c2 == 0:
        if count == 0 :
            count += 1
            continue
        elif count <= 9 :
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
            count += 1
        elif x == 'XXXX' :
            c2 = 1
            count = 0
            fi.write('N.A. N.A. World')
            fi.write('\n')
    elif c2 == 1 :
        count += 1
        if count == 1 or count == 6 or count == 16 :
            continue
        elif count == 17 :
            fi.write('\n')
            count = 0 
        elif count == 2 :       
            start = [m.start() for m in re.finditer('>', x)]
            end = [m.start() for m in re.finditer('<', x)]
            abc = start[1]
            xyz = end[2]
            for it in range (abc+1,xyz) :
                fi.write(x[it])
            fi.write(' ')
        elif (count >= 3 and count <= 5) or (count >= 8 and count <= 14) or count == 15:
            start = [m.start() for m in re.finditer('>', x)]
            end = [m.start() for m in re.finditer('<', x)]
            abc = start[0]
            xyz = end[1]
            if xyz == abc+1 :
                fi.write('N.A.')
            else :
                for it in range (abc+1,xyz) :
                    fi.write(x[it])
            fi.write(' ')
        elif count == 7 :
            start = [m.start() for m in re.finditer('>', x)]
            end = [m.start() for m in re.finditer('<', x)]
            abc = start[0]
            xyz = end[0]
            if xyz == abc+1 :
                fi.write('N.A.')
            else :
                for it in range (abc+1,xyz) :
                    fi.write(x[it])
            fi.write(' ')
     
fi.close()
fr.close()   