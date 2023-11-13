import csv
with open("abcd.csv",'r')as keyfile:
	data=csv.reader(keyfile)
	for i in data:
	 print(i)
