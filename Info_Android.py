import platform
import socket
import psutil

try:
    
    print("""\033[34m
██╗███╗░░██╗███████╗░█████╗░
██║████╗░██║██╔════╝██╔══██╗
██║██╔██╗██║█████╗░░██║░░██║
██║██║╚████║██╔══╝░░██║░░██║
██║██║░╚███║██║░░░░░╚█████╔╝
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░

░█████╗░███╗░░██╗██████╗░██████╗░░█████╗░██╗██████╗░
██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗
███████║██╔██╗██║██║░░██║██████╔╝██║░░██║██║██║░░██║
██╔══██║██║╚████║██║░░██║██╔══██╗██║░░██║██║██║░░██║
██║░░██║██║░╚███║██████╔╝██║░░██║╚█████╔╝██║██████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝╚═════╝░

\n""")
    print("\033[31m• ──────── 『@PreBoyx ✧ @BoxPrey 』  ──────── •")

   
    print('\033[35m===============================================')
    print(f"\033[35m| Architecture    :\033[32m {platform.architecture()[1]}  {platform.architecture()[0]} ")
    print(f"\033[35m| Machine Type    :\033[32m {platform.machine()}")
    print(f"\033[35m| Network Name    :\033[32m {platform.node()}")
    print(f"\033[35m| Platform        :\033[32m {platform.platform()}")
    print(f"\033[35m| Processor       :\033[32m {platform.processor()}")
    print(f"\033[35m| System Release  :\033[32m {platform.release()}")
    print(f"\033[35m| System OS       :\033[32m {platform.system()}")
    print(f"\033[35m| System Version  :\033[32m {platform.version()}")
    print(f"\033[35m| IP System       :\033[32m {socket.gethostbyname(socket.gethostname())}")
    print('\033[35m===============================================')

    # Información del CPU
    print(f"\033[35m┌─────────────────────────────────────────────┐")
    print(f"\033[35m│  Información del CPU                        │")
    print(f"\033[35m├─────────────────────────────────────────────┤")
    cpu_count = psutil.cpu_count(logical=False)  # Número de núcleos físicos
    print(f"\033[35m│ CPU Cores       :\033[32m {cpu_count}                         │")
    cpu_freq = psutil.cpu_freq()
    print(f"\033[35m│ CPU Frequency    :\033[32m {cpu_freq.max:.2f} MHz              │")  # Frecuencia máxima
    print(f"\033[35m└─────────────────────────────────────────────┘")

    # Información de la memoria RAM
    print('\033[35m===============================================')
    print(f"\033[35m┌──────────────────────────────────────┐")
    print(f"\033[35m│  Información de la Memoria RAM              │")
    print(f"\033[35m├──────────────────────────────────────┤")
    mem = psutil.virtual_memory()
    print(f"\033[35m│ Total RAM        :\033[32m {mem.total / (1024 * 1024 * 1024):.2f} GB                  │")
    print(f"\033[35m│ Available RAM     :\033[32m {mem.available / (1024 * 1024 * 1024):.2f} GB                 │")
    print(f"\033[35m└─────────────────────────────────────────────┘")

    # Información de los procesos
    print('\033[35m===============================================')
    print(f"\033[35m┌──────────────────────────────────────┐")
    print(f"\033[35m│  Información de los Procesos                │")
    print(f"\033[35m├──────────────────────────────────────┤")
    num_processes = len(psutil.pids())
    print(f"\033[35m│ Number of Processes:\033[32m {num_processes}                      │")
    print(f"\033[35m└─────────────────────────────────────────────┘")
    print('\033[35m===============================================')

except Exception as e:
    print(e)