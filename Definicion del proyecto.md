# SIPREU (Sistema de Preorizacion en Urgencias)

# Introducción

Los servicios de urgencias hospitalarias suelen enfrentar problemas relacionados con la saturación de pacientes, largos tiempos de espera y dificultades para priorizar correctamente los casos más críticos. 

El proceso de triage es fundamental para clasificar a los pacientes según la gravedad de su condición, permitiendo que aquellos con mayor riesgo reciban atención inmediata.
Sin embargo, en muchos hospitales este proceso todavía depende completamente de evaluaciones manuales, lo que puede generar errores humanos, demoras en la atención y falta de estandarización en la clasificación de los pacientes.

El presente proyecto propone el diseño de una aplicación informática que permita optimizar el proceso de triage mediante el registro digital de pacientes, la evaluación de síntomas y signos vitales, y la priorización automática de los casos de acuerdo con su nivel de urgencia.

# Planteamiento del problema

En los servicios de urgencias hospitalarias, la gran cantidad de pacientes que llegan diariamente puede dificultar la correcta priorización de la atención médica.
Cuando el triage no se realiza de manera eficiente, los pacientes críticos pueden experimentar retrasos en su atención, lo que puede poner en riesgo su vida.
Entre los principales problemas identificados se encuentran:
•	Procesos manuales de registro de paciente.

•	Falta de herramientas tecnológicas para apoyar la toma de decisiones.

•	Saturación del personal médico.

•	Tiempos prolongados de espera en urgencias.

Por lo tanto, surge la necesidad de desarrollar una herramienta tecnológica que ayude a optimizar el proceso de clasificación de pacientes en urgencias.

# Objetivos

## Objetivo general

Diseñar el modelado o la estructura de una aplicación informática que optimice el proceso de triage en servicios de urgencias mediante la clasificación automatizada de pacientes según la gravedad de su condición.

## Objetivos específicos

•	Analizar el proceso actual de triage en los servicios de urgencias.

•	Identificar los requisitos funcionales y no funcionales del sistema.

•	Diseñar los modelos del sistema utilizando diagramas UML (Unified Modeling Language o Lenguaje Unificado de Modelado).

•	Proponer prototipos de interfaz que faciliten el uso del sistema por parte del personal médico.

# Justificación

La implrementación de herramientas tecnologicas en los sistemas de salud da paso a una mejora en los procesos clinicos y administrativos haciendolos mas eficientes. Un sistema de apoyo para el triage puede llegar a recudir los tiempos de espera, mejorar la priorizacion de pacientes y la optimizacion de los recursos hopitalarios

Este proyecto lo que busca es aplicar los principios de ingenieria de software para diseñar una solucion que aporte en el trabajo del personal medico y mejore la calida del servicio en los centros de urgencias

# Alcance del proyecto

El proyecto se enfoca en el análisis y diseño de una aplicación de apoyo al triage hospitalario. No incluye la implementación del software ni el desarrollo de código, sino el diseño conceptual del sistema, sus funcionalidades, modelos y prototipos.
El sistema permitirá:

•	Registrar pacientes que ingresan a urgencias.

•	Registrar síntomas y signos vitales.

•	Clasificar pacientes según niveles de prioridad.

•	Mostrar una lista priorizada de pacientes para atención médica.

# Usuarios del sistema

Los principales usuarios del sistema serán:

Enfermeros de triage Responsables de registrar la información inicial del paciente y evaluar sus signos vitales.

Médicos Encargados de consultar la lista priorizada de pacientes y atender los casos más urgentes.

Personal administrativo Responsable del registro inicial de los pacientes en el sistema.

# Requisitos del sistema
Lógica del algoritmo de triage

El sistema calculará la prioridad del paciente mediante una puntuación basada en signos vitales y síntomas.

Proceso:

Registrar signos vitales.

Evaluar síntomas críticos.

Asignar puntaje de gravedad.

Clasificar el nivel de triage.

Ejemplo de puntuación:

Condición	Puntaje
Frecuencia cardiaca muy alta	+3
Presión arterial muy baja	+3
Dolor severo	+2
Dificultad respiratoria	+4

Clasificación final:

0 – 2 → Azul (No urgente)

3 – 4 → Verde (Poco urgente)

5 – 6 → Amarillo (Urgente)

7 – 8 → Naranja (Muy urgente)

9+ → Rojo (Emergencia)

## Requisitos funcionales

RF1. El sistema debe permitir registrar pacientes.

RF2. El sistema debe permitir registrar signos vitales del paciente.

RF3. El sistema debe permitir registrar síntomas reportados.

RF4. El sistema debe clasificar automáticamente a los pacientes según su nivel de urgencia.

RF5. El sistema debe mostrar una lista de pacientes priorizados.

RF6. El sistema debe permitir actualizar el estado del paciente.

## Requisitos no funcionales

RNF1. El sistema debe ser fácil de usar para el personal médico.

RNF2. El sistema debe garantizar la seguridad de los datos de los pacientes.

RNF3. El sistema debe responder rápidamente ante consultas del usuario.

RNF4. El sistema debe funcionar en computadores del hospital o tablets clínicas.


# Historias de usuario

## Historia de usuario 1

Como enfermero de triage quiero registrar los signos vitales del paciente para determinar su nivel de urgencia.

## Historia de usuario 2

Como médico quiero ver una lista de pacientes ordenada por prioridad para atender primero los casos más críticos.

## Historia de usuario 3

Como personal administrativo quiero registrar los datos básicos del paciente para iniciar su proceso de atención.


# Metodología de desarrollo

Para el desarrollo del sistema se propone utilizar una metodología ágil, ya que permite adaptarse a cambios en los requisitos y desarrollar el sistema de forma iterativa.

El desarrollo puede organizarse en ciclos de trabajo donde se diseñen, prueben y mejoren progresivamente las funcionalidades del sistema.


# Conclusiones

El diseño de una aplicación de apoyo para el proceso de triage puede contribuir significativamente a mejorar la gestión de pacientes en los servicios de urgencias. Mediante la digitalización del registro de pacientes y la priorización automatizada de casos, es posible optimizar los tiempos de atención y apoyar la toma de decisiones del personal médico.

Este proyecto demuestra cómo los principios de la ingeniería de software pueden aplicarse para diseñar soluciones tecnológicas orientadas a resolver problemas reales en el sector de la salud.


# Diagramas UML (propuesto)

## Diagrama de Casos de uso

<img width="1920" height="1080" alt="Tablero de Equipo de Diagrama de Caso de Uso en Estilo de Bloques de Color Espaciados en Amarillo Rosa y Verde" src="https://github.com/user-attachments/assets/4be6cc8d-e1f2-458f-87de-5a35bc09e79a" />


## Mockups (protopipos de interfaz)

### Pantalla 1: Registro del paciente

![Documento A4 Ficha de Registro Tabla Minimalista Sencillo Beige](https://github.com/user-attachments/assets/b70c1651-5b8b-482c-b041-97bf940e7b76)

### Pantalla 2: Evaluación de Triage

![Green Gray Simple Survey Form A4 Document](https://github.com/user-attachments/assets/da671b1e-ac14-4785-8ec6-0d7f0e789a5c)

### Pantalla 3: Lista de Pacientes Priorizados

![Brown White Simple Weekly Personal Growth Tracker List](https://github.com/user-attachments/assets/49687be1-9a79-4739-8c2d-6a942208d757)

### Pantalla 4: Panel del Médico

![Green Gray Simple Survey Form A4 Document (1)](https://github.com/user-attachments/assets/dab214e0-d7c7-402b-91af-57eedf88ad11)



# Soluciones 

1.Con un simulador de una sala de emergencias buscamos preparar al personal de salud y Instituciones e salud para distintos casos de emergencias en los que se haga un correcto manejo de este, clasificando a los pacientes según su edad, síntomas y la gravedad del caso presentado, con esto se busca fácilitar de forma más clara los procesos médicos que se podrán tomar en cuenta dependiendo del grado de emergencia.

## UML (Investigación)
¿Qué es ?
Es un estándar para visualizar, especificar, construir y documentar los componentes de un sistema de software. Son unas reglas gráficas para representar cómo se estructura y se comporta un sistema. Para la clasificación de los diagramas existen varios tipos y se agrupan en dos categorías principales: 

Diagrama Estructural : Se centran en que elementos componen el sistema (Parte estática).
Clases: Muestra las clases , sus atributos, métodos y cómo se relacionan entre sí.
Objetos: Representa una instancia específica de las clases en un momento determinado.
Componentes : Organización de módulos o librerías. 
Despliegue : Muestra el hardware y el software donde se instalará el sistema.  

Diagrama de Comportamiento :  Este se centra en cómo reacciona o evoluciona el sistema ante eventos (Parte dinámica )
 Casos de uso : Describe las funciones del sistema desde el punto de vista del usuario
Interacción: Visión global de interacciones.
Estados : Muestra el ciclo de vida de un objeto y cómo cambia según los eventos.

Diagrama de Casos de uso

Se utiliza durante el análisis de requisitos para representar que hace el sistema, sin entrar en detalles técnicos de cómo lo hace.

 Elementos principales:

Actor: Es cualquier entidad externa que interactúa con el sistema (usuario, otro software, hardware).
Caso de Uso: Es una función específica que el actor puede realizar (ej. "Iniciar sesión", "Consultar saldo").
Límite del Sistema: Un recuadro que encierra los casos de uso para separar lo que está dentro de la aplicación de lo que es externo.

Diagrama de Interacción

 Es un tipo de diagrama de comportamiento que se enfoca en el intercambio de mensajes entre los objetos para lograr un objetivo funcional. Los dos más importantes son:
Diagrama de secuencia
Diagrama de comunicación


