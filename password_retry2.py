## 密碼重試程式
## password='a123456'
## 讓使用者重複輸入密碼
## 最多輸入3次
## 如果正確  就印出"登入成功!"
## 如果不正確  就印出"密碼錯誤! 還有__次機會"


K = 3
password = 'a123456'
while K > 0:
	pwd = input('請輸入密碼: ')
	
	if pwd == password:
		print('登入成功!')
		break #逃出迴圈
	else:
		K = K - 1
		print('密碼錯誤! 還有',K,'次機會')
		
