# Base para proyectos en Web Scrapper con Python y Selenium:writing_hand:

Este template muestra un pequeño ejemplo de como trabajar con Selenium tratando de extraer los precios de ciertos artículos en el sitio [Narvaezbid](https://www.narvaezbid.com.ar/)

## Entorno

Asegurarse de tener instalado `git` . Esto se puede revisar muy facilmente a trevez del comando `git --version` . En caso de no estar instalado, se puede hacer a travez de los siguientes paso

- En linux, a travez del comando `sudo apt install git`.
- En Windows, a travez de la pagina oficial https://git-scm.com/

Procurar tener actualizado `python` . Si desea asegurarse, puede ejecutar el comando `python --version` que le indicara la versión de `python` instalada. Si el comando no se encuentra o `python`  esta desactualizado, puede instalar `python` mediante alguno de los siguientes pasos

- En windows, desde la windows store.
- En linux, esta pre instalado por defecto.

Por defecto, la aplicación utiliza Chrome como base para scrapper. Tener este instalado al momento de ejecutar la aplicación.

## Variables de entorno

En el archivo `main.py`:

- La variable `urls` es el listado de enlaces a scrapear. 

## Instalación y ejecución

- 🛠Para instalar las dependencias ejecutar el siguiente comando `pip install -r requirements.txt`
- ⚒Para ejecutar el ejemplo, usar el siguiente comando `python main.py`
- ⚒Si instala más dependencias y desea que se agreguen al archivo `requirements.txt`, usar el siguiente comando `pip freeze > requirements.txt`
