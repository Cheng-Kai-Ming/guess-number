#如何讓重複的count = count + 1
#　　　　　　print('玩了第', count, '次')　　可以從if/elif/elif之中化簡
#當使用者輸入非數字時 該如何印出'請輸入數字'並回到遊戲之中(初始狀態)
import random
start = input('請輸入初值')
end = input('請輸入末值')
start = int(start)
end = int(end)
count = 0
if start >= end:
	print('初值應大於末值')
else:
	r = random.randint(start, end)
	while True:
		num = input('請輸入數字')
		num = int(num)
		if num > r and num <= end:
			print('你猜太大了!!')
			print('介於', start,'到', num, '之間')
			count = count + 1
			print('玩了第', count, '次')
		elif num < r and num >= start:
			print('你猜太小了!!')
			print('介於', num,'到', end, '之間')
			count = count + 1
			print('玩了第', count, '次')
		elif num == r:
			print('你猜對了!!')
			count = count + 1
			print('玩了第', count, '次')
			break
		else:
			print('請輸入', start, '-', end, '的數字')


