from suaBibSignal import *
import peakutils
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
from scipy.io import wavfile
from scipy.signal import butter, lfilter
import warnings
from scipy.io.wavfile import WavFileWarning


def butter_lowpass(cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=4):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def generate_carrier_wave(frequency, duration, sample_rate):
    t = np.arange(0, duration, 1/sample_rate)
    carrier_wave = np.sin(2 * np.pi * frequency * t)
    return carrier_wave

def normalize_signal(signal):
    max_value = np.max(np.abs(signal))
    normalized_signal = signal / max_value
    return normalized_signal

def main():
    # Desativar temporariamente os avisos da biblioteca scipy.io.wavfile
    warnings.filterwarnings("ignore", category=WavFileWarning)
    # Abra o arquivo .wav em modo de leitura
    taxa_amostragem, dados = wavfile.read("golFox.wav")
    
    # Parâmetros do filtro
    frequencia_corte = 4000  # 4 kHz
    ordem = 4

    # Aplique o filtro passa-baixas
    dados_filtrados = butter_lowpass_filter(dados[:, 0], frequencia_corte, taxa_amostragem, ordem)

    # Normalizar o sinal de áudio
    dados_filtrados = dados_filtrados / np.max(np.abs(dados_filtrados))

    # Gerar a portadora
    frequencia_portadora = 14000  # 14 kHz
    duracao = len(dados_filtrados) / taxa_amostragem
    portadora = generate_carrier_wave(frequencia_portadora, duracao, taxa_amostragem)

    # Modular o sinal de áudio em AM
    sinal_modulado = (1 + dados_filtrados) * portadora

    # # Reproduzir o sinal modulado
    sd.play(sinal_modulado, taxa_amostragem)
    sd.wait()  # Aguarde a reprodução terminar

     # Normalizar o sinal modulado
    sinal_modulado_normalizado = normalize_signal(sinal_modulado)


    # Salvar o áudio modulado normalizado em um arquivo .wav
    wavfile.write("sinal_modulado_normalizado.wav", taxa_amostragem, sinal_modulado_normalizado)

    tempo = np.arange(0, len(dados)) / taxa_amostragem

    # Plote o sinal modulado normalizado
    plt.figure(figsize=(10, 6))
    plt.plot(tempo, sinal_modulado_normalizado, label='Sinal Modulado Normalizado', linewidth=2)
    plt.title('Sinal Modulado Normalizado em AM')
    plt.xlabel('Tempo (segundos)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    # Plote o sinal modulado, o sinal original e o sinal filtrado para visualização
   

    plt.figure(figsize=(10, 6))
    plt.plot(tempo, sinal_modulado, label='Sinal Modulado', linewidth=2)
    plt.title('Sinal Modulado em AM')
    plt.xlabel('Tempo (segundos)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(tempo, dados[:, 0], label='Sinal Original', alpha=0.7)
    plt.plot(tempo, dados_filtrados, label=f'Sinal Filtrado (corte={frequencia_corte} Hz)', linewidth=2)
    plt.title('Sinal Original e Sinal Filtrado')
    plt.xlabel('Tempo (segundos)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
