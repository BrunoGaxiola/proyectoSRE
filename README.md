
# Proyecto Integrador: Patrones de Diseño
**Por: Bruno Gaxiola Gonzalez A01253874**

---

## Simulación de elaboración de citas con la Secretaría de Relaciones Exteriores.

Este es un proyecto en Python que simula el proceso para agendar una cita con la Secretaría de Relaciones Exteriores. El caso de uso actual es el agendar una cita para una renovación con documento de tu pasaporte. Esta representación solo cubre agendar citas en las diferentes oficinas del estado de Sonora. 

---
## Justificación

Agendar una cita para renovar tu pasaporte depende de un proceso que para el ciudadano promedio puede no interesarle. Al ciudadano puede solo importarle hacer el proceso el día y hora que desee, pero es un proceso más complejo en el gobierno para asegurar que todas las personas que quieren renovar su pasaporte no se queden sin cita. Es por esto que se necesita un poco más de estructura en el proceso, como la declaración de observadores del proceso y otros comandos, así como una fachada simplificada para el ciudadano.

---

## Patrones de Diseño 

1. **Builder**: Builder es un patrón creacional que permite extraer el proceso de construcción de una instancia fuera de su clase, con la finalidad de crear una clase exclusiva para construir la instancia.

2. **Command**: Command se trata de una interfaz para ejecutar comandos. Esto permite separar los objetos que solicitan una operación, de quienes la realizan.

3. **Observer**: Observer ofrece un acercamiento para notificar a sus suscriptores cuando ocurran ciertos eventos en el sistema en vez de notificar por cada acción.

4. **Facade**: Facade proporciona una interfaz un poco más simplificada para utilizar varias subclases complejas, permitiendo solo incluir las funcionalidades que le importan al usuario sin acceder a los que manejan la lógica interna.

---
## Implementación de los Patrones.

- La Clase Cita tiene su respectivo constructor y un método para mostrar la cita generada. Sin embargo, también se cuenta con su clase CitaBuilder, que tiene métodos tipo 'set' para los atributos de la cita y un método build() que llama al constructor del objeto Cita.

- Se cuenta con un observador, que es inicializado con una interfaz abstracta con el método actualizar(). En la simulación, se cuenta con el observador ServicioCorreo(), que notifica que el correo con la información de la cita se está enviando.

- Se cuenta con una clase abstracta que representa el comando con el método ejecutar(). La clase AgendarCitaCommand hereda de ella, inicializa su el builder y observadores, y realiza el comando de contruir la cita y notificar al observador.

- El Facade SistemaCitasFacade registra al observador, utiliza el builder de CitaBuilder para construir la cita y ejecuta el comando para programarla.

---
## Diagrama UML.

[![](https://mermaid.ink/img/pako:eNq9VMGOmzAQ_RXkE9UGBISExIoital67WFvFVI0MRPiXcCRMat20_x7bZPdhQQi7aU-GHv8_ObxPPaJMJEhoYQVUNffOeQSyrRydLMRZ8MVOKc2YprnsEYeqVMr2QsKKVHchIsmB3kT3SM7AHUyUNgLi4JfUzw4pdABkO6Xzso5ra41fmt4kaH8L1IfnBrV1pC7ptPKOgpuYDad237uQ60E1_b3gVaVa_tx4M6E3Mv6oG8_dzXKF8hEz7bVilcK5R4YrtddQmCqgYK_ao1MU2rmF8GzQeZHzcsZFxv71132T9FsRAlVJq5rcFQhPiFrVFsso6Rfc6wykIZU85sE_aLZtVaO-Oo54t01rKlT8Fp9WsKj3oQlmAT1D2CQYV_C_RQSc27vxPYD5-phL-OlWPSVMibLreld3_eHZXUqYfXX96_Or8V0D8OCbo28ADvX0fPWnfobsP4N0DN6BPehsoUN2GhgY7pG4F1WMiG55BmhSjY4ISXKEsyU2ONJiTpgiSmheqgzPKckrc56zxGqX0KUb9ukaPIDoXsoaj1rjub1uDyt7xAtEeVGNJUidBolloPQE_lNaDQP_WA-W8TzWRDrwXxC_hDqzRM_WCZRkITTMF7M4ul5Ql5t1tAPg2gZLpI4DhZJFC6j8z88J8n6?type=png)](https://mermaid.live/edit#pako:eNq9VMGOmzAQ_RXkE9UGBISExIoital67WFvFVI0MRPiXcCRMat20_x7bZPdhQQi7aU-GHv8_ObxPPaJMJEhoYQVUNffOeQSyrRydLMRZ8MVOKc2YprnsEYeqVMr2QsKKVHchIsmB3kT3SM7AHUyUNgLi4JfUzw4pdABkO6Xzso5ra41fmt4kaH8L1IfnBrV1pC7ptPKOgpuYDad237uQ60E1_b3gVaVa_tx4M6E3Mv6oG8_dzXKF8hEz7bVilcK5R4YrtddQmCqgYK_ao1MU2rmF8GzQeZHzcsZFxv71132T9FsRAlVJq5rcFQhPiFrVFsso6Rfc6wykIZU85sE_aLZtVaO-Oo54t01rKlT8Fp9WsKj3oQlmAT1D2CQYV_C_RQSc27vxPYD5-phL-OlWPSVMibLreld3_eHZXUqYfXX96_Or8V0D8OCbo28ADvX0fPWnfobsP4N0DN6BPehsoUN2GhgY7pG4F1WMiG55BmhSjY4ISXKEsyU2ONJiTpgiSmheqgzPKckrc56zxGqX0KUb9ukaPIDoXsoaj1rjub1uDyt7xAtEeVGNJUidBolloPQE_lNaDQP_WA-W8TzWRDrwXxC_hDqzRM_WCZRkITTMF7M4ul5Ql5t1tAPg2gZLpI4DhZJFC6j8z88J8n6)
