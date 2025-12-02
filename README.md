# Projeto APC - Analise de Impacto Ambiental de Algoritmos

## Equipe

- Paulo Victor
- Diego Guedes
- Rafael Simoes de Paula
- Kawan Ubirajara Dos Santos Dias Borges
- Carlos Eduardo Pereira Dos Santos
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
pip install requirements.txt

# Execute o programa
python main.py
```

### Instalacao com UV (opcional)

```bash
# Instale as dependências
uv sync 

# Execute o programa
uv run python main.py
```

## Funcionalidades

### Menu Principal

O programa oferece as seguintes opcoes:

# Baixe um modelo (exemplo)
ollama run llama3.2
```

### Algoritmos Implementados

**Merge Sort (O(n log n))**
Divide a lista em partes menores recursivamente e depois junta as partes ordenadas.

**Quick Sort (O(n log n) medio)**
Escolhe um pivo e separa a lista em elementos menores e maiores que o pivo.

**Bubble Sort (O(n²))**
Compara elementos adjacentes e os troca se estiverem na ordem errada.

**Insertion Sort (O(n²))**
Constroi a lista ordenada inserindo cada elemento na posicao correta.

#### 1-5: Algoritmos de Ordenação
- **Merge Sort**: O(n log n) - Divide e conquista
- **Quick Sort**: O(n log n) médio - Particionamento
- **Bubble Sort**: O(n²) - Comparação de adjacentes
- **Insertion Sort**: O(n²) - Inserção ordenada
- **Bogosort**: O((n+1)!) - Foça bruta (máx 10 elementos)

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

#### 10: Comparar com Outras Linguagens
Compara resultados Python com benchmarks reais de:
- **C** 
- **Java** 
- **Go** 

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

| Biblioteca    | Versão    | Função                              |
|---------------|-----------|-------------------------------------|
| **matplotlib**| ≥3.10.7   | Geração de gráficos                 |
| **pillow**    | ≥12.0.0   | Processamento de imagens            |
| **psutil**    | ≥7.1.3    | Medição de CPU e processos          |
| **rich**      | ≥14.2.0   | Interface CLI elegante              |
| **numpy**     | ≥2.0.0    | Operações numéricas                 |

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

### 1. Interface CLI (Rich)
- Tabelas formatadas
- Cores e estilos
- Painéis informativos
- Prompts validados

### 2. Comparação Multi-Linguagem
- Benchmarks reais de C, Java e Go
- Cálculo de speedup
- Gráficos comparativos

### 3. Integração com LLMs
- Suporte a Ollama
- Comparação de impacto ambiental
- Análise de custo computacional de IA

### 4. Visualizações Avançadas
- Gráficos de barras agrupadas
- Comparações multi-dimensionais
- Valores anotados nas barras

### 5. Análise Estatística
- Médias de múltiplas execuções
- Comparação de eficiência
- Relatórios detalhados

---

## Documentação dos Módulos

### `main.py`
Arquivo principal com menu interativo e orquestração de funcionalidades.

### `metodos_ordenacao.py`
Implementações dos algoritmos:
- `merge_sort(lista)` - O(n log n)
- `quick_sort(lista)` - O(n log n) médio
- `bubble_sort(lista)` - O(n²)
- `insertion_sort(lista)` - O(n²)
- `bogosort(lista)` - O((n+1)!) 

### `medidor_desempenho.py`
Função `medir_desempenho(func, *args, **kwargs)`:
- Mede tempo com `time.perf_counter()`
- Mede CPU com `psutil.Process().cpu_percent()`
- Retorna dicionário com resultados

### `impacto_ambiental.py`
Função `calcular_impacto(tempo, cpu, potencia=65)`:
- Calcula energia em Wh
- Calcula emissão de CO2 em gramas
- Baseado em fórmulas científicas

### `graficos.py`
Funções de visualização:
- `grafico_completo(resultados)` - Gráficos Python
- `grafico_comparativo_linguagens(...)` - Comparação específica
- `grafico_comparativo_todos_algoritmos(...)` - Visão geral

### `comparador_linguagens.py`
Benchmarks e comparações:
- `obter_benchmark(linguagem, algoritmo, tamanho)`
- `mostrar_comparacao(resultado_python, algoritmo, tamanho)`
- Dados reais de C, Java e Go

### `medidor_llm_local.py`
Integração com Ollama:
- `verificar_ollama()` - Verifica instalação
- `listar_modelos()` - Lista modelos disponíveis
- `medir_llm_local(modelo, lista)` - Mede desempenho
- `comparar_algoritmo_vs_llm(...)` - Comparação

### `gerador_listas.py`
Geração de listas de teste:
- `gerar_listas()` - Cria listas de 10, 1k, 10k, 100k elementos
- `mostrar_info_listas(listas)` - Exibe informações

---

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

- Allen B. Downey, Pense em Python: Pense como um cientista da computacao, 2016.
- Luciano Ramalho, Python Fluente: Programacao clara, concisa e eficaz, 2015.
- IEA Emissions Report: https://www.iea.org/reports/electricity-2025/emissions
- Python psutil: https://psutil.readthedocs.io/
- Rich Documentation: https://rich.readthedocs.io/
- Ollama: https://ollama.ai

## Licenca

Este projeto foi desenvolvido para fins academicos como parte da disciplina CIC0004 - Algoritmos e Programacao de Computadores da Universidade de Brasilia.
