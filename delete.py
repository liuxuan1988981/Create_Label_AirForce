import os
 
fold_dir = './data/'   # 需要修改的文件所在的文件夹
filename = os.listdir(fold_dir)  # 该文件夹中文件的名称
# print(filename)    # 在控制台输出原文件名称
 
for number, temp in enumerate(filename):
	    if number%2==0:
		    path='./data/'+temp
		    os.remove(path)
