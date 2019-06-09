import random
list1 = []
list2 = []
x = 0
auto1 = str(random.randint(1000,10000))
print('=======================欢迎光临cctv.com=======================')
while 1:
	# list1 = []
	# list2 = []
	# print(list1,list2)
	auto1 = str(random.randint(1000,10000))
	shuzi=input('登录请输入1，注册请输入2：')
	if  shuzi == '1':
		print('==================登录页面==============')
		for x in range(0,4):
			print('您有',(4- x) ,'次登录机会')
			username = input('请输入您的用户名：')
			password = input('请输入您的密码：')
			# auto = str(random.randint(1000,10000))
			print(auto1)
			yanzhenma=input('请输入验证码')
			lenmame  = len(username)
			lenword  = len(password)
			if x >2 :
				x += 1
				print('您已经输入超过4次，请两分钟后重新输入或者重新注册密码，谢谢！')
				continue
			elif yanzhenma != auto1 or yanzhenma == ' ':
				print('验证码输入有误，请重新输入')
				continue
			elif (lenmame<2) and (lenmame>8):
				print('您输入的帐号长度是不合法的，请重新输入')
				continue
			elif lenword>8 or lenword<3:
				print('您输入的密码长度是不合法的，请重新输入')
				continue
			elif username not in list1 and password not in list2:

			# elif password not in list2:
				print('帐号或者密码是错误的，请重新输入')
				continue
			else:
				print('登录成功！')
				break
		break
	elif shuzi=='2':
		print("====================注册页面=======================")
		while 1:
			auto2 = str(random.randint(1000,10000))
			zhucename = input('请输入一个3到7长度的注册用户名:')
			zhucepass = input('请输入一个3到7长度的注册密码:')
			querenpass= input('请确认密码')
			print(auto2)
			yangzhenma=input('请输入验证码')
			lenzhucen = len(zhucename)
			lenzhucep = len(zhucepass)
			if yangzhenma != auto2:
				print('验证码输入有误，请重新输入')
				continue
			elif querenpass != zhucepass:
				print('两次密码输入不一致，请重新输入')
				continue
			elif lenzhucen >8 and lenzhucen < 3:
				# zhucename=input('请按照规定长度重新输入注册用户名：')
				print('请按照规定长度重新输入3-7位注册用户名：')
				continue
			elif lenzhucep > 8 and lenzhucep <3:
				print('请按照规定长度重新输入3-7位的密码：')
				continue
			else:
				list1.append(zhucename)
				list2.append(zhucepass)
				print('注册成功！',list1)
				break
		continue
	else:
		print('输入错误，请重新输入')
		continue
print('===============================welcome to my home============================')



	

