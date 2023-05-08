# B3_Predicty_2023
Projeto de regressão utilizando TensorFlow-Keras para previsão de preço de ações da bolsa de valores Brasileira.



Explicação do modelo LSTM

![image](https://user-images.githubusercontent.com/87772120/236852947-37c97efa-1dbd-4753-90f3-a105d834cf81.png)

Conforme informamos o 'steps' que nada mais é os dias que o modelo deve utilizar como base para o output e assim prever o dia seguinte ou termino do valor informado no steps, ou seja, se steps=10 o output será o 11º dia.
O modelo LSTM utliza esse parametro como calculo para o output sendo assim, no teste do modelo, ele utiliza o mesmo racional para o output apenas para comparação dos erro e ajuste para optmizar a predição.
