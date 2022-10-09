v = 100
def outter():
	v = 200
	print("outter里的V=", v)#在函数内创建一个函数并调用
	def inner():
		nonlocal v#声明V为外部嵌套函数的作用域内的变v+=1
        v+=1
		print("inner里的V=",v)
	inner()#调用上面的函数
	print('调用inner后,outter里的', v)
outter()
print("全局里的V的值是:",v)