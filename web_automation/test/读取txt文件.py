# 作者
# NATURE
# 日期
# 2022/10/14 11:38
# 功能
#
user_file = open('../common/user_info.txt', 'r')
lines = user_file.readlines()
print(lines)
user_file.close()
for line in lines :
    username= line.split(',')[0]
    password= line.split(',')[1]
    print(username, password)
