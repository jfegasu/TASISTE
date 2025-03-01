#COMMIT EN GIT HUB: git commit -m "Texto que quieras poner"
# Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
from app import app

# Importando todos las Rutas
from app import *


if __name__ == '__main__':   
    app.run(debug=True, port=5000,host='0.0.0.0')
