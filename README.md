# Mod_Concurso_Microrelatos
Espacio para mantener los archivos relacionados con el desarrollo del Módulo del SISCAIR-USB para gestionar los Tweets generados por el Concurso de Microrelatos

instrucciones:

0) instalar "pip" para manejar versiones de todo lo que se necesite

1) instalar django (ultima version estable)con el siguiente comando:
	"sudo pip install Django"
2) instalar postgresql (manejador de bases de datos).

3) convertirse en usuario postgres: <sudo -i -u postgres>

4) crear usuario microrelatos: <createuser -s -P microrelatos>

5) introducir clave*** <microrelatospass>

6) Crear base de datos (como usuario postgres) : <createdb microrelatosdb>

7) volver a ser superusuario: <logout>

8) Instalar psycopg2 (interfaz entre python y postgresql) de la siguiente manera: <sudo apt-get install python-psycopg2>



