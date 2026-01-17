# El archivo Dockerfile se utiliza para poder construir contenedores
# Aqui escribimos todas las intrucciones necesarias para que se puedean crear los contenedores

# 1. Indicamos la imagen base del proyecto
FROM python:3.11-slim

# 2. Indicamos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos el código de la API
COPY python-api/ ./python-api/

# 4. Instalamos dependencias
RUN pip install --no-cache-dir fastapi uvicorn

# 4. Exponer puertos
EXPOSE 8000

# 5. Comando para ejecutar aplicacion
CMD ["uvicorn", "python-api.main:app", "--host", "0.0.0.0", "--port", "8000"]


