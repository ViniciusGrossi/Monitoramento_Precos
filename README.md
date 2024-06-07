# Projeto ETL Mercado Livre - Análise de Tênis Masculinos

1. Problema de Negócio
Este projeto visa analisar o mercado de tênis masculinos no site do Mercado Livre. Utilizando técnicas de web scraping e análise de dados, o objetivo é fornecer insights valiosos sobre preços, marcas, avaliações e tendências do mercado para ajudar vendedores e consumidores a tomar decisões informadas.
2. Coleta de Dados
Utilizamos a biblioteca Scrapy para realizar web scraping no site do Mercado Livre, focando em anúncios de tênis masculinos. Os dados coletados incluem informações sobre preços, marcas, avaliações e outras características relevantes dos produtos. Os dados foram armazenados em um arquivo JSONL para processamento posterior.
3. Transformação e Limpeza de Dados
Os dados brutos foram carregados em um DataFrame do pandas para limpeza e transformação. As principais etapas de limpeza incluíram:

- Remoção de entradas duplicadas.
- Correção de valores ausentes e inconsistentes.
- Conversão de tipos de dados.
- Filtragem de dados irrelevantes.

4. Análise de Dados
Utilizamos o pandas e o Streamlit para realizar diversas análises e visualizações dos dados limpos. As principais análises incluíram:

- Distribuição de preços por marca.
- Correlação entre preço e avaliações.
- Identificação de outliers nos preços.
- Análise da satisfação dos consumidores por marca.
5. Produto Final do Projeto
O produto final é um painel interativo desenvolvido com Streamlit, onde é possível explorar os dados de forma dinâmica. O painel inclui filtros para refinar a análise por preço, marca e avaliações, além de diversas visualizações gráficas que facilitam a interpretação dos dados.
6. Conclusão
Este projeto demonstrou como técnicas de web scraping e análise de dados podem ser utilizadas para extrair insights valiosos do Mercado Livre. As análises realizadas forneceram uma visão detalhada sobre o mercado de tênis masculinos, ajudando a identificar tendências e padrões de comportamento dos consumidores.
7. Próximos Passos
Implementar mais métricas combinando algumas já presentes.
Criar novos filtros para refinar ainda mais as análises.
Adicionar mais perspectivas em cada visualização para enriquecer a análise.
