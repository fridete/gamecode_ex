import re
'''
把字符串替换成!!!
'''
s = "黑客"
try:
    print(re.sub(r'\b黑客\b', "!!!", s))
except:
    print("sth was wrong")
finally:
    print("end")
# the number hello-hello-hello