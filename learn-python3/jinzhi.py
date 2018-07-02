a  = [['apple','orange','banana','grape'],(1,2,3)]
for x in a:
    for y in x:
        # end="" 每次输出结束后输出一个定义的字符串 
        print(y,end=" | ")
else:
    # 当列表中所有元素遍历完了之后执行
    print('fruit is gone')
