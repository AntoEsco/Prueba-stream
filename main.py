import os
import subprocess

# Usaremos una señal de prueba pública (.m3u8 directo)
URL_TEST = "https://m3u8-proxy.freecodecamp.rocks/hls/live.m3u8"

# Recuperamos la clave secreta guardada en GitHub
stream_key = os.environ.get("TELEGRAM_KEY")
rtmp_destino = f"rtmps://dc.rtmp.telegram.org:443/s/{stream_key}"

print("Iniciando la retransmisión de prueba a Telegram...")

# Comando FFmpeg para reenviar la señal
cmd = [
    'ffmpeg',
    '-re',
    '-i', URL_TEST,
    '-c:v', 'copy',
    '-c:a', 'aac',
    '-f', 'flv',
    rtmp_destino
]

# Ejecuta la retransmisión
subprocess.run(cmd)
