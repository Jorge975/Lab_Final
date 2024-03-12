# Usa una imagen base de Python
FROM python:3.12.1

EXPOSE 5000

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias
COPY requirements.txt /app
RUN pip install -r requirements.txt


# Copia los archivos de la aplicación al contenedor
COPY . /app

# Comando para ejecutar la aplicación
CMD ["python", "run.py"]
