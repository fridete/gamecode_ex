from re import I
from subprocess import _TXT
def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存成功") 
I = input("请输入用户名:")
thehavenones = []
for thehavenone in thehavenones:
    if thehavenone == I.lower:
        thehavenone.append(I)
    else:
        print("无效用户名")
print("现有用户：", thehavenones)
text_save(ce.txt,thehavenones)