import string

#rule 1
def rule_1(password):
	is_long_enough = len(password) <= 25 and len(password) >= 10
	first_is_letter = password[0] in string.ascii_letters
	if is_long_enough and first_is_letter:
		return True
	return False
#rule 2
def rule_2(password):
	has_at="@" in password
	has_dollar="$" in password
	has_percent="%" in password
	if has_at or has_dollar and not has_percent:
		return True
	return False 
#rule 3
def rule_3(password):
	num=['1','2','3','4']
	has_lower = any([character in password for character in string.ascii_lowercase])
	has_upper = any([character in password for character in string.ascii_uppercase])
	has_num = any([character in password for character in num])
	if has_lower and has_upper or has_num:
		return True
	return False
#rule 4
def rule_4(password):
	if password[-1] in string.ascii_uppercase:
		return False
	for i in range(len(password)-1):
		if password[i] in string.ascii_uppercase and password[i+1]!='_':
			return False
	return True
#rule 5
def rule_5(password):
	high_num=['5','6','7','8','9','0']
	for i in password:
		if i in high_num:
			return False
	return True

word=input("Enter a password => ")
print(word)

if rule_1(word) == True:
	print("Rule 1 is satisfied")
else:
	print("Rule 1 is not satisfied")

if rule_2(word) == True:
	print("Rule 2 is satisfied")
else:
	print("Rule 2 is not satisfied")

if rule_3(word) == True:
	print("Rule 3 is satisfied")
else:
	print("Rule 3 is not satisfied")

if rule_4(word) == True:
	print("Rule 4 is satisfied")
else:
	print("Rule 4 is not satisfied")

if rule_5(word) == True:
	print("Rule 5 is satisfied")
else:
	print("Rule 5 is not satisfied")

if rule_1(word) == True and rule_2(word) == True and rule_3(word) == True and rule_4(word) == True and rule_5(word) == True:
	print("The password is valid")
else:
	if rule_1(word)==True:
		print("A suggested password is",word[0:8]+"42"+word[-8:len(word)])