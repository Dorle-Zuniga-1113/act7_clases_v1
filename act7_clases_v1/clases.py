print("introducción a clases")
class animal:
    edad=3
    raza= "pug"
    comida="croquetas"
    def come(self):
        print("el perro come "+self.comida)
        return
print(animal) 
print("creando el obj de la clase animal")
perro= animal()

print(f"Edad del perro {perro.edad}") 
print(f"Edad del perro {perro.raza}") 
perro.come()


