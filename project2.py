import os
def valid(check, pass_check):
	try:
		check = int(check) 
		print
		#os.system("color 0a")
		#print "Its a whole number"
		pass_check = False
		print pass_check
		return pass_check
	except:
		print
		os.system("color 0c" )
		os.system("cls")
		print "Please enter a whole number"
		print
	
	
os.system("color 07")
pass_check = True


while pass_check == True:
	whole_number = raw_input("Please input a whole number ->")
	valid(whole_number, pass_check)

	

	

#while True:
#	multiplier = raw_input("Please input a multiplier ->")
#	valid(multiplier)
#	break
	
#print int(whole_number) * int(multiplier)
