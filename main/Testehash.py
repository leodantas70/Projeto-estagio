import hashlib
import requests

from datetime import date

data = date.today()
print (data)
input_data_inicial = input('Digite a data dia/mês/ano: ')
textUtf8 = input_data_inicial.encode("utf-8")

hash = hashlib.md5( textUtf8 )
hexa = hash.hexdigest()

print ( hexa )
