import random #加载随机模块
N = random.randint(1,6) #随机1-6中的任意整数
if N > 3: #判断是否大于3
	print('大，','生成的数值是',N,'。') #如果大于3执行
else: 
	print('小，','生成的数值是',N,'。') #如果小于3执行
