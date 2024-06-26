
import re



def validate_numero_telefone(phone_number):
   
    
    pattern = "(XX) 9XXXX-XXXX"
    
    pattern = re.compile(r'^\(\d{2}\) \d{5}-\d{4}$')
    
    if re.match(pattern, phone_number):  
        print ("Número de telefone válido.")
       
    else:
        print ("Número de telefone inválido.")


phone_number = input()  
result = phone_number

validate_numero_telefone(result)

