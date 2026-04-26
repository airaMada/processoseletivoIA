# Relatório - Projeto de IA

Identificação: Maria Madalena da silva


### 1️⃣ Resumo da Arquitetura do Modelo
O modelo implementado é uma Rede Neural Convolucional (CNN) construída utilizando o TensorFlow/Keras. A arquitetura consiste em duas camadas de convolução (Conv2D) com função de ativação ReLU, seguidas por camadas de MaxPooling para redução dimensional. Em seguida, os dados são achatados com uma camada Flatten e passam por uma camada densa (Dense) com 64 neurônios. A camada de saída possui 10 neurônios com ativação softmax, correspondendo às classes de dígitos de 0 a 9.

### 2️⃣ Bibliotecas Utilizadas
O projeto utiliza o TensorFlow como framework principal, especificamente:
- tensorflow.keras.models.Sequential: estrutura do modelo em camadas
- tensorflow.keras.layers: Conv2D, MaxPooling2D, Flatten, Dense
- tensorflow.keras.datasets.mnist: carregamento dos dados MNIST

### 3️⃣ Técnica de Otimização do Modelo
Foi utilizada a técnica de Dynamic Range Quantization através do TensorFlow Lite. Essa técnica reduz o tamanho do modelo ao converter os pesos de precisão float32 para uma representação mais leve, mantendo um bom desempenho. A otimização foi aplicada durante a conversão do modelo para o formato `.tflite`.

### 4️⃣ Resultados Obtidos
O modelo apresentou uma acurácia de aproximadamente 0.9910 no conjunto de teste, demonstrando alta capacidade de generalização na classificação de dígitos manuscritos.

### 5️⃣ Comentários Adicionais 
Durante o desenvolvimento, a principal dificuldade foi entender o fluxo completo do projeto, incluindo treinamento e otimização do modelo. Foi possível aprender sobre redes neurais convolucionais, pré-processamento de dados e técnicas de otimização para execução em dispositivos embarcados.
