import time
from datetime import datetime
import keyboard
import sys
import argparse


def parse_hora(hora_str):
    try:
        # Si contiene ":", separar en hora y minutos
        if ":" in hora_str:
            hora, minutos = map(int, hora_str.split(":"))
            if 0 <= hora <= 23 and 0 <= minutos <= 59:
                return hora, minutos
        else:
            # Si es solo un número, interpretarlo como hora
            hora = int(hora_str)
            if 0 <= hora <= 23:
                return hora, 0
        raise ValueError
    except:
        raise argparse.ArgumentTypeError("Formato de hora inválido. Use HH o HH:MM (24 horas)")


def mantener_activo(hora_fin, minutos_fin, minutos_espera):
    print(f"Programa iniciado. Se detendrá a las {hora_fin:02d}:{minutos_fin:02d}")
    print(f"Intervalo de actividad: {minutos_espera} minutos")

    while True:
        ahora = datetime.now()

        # Verificar si ya pasó la hora límite
        if ahora.hour > hora_fin or (ahora.hour == hora_fin and ahora.minute >= minutos_fin):
            print("Hora límite alcanzada. Programa finalizado.")
            sys.exit()

        # Presionar y soltar shift según el intervalo especificado
        keyboard.press('shift')
        keyboard.release('shift')
        print(f"Actividad ejecutada a las {ahora.strftime('%H:%M:%S')}")
        time.sleep(minutos_espera * 60)  # Convertir minutos a segundos


if __name__ == "__main__":
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description='Programa para mantener el PC activo')

    parser.add_argument('--hora', type=parse_hora, default="18:00",
                        help='Hora de finalización en formato HH o HH:MM (por defecto: 18:00)')

    parser.add_argument('--intervalo', type=int, default=4,
                        help='Intervalo en minutos entre actividades (por defecto: 4)')

    args = parser.parse_args()

    # Desempaquetar hora y minutos
    hora_fin, minutos_fin = args.hora

    if args.intervalo <= 0:
        print("Error: El intervalo debe ser mayor a 0 minutos")
        sys.exit(1)

    try:
        mantener_activo(hora_fin, minutos_fin, args.intervalo)
    except KeyboardInterrupt:
        print("\nPrograma detenido por el usuario.")