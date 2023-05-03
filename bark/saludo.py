#generar saludo python

from datetime import datetime

def formato_fecha(date):
    fecha = date.strftime('%Y-%-m-%-d-%w-%-H-%-M')
    year,month,day,dow,hour,minute = fecha.split("-")
    months = {1:"Enero", 2: "Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto",9:"Septiembre",10:"Octubre",11:"Nombiembre",12:"Diciembre"}
    dows = {1:"Lunes", 2: "Martes", 3:"Miércoles", 4:"Jueves", 5:"Viernes", 6:"Sábado", 7:"Domingo"}
    
    return f"Son las {hour} horas y {minute} minutos del {dows[int(dow)]} {day} de {months[int(month)]} de {year}"


#print(datetime.today().strftime('%Y-%m-%d %H:%M'))
#print(datetime.today().strftime('Son las %H horas y %M minutos del %A %d de %B de %Y'))

bienvenida = "Hola! " 
fecha = datetime.today()
print(bienvenida + formato_fecha(fecha))
