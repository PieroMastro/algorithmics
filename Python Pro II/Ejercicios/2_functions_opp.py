# 4. Corregir los errores en el programa

class My_success():
    def __init__(self,value):
        self.value_of_success = value
    def check_success(self):
        if self.value_of_success >= 4.0:
            return 'El startup fue exitoso'
        elif self.value_of_success < 4.0 and self.value_of_success >= 3.0:
            return 'El startup salió bien'
        return 'El proyecto necesita algo de trabajo'
rate = float(input('Calificación de app'))
object = My_success(rate)
print(object.check_success())

# 5. Escribir el programa. Conversión

#crear una clase Converter
class Converter():
    def __init__(self, usd):
        self.usd = usd

    def rub_to_usd(self, rub_value):
        usd_value = rub_value/self.usd
        print(round(usd_value, 2))

    def usd_to_rub(self, usd_value):
        rub_value = usd_value*self.usd
        print(round(rub_value, 2))

#solicitar 2 números – la tasa y el monto
tasa = int(input('Introduzca el tipo de cambio USD'))
monto = int(input('Introduzca la suma a intercambiar'))

#crear un objeto de la clase Converter
convertir = Converter(tasa)

#implementar la elección del tipo de cambio
opcion = int(input('1 - USD a Rublos / 2 - Rublos a USD'))
if opcion == 1:
    convertir.usd_to_rub(monto)
else: convertir.rub_to_usd(monto)