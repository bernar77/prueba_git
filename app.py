import sys

print(sys.path)

'''
Para ambas formas hay que estar en la carpeta del proyecto donde se usara el entorno
forma 1: Bash
    intalar virtualenv: 
        pip install virtualenv 

    crea entorno virtual: 
        virtualenv nombre_entorno
            (recomendados: env, .env)

    activar entorno virtual:
        source nombre_entorno/Scripts/activate 
            (puede ser también 'nombre_entorno/bin/activate' en linux)
    
    crear archivo requeriments:
        pip freeze > requeriments.txt

    instalar entorno guardado:
        pip install -r requirements.txt
            /despues de haber creado el nuevo entorno y activado)

forma 2: Command Prompt --> no funciona con Powershell!!

    crear entorno virtual:
    c:\Users\berna\AppData\Local\Programs\Python\Python38-32\python.exe -m venv nombre_entorno
        (recomendados: venv, .venv)

    activar entorno virtual:
        nombre_entorno\Scripts\activate.bat


'''