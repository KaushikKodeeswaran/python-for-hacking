#! /usr/bin/env python

def generate(arr, i, s, length,filename): 
    if (i == 0): 
        f = open(filename + ".txt", "a")
	f.write(s+"\n")
	f.close()
        return
      
    for j in range(0, length): 
        appended = s + arr[j] 
        generate(arr, i - 1, appended, length,filename) 
    return
  
def Range(arr, len): 
    for i in range(1, len + 1):  
	    generate(arr, i, "", len) 

	
def load(option):
	lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
	SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
	length = int(input("Enter lenght :"))
	filename = str(raw_input("Enter file name to be saved \n"))
	
	if option == 1:
		generate(lower_case, length, "", 26,str(filename) )
	if option == 2:
		generate(upper_case, length, "", 26,filename )
	if option == 3:
		generate(DIGITS, length, "", 10,filename)
	if option == 4:
		generate(SYMBOLS, length, "", 16,filename)
	if option == 5:
		generate(lower_case+upper_case, length, "", 52,filename)
	if option == 6:
		generate(lower_case+DIGITS, length, "", 36,filename )
	if option == 7:
		generate(lower_case+SYMBOLS, length, "", 42,filename )
	if option == 8:
		generate(upper_case+DIGITS, length, "", 36,filename )
	if option == 9:
		generate(upper_case+SYMBOLS, length, "", 42,filename)
	if option == 10:
		generate(DIGITS+SYMBOLS, length, "", 26,filename)
	if option == 11:
		generate(upper_case+SYMBOLS+lower_case, length, "", 68,filename)
	if option == 12:
		generate(upper_case+DIGITS+lower_case, length, "", 62,filename)
	if option == 13:
		generate(upper_case+SYMBOLS+DIGITS+lower_case, length, "", 78,filename)
def main():
	print('''1 - Lower Case \n2- Upper Case \n3- Digits \n4- Symbols \n5- Lower + Upper \n6- Lower + Digits \n7- Lower + Symbols \n8- Upper + Digits \n9- Upper + Symbols\n10- Digits + Symbols\n11- Upper + Lower + Symbols\n12- Upper + Lower + Digits\n13- Upper + Lower + Digits + Symbols
	''')
	option = input("Enter Option :")
	load(option)
	
main()
print("[+] Done Successfully")


	
