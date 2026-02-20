FROM python:3.11-slim

WORKDIR /app

# Copy app code (see .dockerignore for exclusions)
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Ensure Python finds the 'core' package
ENV PYTHONPATH=/app

# Interactive: press ENTER to shutdown
CMD [ "python", "main.py" ]