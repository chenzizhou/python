score=int(input('请输入您的成绩:'))
if 0>score or score>100:
   print('您输入值错误！')
   score=int(input('请重新输入您的成绩:'))
while 0<=score<=100:
    if score>=90 and score<100:
        print('您的评级为:A')
        break
    elif score>=80 and score<90:
        print('您的评级为:B')
        break
    elif score>=60 and score<80:
        print('您的评级为:C')
        break
    elif score<60:
        print('您的评级为:D')
        break

