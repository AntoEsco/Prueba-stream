import os
import subprocess

# Enlace de prueba directo y superestable (Señal HLS pública)
URL_TEST = "https://demo.unified-streaming.com/k8s/features/stable/hls/tears-of-steel/tears-of-steel.ism/.m3u8"

# Recuperamos la clave secreta guardada en GitHub
stream_key = os.environ.get("TELEGRAM_KEY")
rtmp_destino = f"rtmps://dc.rtmp.telegram.org:443/s/{stream_key}"

print("Iniciando la retransmisión de prueba a Telegram...")

cmd = [
    'ffmpeg',
    '-re',
    '-i', URL_TEST,
    '-c:v', 'copy',
    '-c:a', 'aac',
    '-f', 'flv',
    rtmp_destino
]

subprocess.run(cmd)
