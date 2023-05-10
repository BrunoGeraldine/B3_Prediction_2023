# B3_Predicty_2023
Projeto de regressão utilizando TensorFlow-Keras para previsão de preço de ações da bolsa de valores Brasileira.



EDA → Utilizando YFinance

# Bandas Bollinger
Bandas de bollinger conceitos
Quando o preço do ativo ultrapassa a banda superior, observamos uma tendência de alta do ativo. Por outro lado, se o preço fica abaixo da banda inferior, há então uma tendência de baixa.
As bandas de bollinger funcionam bem para mercados que seguem tendências. Isso mostra que, se utilizadas para analisar ativos que fogem dessa premissa, podem não ser tão úteis.


<p align="center">
  <img width="1000" height="410" src="https://github.com/BrunoGeraldine/B3_Prediction_2023/assets/87772120/86db141f-ca31-4792-8028-1d1cd4ef3589"
</p>

<p align="center">
  <img width="1000" height="410" src="https://github.com/BrunoGeraldine/B3_Prediction_2023/assets/87772120/af0694f3-9238-47d4-af37-f3284b785298"
</p>
  
  Visualização grafica das bandas de bollinger utilizando como principio de tomada de decisão o cruzamento das médias movéis.
	
Estratégias utilizando bandas de bollinger
São utilizadas algumas estratégias baseadas nessa ferramenta de análise. Entretanto, nesse artigo não iremos nos aprofundar no tema, apenas indica-las. São elas:

Cruzamento dos preços com as bandas
Preço acima ou abaixo das bandas
Critério para saída da operação (Stop)



	
	
	
	

Explicação do modelo LSTM

![image](https://user-images.githubusercontent.com/87772120/236852947-37c97efa-1dbd-4753-90f3-a105d834cf81.png)

Conforme informamos o 'steps' que nada mais é os dias que o modelo deve utilizar como base para o output e assim prever o dia seguinte ou termino do valor informado no steps, ou seja, se steps=10 o output será o 11º dia.
O modelo LSTM utliza esse parametro como calculo para o output sendo assim, no teste do modelo, ele utiliza o mesmo racional para o output apenas para comparação dos erro e ajuste para optmizar a predição.


# Comparação dos prevdições com o ano de 2018 e sem o ano de 2018

→ Sem o ano de 2018
![image](https://user-images.githubusercontent.com/87772120/236906059-b12e7009-1830-486e-bbb3-2950f74351c9.png)


Fonte de dados:
[B3 times series - Data](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/series-historicas/)


[File Layout - Quotations History](https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf)
                                       

#The End!
