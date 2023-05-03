#generar saludo python

from datetime import datetime
from urllib.request import urlopen
import json

def formato_fecha(date):
    fecha = date.strftime('%Y-%-m-%-d-%w-%-H-%-M')
    year,month,day,dow,hour,minute = fecha.split("-")
    months = {1:"Enero", 2: "Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto",9:"Septiembre",10:"Octubre",11:"Nombiembre",12:"Diciembre"}
    dows = {1:"Lunes", 2: "Martes", 3:"Miércoles", 4:"Jueves", 5:"Viernes", 6:"Sábado", 7:"Domingo"}
    
    return f"Son las {hour} horas y {minute} minutos del {dows[int(dow)]} {day} de {months[int(month)]} de {year}."

bienvenida = "Hola! Bienvenido! " 

fecha = datetime.today()

j = urlopen("https://api.open-meteo.com/v1/forecast?latitude=40.57&longitude=-3.27&hourly=temperature_2m").read()
j_obj = json.loads(j.decode('utf-8'))
h = fecha.strftime('%-H')

temp = str(j_obj["hourly"]["temperature_2m"][int(h)])

temperatura = " La temperatura en Azuqueca es de " + temp + " grados celsius."

print(bienvenida + formato_fecha(fecha) + temperatura)





