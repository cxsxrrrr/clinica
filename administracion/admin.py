import sqlite3
class admin():

    def __init__(self):
        self.conn=sqlite3.connect("clinicamalestar.db")

    #Metodos administrador

    def addBioanalista(self, bioanalistaData):
        try:
            insertClient_st = '''INSERT INTO Bioanalistas(nombre, apellido, especialidad, telefono, email, password, cedula) VALUES (?, ?, ?, ?, ?, ?, ?)'''
            cur = self.conn.cursor()
            cur.execute(insertClient_st, bioanalistaData[:7])
            self.conn.commit()
            return "Usuario ingresado con exito"
        

        except sqlite3.IntegrityError as e:
            # Manejar errores de integridad (por ejemplo, cédula duplicada)
            if "UNIQUE constraint failed" in str(e):
                return "Error: La cédula ya está registrada."
            else:
                return f"Error de integridad en la base de datos: {e}"

        except sqlite3.Error as e:
        # Manejar otros errores generales de SQLite
            return f"Error en la base de datos: {e}"

        finally:
        # Cerrar el cursor en todos los casos (éxito o error)
            if cur:
                cur.close()

    def deleteBioanalista(self, id):
        try:
            delClient_st = f'''DELETE FROM Bioanalistas WHERE cedula={id}'''
            cur = self.conn.cursor()
            cur.execute(delClient_st)
            self.conn.commit()

            return "Paciente eliminado con exito"
        except sqlite3.Error as e:
            return f"Error en la base de datos: {e}"
        finally:
            if cur:
                cur.close()

    def busquedaBioanalista(self, cedula):
        try:

            cur = self.conn.cursor()
            cur.execute('''SELECT nombre, apellido, cedula FROM Bioanalistas
               WHERE cedula=? OR nombre=? OR apellido=?''', (cedula, cedula, cedula))
            return cur.fetchall()
        except sqlite3.Error as e:
            return f"Error en la base de datos: {e}"
        finally:
            if cur:
                cur.close()
    
    #Metodos Bioanalista
    def addPaciente(self, pacienteData):
        try:
            insertClient_st = '''INSERT INTO Pacientes(nombre, apellido, cedula, fecha_nacimiento, sexo, telefono, direccion, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
            cur = self.conn.cursor()
            cur.execute(insertClient_st, pacienteData[:8])
            self.conn.commit()
            return "Usuario ingresado con exito"
        

        except sqlite3.IntegrityError as e:
            # Manejar errores de integridad (por ejemplo, cédula duplicada)
            if "UNIQUE constraint failed" in str(e):
                return "Error: La cédula ya está registrada."
            else:
                return f"Error de integridad en la base de datos: {e}"

        except sqlite3.Error as e:
        # Manejar otros errores generales de SQLite
            return f"Error en la base de datos: {e}"

        finally:
        # Cerrar el cursor en todos los casos (éxito o error)
            if cur:
                cur.close()


        
    def deletePacientes(self, id):
        try:
            delClient_st = f'''DELETE FROM Pacientes WHERE cedula={id}'''
            cur = self.conn.cursor()
            cur.execute(delClient_st)
            self.conn.commit()

            return "Paciente eliminado con exito"
        except sqlite3.Error as e:
            return f"Error en la base de datos: {e}"
        finally:
            if cur:
                cur.close()
    
    def busquedaPacientes(self, cedula):
        try:

            cur = self.conn.cursor()
            cur.execute('''SELECT nombre, apellido, cedula FROM Pacientes 
               WHERE cedula=? OR nombre=? OR apellido=? OR sexo=?''', (cedula, cedula, cedula, cedula))
            return cur.fetchall()
        except sqlite3.Error as e:
            return f"Error en la base de datos: {e}"
        finally:
            if cur:
                cur.close()
        
    def busquedaPacientes2(self):
        try:

            cur = self.conn.cursor()
            cur.execute('''SELECT nombre, apellido, cedula, sexo, telefono, fecha_nacimiento FROM Pacientes ''')
            return cur.fetchall()
        except sqlite3.Error as e:
            return f"Error en la base de datos: {e}"
        finally:
            if cur:
                cur.close()
            
    def busquedaBioanalistas2(self):
        try:

            cur = self.conn.cursor()
            cur.execute('''SELECT nombre, apellido, cedula, especialidad, telefono FROM Bioanalistas ''')
            return cur.fetchall()
        except sqlite3.Error as e:
            return f"Error en la base de datos: {e}"
        finally:
            if cur:
                cur.close()
    
    def generarResultado(self, data):
        try:
            insertClient_st = '''INSERT INTO Resultados(id_paciente, id_bioanalista, fecha_resultado, resultado) VALUES (?, ?, ?, ?)'''
            cur = self.conn.cursor()
            cur.execute(insertClient_st, data[:4])
            self.conn.commit()
            return "Resultado ingresado con exito"      
        except sqlite3.Error as e:
        # Manejar otros errores generales de SQLite
            return f"Error en la base de datos: {e}"
        finally:
        # Cerrar el cursor en todos los casos (éxito o error)
            if cur:
                cur.close()