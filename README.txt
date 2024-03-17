
---# Crear un entorno de virtual

# Crear un entorno virtual:
- virtualenv venv
# Activar el entorno:
- venv/Scripts/activate
# Desactivar:
- deactivate
# En caso de tener que instalar etorno virtual:
- pip install virtualenv
- sudo pip3 install virtualenv
# Instalar requirements.txt, para obtener todos los modulos:
- pip install -r requirements_venv.txt
# También puedes crear el enviroment directamente en visual studio.

--------------------------------------------------------------------

---# CREAR ENTORNO DE DESARROLLO LOCAL + MYSQL

(Aunque funciona localmente no lo hace en Jenkins)

# Crear el contenedor con docker-compose
- docker-compose -f docker/docker-compose-mysql.yml up
# Ejecutar mysql
- docker exec -it docker-db-1 mysql -u root -p


---------------------------------------------------------------------

---# CREAR ENTORNO DE DESARROLLO LOCAL + POSTGRES

# Crear el contenedor con docker-compose
- docker-compose -f docker/docker-compose-postgres.yml up
# Ejecutar postgres sin entrar en la base de datos
- docker exec -it docker-db-1 psql -U user -d postgres
# Ejecutar postgres entrando en la base de datos
- docker exec -it docker-db-1 psql -U user miproyecto

---------------------------------------------------------------------

--# INSTALAR MYSQL CON ANSIBLE

# Para instalar correctamente Ansible, buscamos "Turn Windows features on or  off" y activamos la característica "Windows Subsystem for Linux", seguido de la instalacion de Ubuntu.
# Instalamos ansible en la terminal wsl en visual//en terminal shell falla:
- sudo apt install ansible
# Se puede instalar Ubuntu desde Microsoft Store o desde el propio cmd
# Creamos un nuevo terminal wsl en VisualStudio
# Instalamos mysql con ansible:
- ansible-playbook playbook_sql.yml
# Ejecutar mysql:
mysql -u root -p

# Es probable que debas dar permisos para que funcione:
GRANT ALL PRIVILEGES ON miproyecto.* TO 'root'@'127.0.0.1';
FLUSH PRIVILEGES;

# Importar base de datos desde wsl:
- mysql -u root -p miproyecto < miproyecto_backup.sql

# Para que funcione correctamente el run.py debes de haber accedido a mysql y activado el venv.
---------------------------------------------------------------------

--# Test de cobertura y pruebas unitarias

# Para hacer pruebas unitarias usamos pytest
# Para ejecutar test:
- pytest
# Para los test de cobertura:
-pytest --cov=tests --cov=app
-coverage report -m

-----------------------------------------------------------------------
--# Para conectarse con GitHub
-git remote add origin https://github.com/Jorge975/Lab_Final.git

#Modificar datos
-git init

-git add .

-git commit -m "first commit"

-git push -u origin main
