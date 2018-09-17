data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完成, 共有', len(data), '筆資料')


sum_len = 0
for d in data: #每一個d是一個字串
	sum_len = sum_len + len(d)

print('平均為', sum_len/len(data), '個字')