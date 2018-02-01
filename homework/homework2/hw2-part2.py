year=2017
day_length=[23,56,4]
rate=6/900000000

def time_to_seconds(hours,minutes,seconds):
	time_in_seconds=int((hours*60**2)+(minutes*60)+seconds)
	return time_in_seconds
def seconds_to_str(time_in_seconds):
	hours=int(time_in_seconds//60**2)
	minutes=int((time_in_seconds%60**2)//60)
	seconds=int((time_in_seconds%60**2)%60)
	modular_time=str(hours)+" hours "+str(minutes)+" mins "+str(seconds)+" secs"
	return modular_time

print("A day in 2017 is",day_length[0],"hours",day_length[1],"minutes and",day_length[2],"seconds long.")
print("Which is equivalent to",time_to_seconds(day_length[0],day_length[1],day_length[2]),"seconds.")

future_year=int(input("Enter a future year => "))
print(future_year)

future_day_length_seconds=int(time_to_seconds(day_length[0],day_length[1],day_length[2])+(future_year-year)*(rate*60**2))
future_day_length_modular=seconds_to_str(future_day_length_seconds)

print("A day in year",future_year,"will be",future_day_length_seconds,"seconds long\n\
which is equivalent to",future_day_length_modular)

