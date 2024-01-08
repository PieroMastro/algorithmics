def rise_pressure(pressure):
    print('Presion actual', pressure)
    answer = input('Aumentar la presion? (si / no)')
    if answer == 'si':
        pressure += 5
        rise_pressure(pressure)

rise_pressure(5)