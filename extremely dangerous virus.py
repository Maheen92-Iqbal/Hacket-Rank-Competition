input_data = map(int, raw_input().split())
import math

a = input_data[0]
b = input_data[1]
t = input_data[2]

def mod_exponent(input_name,power_value,modulos):
   
    Y = 1
    
    while power_value > 0:
        if power_value % 2 == 0:
            input_name = int((input_name * input_name) % modulos)
            power_value = power_value/2
            
        else:
            Y = int((input_name * Y) % modulos)
            
            power_value = power_value - 1
        
        
    print int(Y)

x = (0.5*b + 0.5*a)
virus = mod_exponent(x,t,1000000000 + 7)
    