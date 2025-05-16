# Bruno Gaxiola Gonzalez A01253874
# Proyecto Integrador Patrones de Diseño
# Programa de simulación del proceso de agendar citas para el pasaporte.

from abc import ABC, abstractmethod
import uuid
import datetime
import re

# Oficinas disponibles en el estado de Sonora.
OFICINAS_SONORA = [
    "SONORA", "OME AGUA PRIETA", "OME CD OBREGÓN", "OME GUAYMAS", "OME NOGALES", "OME NAVOJOA", "OME SAN LUIS RÍO COLORADO",
    "OME CABORCA", "OME PUERTO PEÑASCO"
]

# Patrón Creacional: Builder
# Se utiliza el patrón Builder para crear la estructura de las citas.

# Clase Cita.
class Cita:
    def __init__(self, curp, correo, lugar, fecha, folio):
        self.curp = curp
        self.correo = correo
        self.lugar = lugar
        self.fecha = fecha
        self.folio = folio
    
    # Mostrar la cita.
    def mostrar(self):
        return f"""\nCita Confirmada:
    CURP: {self.curp}
    Correo: {self.correo}
    Lugar: {self.lugar}
    Fecha: {self.fecha.strftime('%d/%m/%Y')}
    Folio: {self.folio}

    Se te proporcionará al correo ingresado el folio de la cita, un formulario para que lo llene, 
    la hoja para realizar el pago de derechos y un tríptico con toda la documentación que necesita presentar al
    llegar a su cita. ¡Que tenga un excelente día!

    """
    
# Clase CitaBuilder para construir la cita, con sus métodos para establecerla.
class CitaBuilder:
    def __init__(self):
        self.curp = None
        self.correo = None
        self.lugar = None
        self.fecha = None

    def set_curp(self, curp):
        self.curp = curp
        return self

    def set_correo(self, correo):
        self.correo = correo
        return self

    def set_lugar(self, lugar):
        self.lugar = lugar
        return self

    def set_fecha(self, fecha):
        self.fecha = fecha
        return self

    def build(self):
        folio = str(uuid.uuid4()).split("-")[0].upper()
        return Cita(self.curp, self.correo, self.lugar, self.fecha, folio)

# Patrón de Comportamiento: Observer.
# Se utiliza el patrón Observer para informar el estado de la generación de la cita.
class Observador(ABC):
    @abstractmethod
    def actualizar(self, cita):
        pass

class ServicioCorreo(Observador):
    def actualizar(self, cita):
        print(f"\nEnviando correo a {cita.correo} con los datos de la cita...")
        print(cita.mostrar())

# Patrón de comportamiento: Command
# Se utiliza el patrón Command para llamar la contrucción de la cita y llamar a actualizar al observador.
class ComandoCita(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

class AgendarCitaCommand(ComandoCita):
    def __init__(self, builder, observadores):
        self.builder = builder
        self.observadores = observadores

    def ejecutar(self):
        cita = self.builder.build()
        for obs in self.observadores:
            obs.actualizar(cita)

# Patrón Estructural: Facade
# Se utiliza Facade para enmascarar el funcionamiento interno del proceso.
class SistemaCitasFacade:
    def __init__(self):
        self.observadores = []

    def registrar_observador(self, observador):
        self.observadores.append(observador)

    def solicitar_cita(self, curp, correo, lugar, dia, mes):
        try:
            fecha = datetime.date(2025, mes, dia)
        except ValueError:
            print("Fecha inválida. Asegúrate de que el día y mes sean correctos.")
            return

        builder = CitaBuilder() \
            .set_curp(curp) \
            .set_correo(correo) \
            .set_lugar(lugar) \
            .set_fecha(fecha)

        comando = AgendarCitaCommand(builder, self.observadores)
        comando.ejecutar()

# Función para checar si el correo es válido.
def correo_valido(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(patron, correo) is not None

# Programa principal Main.
if __name__ == "__main__":
    sistema = SistemaCitasFacade()
    sistema.registrar_observador(ServicioCorreo())
    print("Bienvenido al Portal para agendar cita a la Secretaría de Relaciones Exteriores en Sonora.\n")
    print("Oficinas Disponibles:")
    for oficina in OFICINAS_SONORA:
        print(oficina)
    print("\n")

    curp = input("Introduce tu CURP: ").strip().upper()
    while not curp:
        print("No puedes mandar una CURP vacía. Introduzca tu CURP correctamente.")
        curp = input("Introduce tu CURP: ")

    correo = input("Introduce tu correo: ")
    while not correo_valido(correo):
        print("Correo inválido. Intenta de nuevo.")
        correo = input("Introduce tu correo: ")
    
    lugar = input("Oficina deseada para la cita: ").strip().upper()
    while lugar not in OFICINAS_SONORA:
        print("Por favor, introduzca una oficina disponible.")
        lugar = input("Oficina deseada para la cita: ").strip().upper()

    try:
        dia = int(input("Día deseado (1-31): "))
        mes = int(input("Mes deseado (1-12): "))
    except ValueError:
        print("Entrada inválida. El día y mes deben ser números.")
    else:
        sistema.solicitar_cita(curp, correo, lugar, dia, mes)

