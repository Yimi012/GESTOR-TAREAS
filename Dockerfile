# Imagen base de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos del proyecto
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que usa Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
