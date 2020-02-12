from connec2 import connectionDB

class Dao(object):
    sentencia:None
    myCdb= connectionDB.ConnectionDB()

    def insert(self, Jugador):
        preSentencia = """INSERT INTO jugador (id,nombre,apellido,edad,salario) VALUES (%s,%s,%s,%s,%s) """
        toInsert = (Jugador.getId(), Jugador.getNombre(), Jugador.getApellido(), Jugador.getEdad(), Jugador.getSalario())
        self.myCdb.execute(preSentencia,toInsert)

    def update(self, Jugador):
        preSentencia = """UPDATE jugador SET nombre = %s, apellido = %s, edad = %s, salario = %s WHERE id = %s"""
        toUpdate = (Jugador.getNombre(), Jugador.getApellido(), Jugador.getEdad(), Jugador.getSalario(), Jugador.getId())
        self.myCdb.execute(preSentencia,toUpdate)

    def delete(self, Jugador):
        preSentencia = """DELETE FROM jugador WHERE id = %s"""
        toDelete = (Jugador.getId(),)
        self.myCdb.execute(preSentencia,toDelete)

    def readOne(self, Jugador):
        preSentencia = """SELECT * FROM jugador WHERE id = %s """
        toReadOne = (Jugador.getId(),)
        self.myCdb.executeOneQuery(preSentencia,toReadOne)

    def readAll(self):
        preSentencia = """SELECT * FROM jugador """
        #toRead = ('jugador')
        self.myCdb.executeQuery(preSentencia)



