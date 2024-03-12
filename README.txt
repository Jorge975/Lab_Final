

# Crear un entorno virtual:
virutalenv venv

# Activar el entorno:
venv/Scripts/activate

# Desactivar:
deactivate

# En caso de tener que instalar etorno virtual:
pip install virtualenv
sudo pip3 install virtualenv

# Instalar requirements.txt, para obtener todos los modulos:
pip install -r requirements.txt

# También puedes crear el enviroment en visual studio

# Para instalar correctamente Ansible, buscamos "Turn Windows features on or  off" y activamos la característica "Windows Subsystem for Linux", seguido de la instalacion de Ubuntu.

# Instalamos ansible en la terminal wsl en visual//en terminal shell falla:
sudo apt install ansible

# Se puede instalar Ubuntu desde Microsoft Store o desde el propio cmd

# Creamos un nuevo terminal wsl en VisualStudio

# Instalamos mysql con ansible:
ansible-playbook playbook_sql.yml

# Para entrar en mysql:
mysql -u root -p

# Es probable que debas dar permisos para que funcione:
GRANT ALL PRIVILEGES ON miproyecto.* TO 'root'@'127.0.0.1';
FLUSH PRIVILEGES;

# Importar base de datos desde wsl:
mysql -u root -p miproyecto < miproyecto_backup.sql

# table
CREATE TABLE data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

# Para que funcione correctamente el run.py debes de haber accedido a mysql y activado el venv.

# Para hacer pytest, puede que sea necesario

pip install pytest coverage


# Para ejecutar test:

pytest

# Para el coverage:

pytest --cov=app

pytest --cov=tests --cov=app
coverage report -m

# Para conectarse con GitHub
https://github.com/Jorge975/Final_Lab.git
