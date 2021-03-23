import wave 
import numpy as np
import matplotlib.pyplot as plt

#Cargar archivo wav en la variable 

audio1 = wave.open('audio1.wav', 'r')
audio2 = wave.open('audio2.wav', 'r')

#Obtener todos los frames del objeto wave
frames = audio1.readframes(-1)
frames_t = audio2.readframes(-1)

#Mostrar el resultado de frames
#print(frames [:10])

#Convierte el audio good morning de bytes a enteros
ondaconvertida = np.frombuffer(frames, dtype='int16')
ondaconvertida_t = np.frombuffer(frames_t, dtype='int16')
#print(ondaconvertida [:10])

framerate_o = audio1.getframerate()
framerate_t = audio2.getframerate()

print(framerate_o)
print(framerate_t)

time_o = np.linspace(start = 0, stop = len(ondaconvertida ) /framerate_o, num= len(ondaconvertida))
time_t = np.linspace(start = 0, stop = len(ondaconvertida_t ) /framerate_t, num= len(ondaconvertida_t))

print(time_o[:10])
print(time_t[:10])

#Generación de la gráfica

plt.title('audio1 vs audio2')

#etiquetas de los ojos
plt.xlabel('Tiempo segundos')
plt.ylabel('Amplitud')

#Agregar la informacion
plt.plot(time_o, ondaconvertida, label='audio1')
plt.plot(time_t, ondaconvertida_t, label='audio2', alpha = 0.5)

plt.legend()
plt.show()