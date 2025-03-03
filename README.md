# CamadasProjeto8

Descrição Geral
O sistema contém três partes principais:

Codificação (Modulação AM)

Lê um arquivo de áudio (golFox.wav).
Filtra o sinal com um filtro passa-baixa de 4 kHz.
Normaliza o áudio.
Gera uma onda portadora de 14 kHz.
Modula o sinal usando AM.
Reproduz e salva o sinal modulado (sinalModulado.wav).
Plota gráficos do sinal original, filtrado e modulado.
Decodificação (Demodulação AM)

Lê o sinal modulado (sinalModulado.wav).
Gera uma portadora idêntica à usada na modulação.
Multiplica o sinal modulado pela portadora para recuperar o áudio original.
Aplica um detector de envelope para extrair o sinal original.
Reproduz e plota a envoltória do sinal demodulado.
Biblioteca de Processamento de Sinal (suaBibSignal.py)

Implementa transformada de Fourier para análise espectral.
Usa janela de Hamming para suavizar o espectro.
Permite visualizar a frequência dominante no sinal.
Objetivo
O código permite codificar um áudio em um sinal AM, transmiti-lo e depois recuperar o áudio original, analisando o comportamento da modulação/demodulação. 
