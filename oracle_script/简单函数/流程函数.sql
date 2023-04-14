SELECT NVL(NULL,1),'1不空为1，否则2' FROM DUAL;--如果第一个参数为空,值为第二个参数
SELECT NVL2(NULL,0,1),'1不空为2，否则3' FROM DUAL;--如果第一个参数不为空,值为第2个参数，值为第3个参数
SELECT DECODE(3/1,3,'正确答案','错误答案') FROM DUAL;
---DECODE(value,if1,then1,if2,then2,if3,then3,...,else)，表示如果value等于if1时，DECODE函数的结果返回then1,...,
-- 如果不等于任何一个if值，则返回else
SELECT NULLIF(1,0) FROM DUAL;
