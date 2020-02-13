import psycopg2

class ConnectionDB(object):
    __instance = None
    conn = None


    """Constructor """
    def __init__(self):
        print('Connecting to the PostgreSQL database...')
        self.conn = psycopg2.connect(host="localhost", database="seleccion", user="postgres", password="12334")

    #####SINGLETON JAVESCO#### It'll be better.
    def __new__(cls):
        if ConnectionDB.__instance is None:
            ConnectionDB.__instance = object.__new__(cls)

        return ConnectionDB.__instance


    #Sentencias de actualización
    def execute(self,preSentencia,toInsert):
        try:

            # create a cursor
            cur = self.conn.cursor()

            # execute a statement
            print('Haciendo cositas...')
            cur.execute(preSentencia, toInsert)


            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.commit()
                print('Database connection closed.')

    def executeOne(self, preSentencia,toRead):
        try:
            # create a cursor
            cur = self.conn.cursor()
            # execute a statement; NOTA MENTAL: Volverlo una lista de objetos según lo que necesite <3 NO OLVIDAR
            print('Seleccionando cositas...')

            if preSentencia.find("WHERE") >= 1:
                cur.execute(preSentencia, toRead)
                registros = cur.fetchall()

                for row in registros:
                    print("ID:", row[0])
                    print("Nombre:", row[1])
                    print("Apellido:", row[2])
                    print("Edad:", row[3])
                    print("Salario:", row[4])

            else:
                cur.execute(toRead)
                registros = cur.fetchall()

                for row in registros:
                    print("ID:", row[0])
                    print("Nombre:", row[1])
                    print("Apellido:", row[2])
                    print("Edad:", row[3])
                    print("Salario:", row[4])

            cur.close()
            # close the communication with the PostgreSQL
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                print('Database connection closed.')