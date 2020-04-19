#・末尾が s, sh, ch, o, x のいずれかである英単語の末尾に es を付ける
#・末尾が f, fe のいずれかである英単語の末尾の f, fe を除き、末尾に ves を付ける
#・末尾の1文字が y で、末尾から2文字目が a, i, u, e, o のいずれでもない英単語の末尾の y を除き、末尾に ies を付ける
#・上のいずれの条件にも当てはまらない英単語の末尾には s を付ける

import re
n = int(input())
for i in range(n):
    temp = input()
    result = ""
    end = temp[len(temp)-2] + temp[len(temp)-1] 
    sta1 = re.sub(".{1}$","",temp)
    sta2 = re.sub(".{2}$","",temp)
    if(re.search("(sh|ch)$",temp)):
        result = temp + "es"
    elif(re.search("(s|o|x)$",temp)):
        result = temp + "es"
    elif(re.search("(f)$",temp)):
        result = sta1 + "ves"
    elif(re.search("(fe)$",temp)):
        result = sta2 + "ves"
    elif(end[1] == "y"):
        if(not re.search("a|i|u|e|o",end[0])):
            result = sta1 + "ies"
        else:
            result = temp + "s"
    else:
        result = temp + "s"
    print(result)
