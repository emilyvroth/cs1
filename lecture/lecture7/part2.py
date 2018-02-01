values=[14,10,8,19,7,13]

append_value=int(input("Enter a value: "))
print(append_value)
values.append(append_value)

value_index_two=int(input("Enter another value: "))
print(value_index_two)
values.insert(2,value_index_two)

print(values[3],values[-1])
print("Difference:",(max(values)-min(values)))
avg=sum(values)/len(values)
print("Average: {:.1f}".format(avg))
values_sorted=sorted(values)
median=(values_sorted[len(values)//2-1]+values_sorted[(len(values)//2)])/2
print("Median: {:.1f}".format(median))
	