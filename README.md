# 1. Problema de negócio.

A Fome Zero é uma empresa de tecnologia que criou um aplicativo que conecta pessoas a restaurantes de diversas cidades, em países diferentes. Seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O meu desafio como estudante de Python do curso Ciência de Dados é aplicar meus conhecimentos adquirido na Instituição de ensino Comunidade DS, tomando como premissa do meu meu primeiro projeto de análise de dados a empresa Fome Zero.

Para isso vou precisar fazer uma análise nos dados respondendo a algumas perguntas levantadas junto a empresa, bem como demonstrar seu resultado em forma de respostas e, quando necessário, gerar dashboards visando auxiliar o CEO Guerra recém-contratado a entender melhor o funcionamento do negócio para conseguir, com isso, uma melhor tomada de decisão estratégica e alavancar ainda mais os objetivos da empresa Fome Zero.

# Levantamento Geral 

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

# Levantamento Países 

1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

# Levantamento Cidades 

1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

# Levantamento Restaurantes 

1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de um prato para duas pessoas? 
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maiores que as churrascarias americanas (BBQ)?

# Levantamento Tipos de Culinária. 

1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação? 
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação? 
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

O objetivo deste projeto é criar um conjunto de gráficos e/ou tabelas que exibam da melhor forma as informações para novo CEO da empresa.

# 2. Premissas assumidas para análise

1. A Fome Zero tem como seu modelo de negócio marketplace.
2. Sua visão de negócio e conectar diferentes clientes a diversos restaurantes, em diversos países e cidades com foco em diferentes tipos de culinárias. 
3. Os três principais visão de negócio foram: Visão de Países, Visão de Cidades e Visão de Tipos de Culinárias.

# 3. Estratégia de solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem as principais visões de modelo de negócio da empresa:
* Apresentação Geral
* Visão Países
* Visão Cidades
* Visão Tipos de Culinárias

Cada visão é representada pelo seguinte conjunto de métricas.

# 3.1. Apresentação Geral

	Total Restaurante Cadastrado
	Países Cadastrado 
	Total Cidades 
	Total Avaliações na Plataforma 
	Total Tipos de Culinárias 
	Mapas Países e Restaurantes 

# 3.2. Visão Países
	Quantidade de Restaurantes Registrados por País
	Quantidade de Cidades Registradas por País
	Média de Avaliações feitas por País
	Média Preço de Prato para duas pessoas por País
	
# 3.3. Visão Cidades
	10 Cidades com mais Restaurantes na Base de dados
	7 Top Cidades com Restaurantes com média de avaliação acima de 4
	7 Top Cidades com Restaurantes com média de avaliação abaixo de 2.5
	Top 10 Cidades com mais Restaurantes com tipos culinários distintos

# 3.4. Visão Tipos de Culinárias
 	O Melhor Restaurante do Principal tipo Culinária Italian 
	O Melhor Restaurante do Principal tipo Culinária American
	O Melhor Restaurante do Principal tipo Culinária Arabians
	O Melhor Restaurante do Principal tipo Culinária Japanese
	O Melhor Restaurante do Principal tipo Culinária Brazil
	Top 10 Restaurantes
	Top 10 Melhores Tipos de Culinária
	Top 10 Piores Tipos de Culinária

# 4. Top 3 Insights de dados

  1. Mesmo a Índia tendo o maior número de cidades cadastradas, como também o maior número de restaurantes cadastrados, é a Indonésia que lidera em melhor preço para duas pessoas.
  2. Menos de 30% dos países cadastrados trabalham com delivery online.
  3. O Brasil tem baixa avaliação no geral.

# 5. O produto final do projeto

Painel interativo online, hospedado em uma Cloud e disponível através do link: https://marlids-project-fome-zero.streamlit.app/

# 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível com o objetivo de fornecer a melhor visão da empresa para o novo CEO.

# 7. Próximos passos.

1. Expandir as métricas.
2. Criar novos filtros.
3. Adicionar novas visões de negócios.
