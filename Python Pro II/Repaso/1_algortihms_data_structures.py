# CICLO WHILE:
# time = int(input('¿Cuántas horas debe tomar el proyecto?'))
# while time > 8:
#     spent_time = int(input('¿Cuántas horas ya han gastado en el proyecto?'))
#     time -= spent_time
#     print('Tiempo restante: ', time)
# print('¡Menos de 1 día restante para completar el proyecto! ¡Aconsejamos que incremente la velocidad!')

# CICLO FOR:
# password = 'World_of_Code'
# data = '_1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
# for symbol in password:
#     pos = data.find(symbol) + 1
#     print('Código para símbolo', symbol, '-', pos)

# start_year = int(input('Año de creación de cuenta bancaria:'))
# end_year = int(input('Año de terminación de cuenta bancaria:'))
# amount = int(input('Monto inicial:'))
# interest_rate = int(input('Tasa de interés:'))
# for i in range(end_year - start_year):
#     amount += amount * (interest_rate / 100)
# print('Período de depósito (años):', end_year - start_year)
# print('Monto resultante:', round(amount))