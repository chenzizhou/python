SELECT
	lpad( 'chen', 5, 'a' ), ----向左填充
	rpad( 'chen', 5, 'a' ), ----向右填充
	chr( 65 ),						 ----对应ascii 码字符
	ascii( 'A' ),						---对应ASCII码数值
	initcap( 'chenziran' ),	----首字母大写
	lower( 'CHENZIRAN' ),		----转换成小写
	upper( 'chenziran' ),		----转换成大写
	substr( 'chenziran', 1, 4 ),----截取字符
	REPLACE ( 'chenzizhou', 'zhou', 'ran' ),----替换字符
	instr('chenzizhou','z',1,2),----获取查找字符坐在位置
	length( 'chenziran' ),----获取字符长度
	ltrim( 'chenziran', 'cziran' ),----左边第一个字符不能出现在右边字符串中
	rtrim( 'chenziran', 'chen' )-----右边第一个字符不能出现在右边字符串中
FROM
	dual;