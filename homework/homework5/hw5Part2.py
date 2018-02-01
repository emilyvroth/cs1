file=input("Filename => ")
#file="temp_data.txt"
print(file)
month=int(input("Month => "))
#month=2
print(month)

lines=[]
for line in open(file):
	lines.append(line.strip().split(","))
lines.pop(0)


def extreme_avg_temp(month, function, data):
	dates=[]
	avg_temps=[]
	for line in data:
		if len(line[1])>0 and len(line[9])>0 and int(line[1][-2:len(line[1])])==month:
			dates.append(line[1])
			avg_temps.append(float(line[9]))
	return [function(dates),avg_temps[dates.index(function(dates))]]

def avg(data):
	avg_temps=[]
	for line in data:
		if len(line[1])>0 and len(line[9])>0 and int(line[1][-2:len(line[1])])==month:
			avg_temps.append(float(line[9]))
	return sum(avg_temps)/len(avg_temps)

def extreme_temp(month, function, data):
	dates=[]
	minimum=[]
	maximum=[]
	for line in data:
		if len(line[1])>0 and len(line[10])>0 and len(line[11])>0 and int(line[1][-2:len(line[1])])==month:
			dates.append(line[1])
			minimum.append(float(line[11]))
			maximum.append(float(line[10]))
	if function == min:		
		return [function(minimum), dates[minimum.index(function(minimum))]]
	if function == max:
		return [function(maximum), dates[maximum.index(function(maximum))]]

def histogram(month, data):
	dates=[]
	tens_list=[]
	dummy_tens=[]
	dummy_dates=[]
	for line in data:
		if len(line[1])>0 and len(line[9])>0 and int(line[1][-2:len(line[1])])==month:
			dummy_dates.append(line[1])
			dummy_tens.append(float(line[9]))
		if len(dummy_tens) == 10:
			dates.append(dummy_dates[0][0:4]+'-'+dummy_dates[-1][0:4])
			dummy_dates=[]
			tens_list.append(sum(dummy_tens)/len(dummy_tens))
			dummy_tens=[]
		if line==data[-1] and len(dummy_tens)!=0:
			dates.append(dummy_dates[0][0:4]+'-'+dummy_dates[-1][0:4])
			dummy_dates=[]
			tens_list.append(int(sum(dummy_tens)/len(dummy_tens)))
			dummy_tens=[]
	return dates,tens_list

print("Earliest recorded average {:.2f} in {}".format(extreme_avg_temp(month, min, lines)[1],extreme_avg_temp(month, min, lines)[0][0:4]))
print("Latest recorded average {:.2f} in {}".format(extreme_avg_temp(month, max, lines)[1],extreme_avg_temp(month, max, lines)[0][0:4]))
print("Average temperature: {:.2f}".format(avg(lines)))
print("Lowest min value recorded: {:.2f} in year(s): {}".format(extreme_temp(month, min, lines)[0],extreme_temp(month, min, lines)[1][0:4]))
print("Highest max value recorded: {:.2f} in year(s): {}".format(extreme_temp(month, max, lines)[0],extreme_temp(month, max, lines)[1][0:4]))
print("Histogram of average temperature")
#print(histogram(month,lines))

hist=histogram(month, lines)
for i in range(len(hist[0])):
	print("{}: {}".format(hist[0][i],int(hist[1][i])*"*"))
#print("{}-{}: {}".format(hist[2][0][0:4],hist[2][-1][0:4],int(sum(hist[3])/len(hist[3]))*"*"))