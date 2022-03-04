alumnos=int(input("Cuantos alumnos son"))
if alumnos >=100 :
    print(65*alumnos)
    print("El alumno debe pagar "+ (65))
elif alumnos >=50 and alumnos<=99:
    print(70*alumnos)
    print("El alumno debe pagar "+ (70))
elif alumnos >=30 and alumnos<=49:
    print(95*alumnos)
    print("El alumno debe pagar "+ (95))
elif alumnos <=30:
    print(alumnos*4000)
    print("El alumno debe pagar "+ (4000))