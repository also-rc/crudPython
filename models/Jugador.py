class Jugador(object):
    id:None
    nombre:None
    apellido:None
    edad:None
    salario:None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setSalario(self, salario):
        self.salario = salario

    def getSalario(self):
        return self.salario
