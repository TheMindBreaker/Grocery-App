
# Proyecto Final 
-Fernando Ruiz Velasco Hernandez

Este proyecto es un catalogo de productos con convertidor de moneda con la posibilidad de ser utilizado por medio de API o CRUD. Utilizando FastAPI y SQLAlchemy.




# Principios de SOLID

1. SRP: Cada modulo clase o funcion tienen una sola responsabilidad como lo es el modulo de Crud.py
2. OCP: El codigo esta hecho de tal manera que puede ser extendido sin tener la necesidad que se edite el codigo base.
3. LSP: Este se comple con el uso de un ORM con uso de los modelos
4. ISP: El uso de FastAPI nos permite generar diferentes rutas para funciones diferentes del sistema.


# Principios de Diseño

1. Singleton Pattern: La coneccion de la base de datos asegura que solo exista una instancia de la connection creada.
2. MVC: Esta generado con un enfoque de Modelo Vista Controlador con los modelos, los enpoints de API o CRUD y las controladores.


# 5 puntos estructurales del proyecto.

El sistema esta diseñado tomando en cuenta la modularidad, escalabilidad, mantenimiento simple, rendimiento. Esto organizando el software en modulos, ademas de separar los por rutas, modelos y logica empresarial. De misma forma el uso de FastAPI y el ORM, permite que el sistema se escale sin generar problemas con los otros modulos que puedan existir. Tambien haciendo caso a los principios de limpieza y organizacion de codigo de SOLID se genera un software facil de mantener.


# Instalacion

- Instalacion
pip install -r requiments.txt

- Correr la aplicacion
py src/app.py

- Correr Pruebas
pytest tests



# Video:
 https://drive.google.com/file/d/19n_nec6PFZdmzpwSNwQ1R1oiyApkpa6A/view?usp=sharing