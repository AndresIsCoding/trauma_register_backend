import os
import sys
from waitress import serve
from django.core.wsgi import get_wsgi_application

# Configuración del entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trauma_register.settings')

# Inicializar la aplicación WSGI
application = get_wsgi_application()

if __name__ == '__main__':
    # Puerto donde correrá la API (puedes cambiarlo si es necesario)
    PORT = int(os.getenv('RUN_SERVER_PORT, 8000'))
    
    print(f"--- Iniciando servidor de producción (Waitress) ---")
    print(f"--- Escuchando en: http://0.0.0.0:{PORT} ---")
    print(f"--- Presiona Ctrl+C para detener ---")
    
    # serve() recibe la aplicación y la pone a disposición en la red
    # host='0.0.0.0' permite que la VM acepte conexiones externas
    serve(application, host='0.0.0.0', port=PORT, threads=4)
