x = int (input ("Please enter your result: "))
if x <= 100 and x >= 90:
	print ("A")
elif x <= 89 and x >= 80:
	print ("B")
elif x <= 79 and x >= 60:
     print ("C")
elif x <= 69 and x >= 50:
	print ("D")
elif x < 50:
	print ("F")
else: 
	print ("Check Again")