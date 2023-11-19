
# Proyecto Final 
-Fernando Ruiz Velasco Hernandez

Este proyecto es un catálogo de productos con convertidor de moneda con la posibilidad de ser utilizado por medio de API o CRUD. Utilizando FastAPI y SQLAlchemy.




# Principios de SOLID

1. SRP: Cada módulo clase o función tienen una sola responsabilidad como lo es el modulo de Crud.py
2. OCP: El código está hecho de tal manera que puede ser extendido sin tener la necesidad de que se edite el código base.
3. LSP: Este se comple con el uso de un ORM con uso de los modelos
4. ISP: El uso de FastAPI nos permite generar diferentes rutas para funciones diferentes del sistema.


# Principios de Diseño

1. Singleton Pattern: La conexión de la base de datos asegura que solo exista una instancia de la conexión creada.
2. MVC: Está generado con un enfoque de Modelo Vista Controlador con los modelos, los endpoints de API o CRUD y las controladores.


# Características Arquitectónicas Actuales del Sistema

El sistema está diseñado tomando en cuenta la modularidad, escalabilidad, mantenibilidad y rendimiento. Esto organizando el software en módulos, además de separar los por rutas, modelos y lógica empresarial. De la misma forma el uso de FastAPI y el ORM, permite que el sistema se escale sin generar problemas con los otros módulos que puedan existir. También haciendo caso a los principios de limpieza y organización de código de SOLID se genera un software fácil de mantener.

# Migración a Microservicios

La migración a microservicios puede tener muchas ventajas a comparación de una arquitectura monolítica, como lo puede ser la escalabilidad, mantenimiento y agilidad. Aun con los beneficios mencionados, también la migración tiene sus propios desafíos, como lo puede ser la gestión y la necesidad de coordinar múltiples servicios. 


# Instalación

- Instalación de dependencias
pip install -r requiments.txt

- Correr la aplicación
py src/app.py

- Correr Pruebas
pytest tests

Nota: Pueden utilizar la coleccion de insomnia para probar los endpoints del api. 



# Video:
https://drive.google.com/file/d/1eESWMxwQwquuiekidkN5FrwYdHnswbmq/view?usp=sharing
