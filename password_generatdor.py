import random
import string
import re

def tem_numero(texto):
    # Expressão regular para verificar se há algum dígito na string
    padrao = re.compile(r'\d')
    # Verifica se a expressão regular encontra correspondências na string
    if padrao.search(texto):
        return True
    else:
        return False

def tem_caracter_especial(texto):
    # Expressão regular para verificar se há algum caracter especial na string
    padrao = re.compile(r'[^\w\s]')
    # Verifica se a expressão regular encontra correspondências na string
    if padrao.search(texto):
        return True
    else:
        return False
    
def generate_password(min_Length, numbers=True,special_caracters=True):
    all_caracters = string.ascii_letters
    if numbers:
        all_caracters += string.digits
        password = "".join(random.sample(all_caracters,min_Length))
    if special_caracters:
        all_caracters += string.punctuation
        password = "".join(random.sample(all_caracters,min_Length))
         # Se não houver números nem caracteres especiais, retorna uma senha de letras
    if not (numbers or special_caracters):
        return "".join(random.choices(string.ascii_letters, k=min_Length))
    # Se houver números ou caracteres especiais, retorna uma senha com números e caracteres especiais
    while True:
        if (not numbers or tem_numero(password)) and \
           (not special_caracters or tem_caracter_especial(password)):
            return password
        password = "".join(random.sample(all_caracters,min_Length))

    
size_password = input("Please informe the length of the password: ")
if size_password.isdigit():
    size_password = int(size_password)

numbers = input("Do you want numbers in the password? (Y - N)")
if numbers.lower() == "y":
    numbers = True
else:
    numbers = False

special_caracters = input("Do you want special caracters in the password? (Y - N)")
if special_caracters.lower() == "y":
    special_caracters = True
else:
    special_caracters = False

final_password = generate_password(size_password,numbers,special_caracters)
print("Your password is: " + final_password)
