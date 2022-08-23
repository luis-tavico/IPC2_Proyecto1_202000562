import xml.etree.ElementTree as ET
from paciente import Paciente
from cargarArchivo import CargarArchivo

class MenuPrincipal:

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
            try: 
                opcion = int(input("Ingrese una opcion: "))
                if opcion == 1:
                    ruta = input("Ingrese la ruta del archivo:\n")
                    if ruta != "":
                        CargarArchivo(ruta, self.listaPacientes)
                elif opcion == 2:
                    if self.listaPacientes.longitud() > 0:
                        nombre = str(input("Ingrese el nombre del paciente: "))
                        print("")                  
                        pacientes = self.listaPacientes.valores()

                        while pacientes != None:
                            if nombre == pacientes.paciente.getNombre():              
                                paciente = Paciente(pacientes.paciente, True)
                                paciente.ejecutar()
                                break
                            pacientes = pacientes.siguiente
                        if pacientes == None:
                            print("\n¡No se encontro el paciente!\n")
                    else:
                        print("\n¡No se han ingresado pacientes aun!\n")
                    opcion = 0
                elif opcion == 3:
                    if self.listaPacientes.longitud() > 0:
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
                        if pacientes == None:
                            print("\n¡No se encontro el paciente!\n")
                    else:
                        print("\n¡No se han ingresado pacientes aun!\n")
                    opcion = 0
                elif opcion == 4:
                    if self.listaPacientes.longitud() > 0:
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
                        if pacientes == None:
                            print("\n¡No se encontro el paciente!\n")
                    else:
                        print("\n¡No se han ingresado pacientes aun!\n")
                    opcion = 0
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
            except ValueError:
                print("\n¡Solo ingrese numeros!\n")
            except FileNotFoundError:
                print("\n¡No se encontro el archivo!\n")
            except SyntaxError:
                print("\n¡Error!, ¡No se pudo leer el archivo!\nVerifique la extension del archivo o que este bien escrito\n")