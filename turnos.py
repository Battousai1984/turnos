print('*************************')
print('*Sistema de turnos PyTurn*')
print('*************************')
usuario1 = 'Luca'
password1 = '123456'
usuario2 = 'Violeta'
password2 = '987654'  
usuario = input ('Ingrese su usario: ')
password = input ('Ingrese la contraseña: ')
médico1 = 'Daniel Foreman'
médico2 = 'Cristina Perez'
if (usuario == usuario1 and password == password1) or (usuario == usuario2 and password == password2):
    print('Bienvenido al sistema de turnos médicos '+ usuario)
    if usuario == 'Luca':
        médico = médico1
    else: 
        médico = médico2
    print('Su médico es: '+médico)
else: 
    print('Usted no tiene acceso al sistema de turnos')
    print('Comuníquese a lcdtm@lpqtp.com')