# Projeto APC - Analise de Impacto Ambiental de Algoritmos

## Equipe

- Paulo Victor
- Diego Guedes
- Rafael Simoes de Paula
- Kawan Ubirajara Dos Santos Dias Borges
- Gabriel de Medeiros Matos

## Problema

O uso crescente de tecnologias e desenvolvimento de softwares tem aumentado significativamente o consumo global de energia eletrica. Aplicacoes que demandam grande poder computacional, como algoritmos de ordenacao massivos e modelos de Inteligencia Artificial, contribuem para esse consumo.

Muitos desenvolvedores e usuarios desconhecem o impacto ambiental causado pela execucao de algoritmos ineficientes, que consomem mais energia e geram maiores emissoes de carbono. Esse desconhecimento impede a adocao de praticas de programacao sustentavel.

## Objetivo

Desenvolver um sistema em Python 3 que analisa e compara o gasto energetico estimado de algoritmos comuns de ordenacao (Merge Sort, Quick Sort, Bubble Sort, Insertion Sort e Bogosort) com implementacoes em outras linguagens de programacao (C, Java e Go) e, opcionalmente, com modelos de IA locais usando Ollama.

O sistema apresenta relatorios e graficos que demonstram como a eficiencia de algoritmos e linguagens impacta o meio ambiente, incentivando praticas de computacao sustentavel.

## Estrutura do Projeto

```
projeto_apc_revisado/
├── engine/
│   ├── __init__.py
│   ├── comparador_linguagens.py
│   ├── exportador_csv.py
│   ├── gerador_listas.py
│   ├── graficos.py
│   ├── impacto_ambiental.py
│   ├── medidor_desempenho.py
│   ├── medidor_llm_local.py
│   └── metodos_ordenacao.py
├── main.py
├── README.md
├── requirements.txt
└── pyproject.toml
```

## Instalacao

### Pre-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

### Instalacao com pip

```bash
# Clone o projeto
git clone https://github.com/Polers-two/Projeto-APC-Turma-6-2025.2
cd Projeto-APC-Turma-6-2025.2

# Instale as dependencias
pip install -r requirements.txt

# Execute o programa
python main.py
```

### Instalacao com UV (opcional)

```bash
# Instale as dependencias com UV
uv sync

# Execute o programa
uv run python main.py
```

## Funcionalidades

### Menu Principal

O programa oferece as seguintes opcoes:

1. Merge Sort - Algoritmo de ordenacao O(n log n)
2. Quick Sort - Algoritmo de ordenacao O(n log n) medio
3. Bubble Sort - Algoritmo de ordenacao O(n²)
4. Insertion Sort - Algoritmo de ordenacao O(n²)
5. Bogosort - Algoritmo educacional O((n+1)!) - maximo 10 elementos
6. Gerar listas automaticas - Cria listas de teste
7. Comparar todos - Executa todos os algoritmos
8. Estatisticas - Calcula medias dos resultados
9. Graficos Python - Gera visualizacoes comparativas
10. Comparar com outras linguagens - Compara Python com C/Java/Go
11. Medir LLM local - Compara com modelos de IA (requer Ollama)
12. Exportar resultados para CSV - Salva dados em arquivos CSV
0. Sair - Encerra o programa

### Algoritmos Implementados

**Merge Sort (O(n log n))**
Divide a lista em partes menores recursivamente e depois junta as partes ordenadas.

**Quick Sort (O(n log n) medio)**
Escolhe um pivo e separa a lista em elementos menores e maiores que o pivo.

**Bubble Sort (O(n²))**
Compara elementos adjacentes e os troca se estiverem na ordem errada.

**Insertion Sort (O(n²))**
Constroi a lista ordenada inserindo cada elemento na posicao correta.

**Bogosort (O((n+1)!))**
Embaralha a lista aleatoriamente ate que esteja ordenada. Apenas para fins educacionais.

### Geracao de Listas

O programa gera automaticamente listas de teste com os seguintes tamanhos:
- 10 elementos (teste rapido)
- 1.000 elementos (pequeno)
- 10.000 elementos (medio)
- 100.000 elementos (grande)

### Comparacao entre Linguagens

O sistema possui dados de benchmark reais de implementacoes em C, Java e Go para comparacao. Voce pode:
- Ver tabela comparativa de um algoritmo especifico
- Gerar grafico comparativo de um algoritmo
- Gerar grafico comparativo de todos os algoritmos

### Exportacao de Dados

Nova funcionalidade que permite exportar:
- Todos os resultados de execucao para CSV
- Estatisticas agregadas (medias) para CSV

Os arquivos CSV sao salvos no diretorio atual com data e hora no nome.

### Integracao com LLM (Opcional)

Se voce tiver o Ollama instalado, pode comparar o impacto ambiental de usar modelos de IA para ordenar listas versus algoritmos tradicionais.

Para usar esta funcionalidade:
1. Instale o Ollama em https://ollama.ai
2. Baixe um modelo: `ollama pull llama3.2`
3. Execute a opcao 11 no menu

## Metodologia Cientifica

### Formulas Utilizadas

**Energia Estimada (Wh):**
```
E = (P_CPU × T × Uso_CPU%) / 3600
```

Onde:
- P_CPU = Potencia media da CPU (65W padrao)
- T = Tempo de execucao (em segundos)
- Uso_CPU% = Percentual de uso da CPU (0-100)

**Emissao de CO2 (g):**
```
CO2 = E × 426
```

Fonte: IEA (International Energy Agency) 2025
- 426 gCO2/kWh e a media global para geracao eletrica em 2025

### Medicao de Desempenho

O sistema utiliza:
- time.perf_counter() para medicao precisa de tempo
- psutil.Process().cpu_percent() para uso real de CPU
- Dados de benchmarks reais para C, Java e Go

## Dependencias

| Biblioteca | Versao Minima | Funcao |
|------------|---------------|---------|
| matplotlib | 3.10.7 | Geracao de graficos |
| pillow | 12.0.0 | Processamento de imagens |
| psutil | 7.1.3 | Medicao de CPU e processos |
| rich | 14.2.0 | Interface CLI elegante |

## Requisitos Funcionais

| ID | Descricao |
|----|-----------|
| RF01 | Executar algoritmos classicos de ordenacao |
| RF02 | Medir tempo de execucao e uso de CPU |
| RF03 | Calcular consumo energetico estimado |
| RF04 | Calcular emissoes de CO2 equivalentes |
| RF05 | Gerar graficos comparativos |
| RF06 | Permitir comparacao entre linguagens |
| RF07 | Permitir comparacao com modelos de IA |
| RF08 | Exibir resumo e relatorio final |
| RF09 | Exportar dados para formato CSV |

## Exemplo de Uso

```bash
# Execute o programa
python main.py

# Fluxo recomendado:
# 1. Escolha opcao 6 - Gerar listas automaticas
# 2. Escolha opcao 7 - Comparar todos os algoritmos
#    → Selecione tamanho: 10000
# 3. Escolha opcao 9 - Ver graficos comparativos
# 4. Escolha opcao 12 - Exportar resultados para CSV
# 5. Escolha opcao 10 - Comparar com outras linguagens
```

### Exemplo de Saida

```
Comparacao (10.000 elementos)
┌──────────────┬──────────┬───────┬──────────┬────────┐
│ Algoritmo    │ Tempo    │ CPU   │ Energia  │ CO2    │
├──────────────┼──────────┼───────┼──────────┼────────┤
│ Merge Sort   │ 0.012448 │ 87.48 │ 0.000039 │ 0.0166 │
│ Quick Sort   │ 0.009974 │ 83.19 │ 0.000015 │ 0.0064 │
│ Bubble Sort  │ 1.750150 │ 99.86 │ 0.031550 │ 13.440 │
│ Insertion    │ 0.146610 │ 98.65 │ 0.002610 │ 1.1119 │
└──────────────┴──────────┴───────┴──────────┴────────┘
```

## Funcionalidades Extras

### Interface CLI Avancada
Utilizacao da biblioteca Rich para criar uma interface de linha de comando elegante com:
- Tabelas formatadas
- Cores e estilos
- Paineis informativos
- Validacao de entrada

### Comparacao Multi-Linguagem
Benchmarks reais de C, Java e Go permitem comparar o desempenho de Python com linguagens compiladas.

### Visualizacoes com Matplotlib
Graficos de barras comparativos mostram visualmente as diferencas de:
- Tempo de execucao
- Consumo de energia
- Emissao de CO2

### Analise Estatistica
Calculo de medias de multiplas execucoes para resultados mais confiáveis.

### Exportacao de Dados
Nova funcionalidade que permite salvar todos os resultados e estatisticas em formato CSV para analise posterior.

## Documentacao dos Modulos

### main.py
Arquivo principal com menu interativo e orquestracao de funcionalidades.

### metodos_ordenacao.py
Implementacoes dos algoritmos de ordenacao.

### medidor_desempenho.py
Funcao que mede tempo de execucao e uso de CPU.

### impacto_ambiental.py
Calcula energia consumida e emissao de CO2.

### graficos.py
Funcoes de visualizacao com matplotlib.

### comparador_linguagens.py
Benchmarks e comparacoes com outras linguagens.

### medidor_llm_local.py
Integracao com Ollama para medir LLMs locais.

### gerador_listas.py
Geracao de listas de teste com diferentes tamanhos.

### exportador_csv.py
Exportacao de resultados e estatisticas para formato CSV.

## Referencias

- IEA Emissions Report: https://www.iea.org/reports/electricity-2025/emissions
- Python psutil: https://psutil.readthedocs.io/
- Rich Documentation: https://rich.readthedocs.io/
- Ollama: https://ollama.ai
