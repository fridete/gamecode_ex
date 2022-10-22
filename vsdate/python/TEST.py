for thegusser in range(5):#1~100
    thegusser = float(input("你好欢迎来到本次抽奖，如果你猜中了，即可把奖品带回家。你有五次机会,请输入："))
    if thegusser == 10:
       print("恭喜你猜对了，本商品10元！")
       break
    else:
       print("太可惜了，再来一次吧")
       if thegusser>10:
           print("太大了")
       else:
           print("太小了")
       continue
if thegusser == 10:
    pass
else:
    print("你的机会用完了，欢迎下次光临")