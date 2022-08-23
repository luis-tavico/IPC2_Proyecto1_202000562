import xml.etree.ElementTree as ET
from paciente import Paciente


class Princip:

    def __init__(self, listaPacientes):
        self.listaPacientes = listaPacientes
    
    def menuPrincipal(self):
        opcion = 0
        while opcion != 7:
            print(" ============== MENU PRINCIPAL ============== ")
            print("| 1. Cargar Archivo (.xml)                   |")
            print("| 2. Leer Paciente                           |")
            print("| 3. Leer Paciente Hasta Periodo N           |")
            print("| 4. Leer Paciente Hasta Encontrar Resultado |")
            print("| 5. Generar Archivo (.xml)                  |")
            print("| 6. Salir                                   |")
            print(" ============================================ ")
            #try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                print()
            elif opcion == 2:
                nombre = str(input("Ingrese el nombre del paciente: "))
                print("")
                pacientes = self.listaPacientes.valores()

                while pacientes != None:
                    if nombre == pacientes.paciente.getNombre():              
                        paciente = Paciente(pacientes.paciente, True)
                        paciente.ejecutar()
                        break
                    pacientes = pacientes.siguiente
                opcion = 0
                if pacientes == None:
                    print("\n¡No se encontro el paciente!\n")
            elif opcion == 3:
                nombre = str(input("Ingrese el nombre del paciente: "))
                periodo = int(input("Ingrese hasta que periodo desea ejecutar: "))
                print("")
                pacientes = self.listaPacientes.valores()

                while pacientes != None:
                    if nombre == pacientes.paciente.getNombre():              
                        pacientes.paciente.setPeriodos(periodo)
                        paciente = Paciente(pacientes.paciente, True)
                        paciente.ejecutar()
                        break
                    pacientes = pacientes.siguiente
                opcion = 0
                if pacientes == None:
                    print("\n¡No se encontro el paciente!\n")
            elif opcion == 4:
                nombre = str(input("Ingrese el nombre del paciente: "))
                print("")
                pacientes = self.listaPacientes.valores()

                while pacientes != None:
                    if nombre == pacientes.paciente.getNombre():              
                        pacientes.paciente.setPeriodos(10000)
                        paciente = Paciente(pacientes.paciente, True)
                        paciente.ejecutar()
                        break
                    pacientes = pacientes.siguiente
                opcion = 0
                if pacientes == None:
                    print("\n¡No se encontro el paciente!\n")
            elif opcion == 5:
                pacientes = self.listaPacientes.valores()

                while pacientes != None:   
                    pacientes.paciente.setPeriodos(10000)          
                    paciente = Paciente(pacientes.paciente, False)
                    paciente.ejecutar()
                    paciente.reportar()
                    pacientes = pacientes.siguiente
                print("\n¡Archivo creado exitosamente!\n")
                opcion = 0
            elif opcion == 6:
                rootPacientes = ET.Element('pacientes')
                myData = ET.tostring(rootPacientes)
                file = open("./datos.xml", "wb")
                file.write(myData)
            else:
                print("¡Ingrese una opcion valida!")