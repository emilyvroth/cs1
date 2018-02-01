from Date2 import *

def birthday_list(file):
	birthdays=[]
	for line in open(file):
		line=line.strip().split(" ")
		birthdays.append(Date(line[0],line[1],line[2]))
	return birthdays

if __name__ == '__main__':
	birthdays=birthday_list("birthdays.txt")
	minimum=birthdays[0]
	maximum=birthdays[0]
	months_count=dict()
	for date in birthdays:
		if date<minimum:
			minimum=date
		if maximum<date:
			maximum=date
		if date.month in months_count:
			months_count[date.month]+=1
		else:
			months_count[date.month]=1
	most_month=max(months_count.keys(),key=lambda x: months_count[x])
	most_month_name=month_names[most_month]

	print("Earliest birthday: ", str(minimum))
	print("Latest birthday: ", str(maximum))
	print("Month with the most birthdays: ", most_month_name)


