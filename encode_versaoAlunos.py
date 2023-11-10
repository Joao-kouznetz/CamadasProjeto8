from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, lfilter

def generate_carrier_wave(frequency, duration, sample_rate):
    t = np.arange(0, duration, 1/sample_rate)
    carrier_wave = np.sin(2 * np.pi * frequency * t)
    return carrier_wave

def envelope_detector(signal):
    b, a = [1], np.array([1, -0.95])
    envelope = lfilter(b, a, np.abs(signal))
    return envelope

def main():
    taxa_amostragem, dados_modulados = wavfile.read("sinalModulado.wav")

    # Parâmetros da portadora
    frequencia_portadora = 14000  # A mesma frequência usada na modulação
    duracao = len(dados_modulados) / taxa_amostragem
    portadora = generate_carrier_wave(frequencia_portadora, duracao, taxa_amostragem)

    # Demodulação multiplicando o sinal pela portadora original
    sinal_demodulado = dados_modulados * portadora[:len(dados_modulados)]

    # Aplicar envelope detector
    envelope = envelope_detector(sinal_demodulado)

    # Reproduzir o sinal demodulado
    sd.play(envelope, taxa_amostragem)
    sd.wait()

    # Plotar a envoltória
    plt.figure(figsize=(12, 6))
    plt.plot(envelope)
    plt.title('Envoltória do Sinal Demodulado')
    plt.xlabel('Tempo')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
