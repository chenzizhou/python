# \r关闭返回到首行，打印字符覆盖之前打印的字符
print('nihao\rc')
# \f换行后在对应结束位置继续打印字符
print('nihao\fc')
# \t缩减两个字符 4个字节
print('nihao\tc')
# 覆盖前一个字符打印
print('nihao\bc')

print('nihao\0c')
# 和分页相似

print('nihao\vc')