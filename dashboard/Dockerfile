# Imagen base
FROM python:3.9

# Configurar directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY ./api.py ./requirements.txt /app/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de la API
EXPOSE 8000

# Comando para iniciar la API
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
