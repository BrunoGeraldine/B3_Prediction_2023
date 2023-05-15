# B3_Predicty_2023
Projeto de regressão utilizando TensorFlow-Keras para previsão de preço de ações da bolsa de valores Brasileira.

Técnologias aplicadas:

<p align="left">
	<img width="100" height="30" src="https://github.com/BrunoGeraldine/B3_Prediction_2023/assets/87772120/27f9c64c-0b51-41fb-aa74-7854da290708"
</p> 

<p align="left">
	<img width="100" height="30" src="https://github.com/BrunoGeraldine/B3_Prediction_2023/assets/87772120/b5a4699a-ef20-4ebf-b325-351db871c2de"
</p>  
     

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
São utilizadas algumas estratégias baseadas nessa ferramenta de análise. Entretanto, nesse artigo não iremos nos aprofundar no tema, apenas 	   indica-las. São elas:

Cruzamento dos preços com as bandas
Preço acima ou abaixo das bandas
Critério para saída da operação (Stop)

	
# MACD → Moving Average Convergence-Divergence

MACD: o que é e como funciona esse indicador?
	
Um dos indicadores mais populares da análise técnica, o MACD, é amplamente utilizado por traders de diversos mercados. 
Esse indicador, como vemos nessa análise técnica, pode emitir fortes sinais de aceleração ou reversão de tendências nos preços de um ativo.        Apesar de não ser infalível (nenhum indicador é), o MACD provê insights muito valiosos para o trader que souber utilizá-lo.
	
Como usar esse indicador na Análise Técnica?
Por ser um gerador de sinais de compra e venda, o Indicador MACD é uma maneira de prever movimentos do mercado. Portanto, seu uso é mais comum (e eficaz) para identificar o começo ou fim de uma tendência, a tempo de se posicionar para aproveitá-la.

Isso acontece com mais frequência quando a linha do MACD cruza a do Sinal. Se o cruzamento acontece em sinal de alta, a tendência é que aquele ativo se valorize em breve. O oposto é verdadeiro: se o MACD cruza a linha de Sinal em baixa, o ativo tende a fazer um movimento de baixa.
	
	
<p align="center">
  <img width="1000" height="410" src="https://github.com/BrunoGeraldine/B3_Prediction_2023/assets/87772120/bcf149c0-21d5-4c2e-b6d7-56d9b13dcdd4](https://github.com/BrunoGeraldine/B3_Prediction_2023/assets/87772120/5579c912-3986-414c-836f-ec8009d532c6"
</p>
	Visualização gráfica do grafico influenciado pelo MACD


Explicação do modelo LSTM

![image](https://user-images.githubusercontent.com/87772120/236852947-37c97efa-1dbd-4753-90f3-a105d834cf81.png)

Conforme informamos o 'steps' que nada mais é os dias que o modelo deve utilizar como base para o output e assim prever o dia seguinte ou termino do valor informado no steps, ou seja, se steps=10 o output será o 11º dia.
O modelo LSTM utliza esse parametro como calculo para o output sendo assim, no teste do modelo, ele utiliza o mesmo racional para o output apenas para comparação dos erro e ajuste para optmizar a predição.


# Comparação dos predições
	
	Resultado da predição:
	<p align="center">
  	<img width="600" height="410" src="https://github.com/BrunoGeraldine/B3_Prediction_2023/assets/87772120/af0694f3-9238-47d4-af37-f3284b785298](https://github.com/BrunoGeraldine/B3_Prediction_2023/assets/87772120/9c373192-a603-4fbf-b778-46d9d4eda669"
	</p>
		
	Grafico entre a predição e o coportamento real das datas:
	

→ Sem o ano de 2018
![image](https://user-images.githubusercontent.com/87772120/236906059-b12e7009-1830-486e-bbb3-2950f74351c9.png)


Fonte de dados:
[B3 times series - Data](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/series-historicas/)


[File Layout - Quotations History](https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf)
                                       

#The End!
