# -*- coding: utf-8 -*-
"""
Authors: Cindy Pino
Date: 3/26/2020
Description: Kelvin, Celsius, Farenheight Temperature Convertor"""

import sys
def tempConvertor():
	while True:             
	    inp1 = (input("Temperature one? (c = celsius, f = fahrenheit, k = kelvin)  "))   
	    if inp1 == "c" or inp1 == "f" or inp1 == "k":       
	    	break   
	 
	while True:             
	    inp2 = input("Temperature two? (c = celsius, f = fahrenheit, k = kelvin)  ")
	    if inp1 != inp2 and inp2 == "c" or inp1 != inp2 and inp2 == "f" or inp1 != inp2 and inp2 == "k":
	    	break  

	while True:            
	    inp3 = int(input(("What's your temperature  " )))   
	    if (inp3) <= 1000:       
	        break  

	if inp1 == "c" and inp2 == "f":
	    c1 = float(inp3) * 9/5 + 32
	    print(c1)
	elif inp1 == "c" and inp2 == "k":
	    c2 = float(inp3) + 273.15
	    print(c2)
                                                                              
	elif inp1 == "f" and inp2 == "c":
	    f1 = (float(inp3) - 32 ) * 5/9
	    print(f1)
	elif inp1 == "f" and inp2 == "k":
	    f2 = (((float(inp3) - 32) * 5/9 ) + 273.15 )
	    print(f2)
	elif inp1 == "k" and inp2 == "c":
	    k1 = (float(inp3) - 273.15) 
	    print(k1)
	else:
	    k2 = (((float(inp3) - 273.15) * 9/5 )+ 32) 
	    print(k2)
	    


def again():
	
	
	while True:
		inp4 = (str(input(" Do you want to try again? yes/no. "))).lower()
		if inp4 == "yes":
			tempConvertor()
		if inp4 == "no":
			sys.exit()
	
	while True:
		if inp4 != "yes" or inp4 != "no":
			break


	
	
(str(tempConvertor()))
(again())



























