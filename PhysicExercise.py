import sys
import os

print("""
Preparación para física
""")

command = sys.argv[1]

if command == '-h' or command == '--help':
    print("""
-ef, --env-file     Crea conda environment file [-h,--help,-k,--key]
-v, --version       Muestra la version
-h, --help          Muestra la información general y comandos
""")
    sys.exit(1)

if command == "-v" or command == "--version":
    print('0.0.1')
    sys.exit(1)

if command == '-ef' or command == '--env-file':
    command = sys.argv[2]
    if command == '-h' or command == '--help':
        print("""
-k=<key>, --key=<key>   Clave para general el archivo.
""")
        sys.exit(1)
    if command.split('=')[0] == '-k' or command.split('=')[0] == '--key':
        if command.split('=')[1] == 'julyoc':
            os.system('conda env export > vs-env.yml')
        else:
            print('Clave incorrecta')