# 作者
# NATURE
# 日期
# 2023/2/14 14:04
# 功能
# 字符串从左到右开始匹配满足正则表达式情况
import re

print(re.findall("abc", "abcdefghabcdhig"))  # 普通字符
print(re.findall("ab|cd", "abcdefghabcdhig"))  # 或
print(re.findall("f.o", "foo is not fao"))  # 匹配单一字符
print(re.findall("^hello", "hello world"))  # 匹配开始位置元字符:^
print(re.findall("py$", "hello.py"))  # 匹配结束位置元字符:$
print(re.findall("ab*", "ababbbcdefabbba"))  # 匹配重复元字符:*匹配规则:匹配前面的正则表达式重复0次或多次([b*]代表字符[a,ab,abb,abb...])
print(re.findall("ab+", "ababbbcdefabbba"))  # 匹配重复元字符:+匹配规则:匹配前面的正则表达式重复1次或多次([b+]代表字符[ab,abb,abb...])
print(re.findall("ab?", "ababbcdefabbba"))  # 匹配重复元字符:? 匹配规则:匹配前面的正则表达式重复0次或1次([b?]代表字符[a,ab,abb,abb...])
print(re.findall("ab{3}", "ababbbcdefabbba"))  # 匹配重复元字符:{n} 匹配规则:匹配前面的正则表达式重复0次或1次([b{3}}]代表字符[a,ab,abb,abb...])
print(re.findall("ab{2,5}", "abcdabbbabbbbbb"))  # 匹配重复元字符:? 匹配规则:匹配前面的正则表达式重复0次或1次([b{3}}]代表字符[a,ab,abb,abb...])
print(re.findall("a[a-z]", "abcdabbbabbbbbbac"))  # 匹配字符集合元字符:a[] 匹配规则:匹配括号范围内的任意一个字符，必须要匹配到一个值和a整体出现
print(re.findall("a[^abc]", "abcdabbbabbbbbbacad"))  # 匹配字符集合元字符:a[]匹配规则:匹配括号范围内的任意一个字符,必须要匹配到一个值和a整体出现
print(re.findall("1\d{10}","17611665537111"))  # digital 匹配任意(非）数字字符元字符:\d\D 匹配规则:\d 匹配任意数字字符  \D匹配任意非数字字符.\d{10}代表\d\d\d\d\d\d\d\d\d\d
print(re.findall("\w+", "hello$1_"))  # word# 匹配（非）普通字符（普通字符:数字字母下划线) \w匹配任意一个普通字符  \W匹配任意非普通字符
print(re.findall("\S", 'hello world\r\n\t\0'))  # space 匹配（非）空字符元字符:\s\S 匹配规则:\s匹配任意空字符   \S匹配任意非空字符
print(re.findall("\A/\w+/\w+\Z", '/football/zhongchao'))  # 匹配起止位置元字符:\A\Z 匹配规则:\A匹配开始位置 \Z匹配结束位置
print(re.findall("^/\w+/\w+$", '/football/zhongchao'))  # 匹配起止位置元字符:\A\Z 匹配规则:\A匹配开始位置 \Z匹配结束位置
print(re.findall(r"\Bis\b", 'This is a test'))  # 单词边界位置元字符:\b  \B匹配规则:\b匹配单词的边界   \B匹配非单词的边界 单词边界:数字字母下划线和其他字符的交界位置为单词的边界
print(re.findall(r"1.*1", '10010001'))  # 贪婪模式:模式匹配搜索到的、尽可能长的字符串。
print(re.findall(r"1.??1", '10010001'))  # 非贪婪模式:模式匹配搜索到的、尽可能短的字符串
print(re.findall(r"1.+?1", '10010001'))  # 非贪婪模式:模式匹配搜索到的、尽可能短的字符串
print(re.findall(r"1.{1,2}?1", '1000101'))  # 非贪婪模式:模式匹配搜索到的、尽可能短的字符串
print(re.findall(r"1.{1,2}?1", '1000101'))  # 非贪婪模式:模式匹配搜索到的、尽可能短的字符串
print(re.findall(r"\B1b1c\B",'101b1c0101'))  # 非贪婪模式:模式匹配搜索到的、尽可能短的字符串

