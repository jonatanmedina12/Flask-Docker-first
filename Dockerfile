# Usar la imagen base de Python
FROM python:latest

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requisitos y el contenido de la aplicación al contenedor
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto que usará Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
