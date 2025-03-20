


import datetime

data = datetime.datetime.now()
agr = data.strftime("%x")

hora = data.strftime("%X")

print("Data: ", agr)
print("Horas: ", hora)