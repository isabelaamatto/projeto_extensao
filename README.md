# Caracterização dos incidentes de segurança relacionados ao uso de antimicrobianos e psicotrópicos notificados ao Centro de Vigilância Sanitária do Estado de São Paulo no período de 2005 a 2023
### Descrição dos arquivos
#### "DADOS_ABERTOS_MEDICAMENTOS" (csv ou xlsx)
Obtido do Portal de Dados Abertos do Governo Federal, na sessão de medicamentos registrados no Brasil, atrvés do link 'https://dados.gov.br/dados/conjuntos-dados/medicamentos-registrados-no-brasil'. Esses dados foram organizados pela ANVISA, sendo a data da última atualização em 12/01/2023;
#### "lista_medicamentos.xlsx"
Arquivo criado a partir dos medicamentos listados na Instrução Normativa 244 de 2023 e nas listas A3, B1 e B2 da Portaria 344 (atualizada em 2023);
#### "amostraNotificacoesRecebidas.json"
Amostra fornecida pelo CVS do banco de dados que será anlisado;
#### "Medicamentos_registrados_psicotrópicos.xlsx"
Dicionário dos medicamentos psicotrópicos;
#### "analise_amostras_notificacoes.ipynb"
Script da análise do arquivo "amostraNotificacoesRecebidas.json";
#### "medicamentos_1.ipynb"
Script das análises realizada com os dados do arquivo "DADOS_ABERTOS_MEDICAMENTOS";
#### "read_json.py"
Tutorial para ler arquivos do tipo json;
#### "retrieve_category.ipynb"
Script para buscar os nomes dos medicamentos do site https://consultaremedios.com.br;
#### "VigiMed_Medicamentos.csv", "VigiMed_Notificacoes.csv", "VigiMed_Reacoes.csv"
Planilhas da ANVISA com os dados abertos utilizados no projeto. Futuramente serão substituídas pelas planilhas com os dados fechados;
#### "variaveis de interesse vigimed.jpg"
Arquivo com as variáveis de interesse para cada arquivo VigiMed
#### "vigimed.ipynb"
Scrit da análise dos dados das planilhas VigiMed (Notificações, Medicamentos e Reações). Utilização dos dicionários de medicamentos e reações adversas.
#### Gráficos: os arquivos a seguir contém gráficos produzidos pela análise dos dados VigiMed
- medicamentos_missing_filled.pdf e medicamentos_missing_filled_editado.svg
- notificacoes_missing_filled.pdf e notificacoes_missing_filled_editado.svg
- reacoes_missing_filled.pdf e reacoes_missing_filled_editado.svg
Gráficos originais e editados da análise do preenchimento das colunas das tabelas "VigiMed_Medicamentos.csv", "VigiMed_Notificacoes.csv" e "VigiMed_Reacoes.csv". Os gráficos apresentam a quantidade de linhas preenchidas e não preenchidas para cada coluna das tabelas.
