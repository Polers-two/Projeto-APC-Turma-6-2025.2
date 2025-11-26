# Projeto APC - Análise de Impacto Ambiental de Algoritmos

## Especificação do Projeto

### Problema
O crescimento exponencial do uso de tecnologias e do desenvolvimento de softwares vem aumentando o **consumo global de energia elétrica**, especialmente em aplicações que demandam **grande poder computacional**, como algoritmos de ordenação massivos e **modelos de Inteligência Artificial (IA)**.

Apesar disso, muitos desenvolvedores e usuários desconhecem o **impacto ambiental** causado pela execução de algoritmos ineficientes, que consomem mais energia e geram maiores emissões de carbono.  
Esse desconhecimento impede a adoção de práticas de **programação sustentável**.

---

### Objetivo Geral
Desenvolver um sistema em **Python 3** que analisa e compara o **gasto energético estimado** de algoritmos comuns (como *Merge Sort*, *Quick Sort*, *Bubble Sort*, etc.) com implementações em outras linguagens de programação e, se possível, com modelos de IA de uso comum (como LLaMA via Ollama).

O sistema deve apresentar relatórios e gráficos que demonstrem como a **eficiência de algoritmos e linguagens impacta o meio ambiente**, incentivando práticas de **computação sustentável**.

---

## Estrutura do Projeto

```
projeto-apc/
├── .venv/                      # Ambiente virtual Python
├── Lib/                        # Bibliotecas do ambiente
├── Scripts/                    # Scripts de ativação
├── share/                      # Recursos compartilhados
├── engine/                     # CÓDIGO PRINCIPAL
│   ├── __pycache__/           # Cache Python
│   ├── __init__.py            # Inicializador do módulo
│   ├── comparador_linguagens.py  # Comparação Python vs C/Java/Go
│   ├── gerador_listas.py      # Geração de listas de teste
│   ├── graficos.py            # Visualizações com matplotlib
│   ├── impacto_ambiental.py   # Cálculo de energia e CO2
│   ├── medidor_desempenho.py  # Medição de tempo e CPU
│   ├── medidor_llm_local.py   # Comparação com LLMs (Ollama)
│   └── metodos_ordenacao.py   # Algoritmos de ordenação
├── src/                       # Código fonte
│   ├── __pycache__/
│   └── __init__.py
│   ├── main.py                # Arquivo principal 
├── .gitignore                 # Arquivos ignorados pelo Git
├── .lock                      # Lock de dependências
├── pyproject.toml             # Configuração do projeto
├── python-version             # Versão do Python
├── README.md                  # Este arquivo
└── uv.lock                    # Lock do gerenciador UV
```

---

## Instalação e Execução

### Pré-requisitos
- **Python 3.13** ou superior
- **UV** (gerenciador de pacotes) - Recomendado
- **Ollama** (opcional) - Para comparação com LLMs

### Instalação com UV (Recomendado)

```bash
# Clone o repositório
git clone <seu-repositorio>
cd projeto-apc

# Instale as dependências com UV
uv sync

# Execute o programa
uv run python engine/main.py
```

### Instalação Alternativa (pip)

```bash
# Instale as dependências
pip install matplotlib pandas pillow psutil rich 

# Execute o programa
python engine/main.py
```

### Funcionalidade LLM (Opcional)

Para usar a comparação com modelos LLM locais:

```bash
# Instale o Ollama
# Visite: https://ollama.ai

# Baixe um modelo (exemplo)
ollama run llama3.2
```

---

## Funcionalidades

### Menu Principal

```
╭─────────────────────────────────────────────────────────╮
│                         MENU                            │
├────────┬────────────────────────────────────────────────┤
│ Opção  │ Descrição                                      │
├────────┼────────────────────────────────────────────────┤
│ 1      │ Merge Sort                                     │
│ 2      │ Quick Sort                                     │
│ 3      │ Bubble Sort                                    │
│ 4      │ Insertion Sort                                 │
│ 5      │ Bogosort (máx 10 elementos)                    │
│ 6      │ Gerar listas automáticas                       │
│ 7      │ Comparar todos                                 │
│ 8      │ Estatísticas                                   │
│ 9      │ Gráficos Python                                │
│ 10     │ Comparar com outras linguagens (C/Java/Go)     │
│ 11     │ Medir LLM local (Ollama)                       │
│ 0      │ Sair                                           │
╰────────┴────────────────────────────────────────────────╯
```

### Descrição das Funcionalidades

#### 1-5: Algoritmos de Ordenação
- **Merge Sort**: O(n log n) - Divide e conquista
- **Quick Sort**: O(n log n) médio - Particionamento
- **Bubble Sort**: O(n²) - Comparação de adjacentes
- **Insertion Sort**: O(n²) - Inserção ordenada
- **Bogosort**: O((n+1)!) - Foça bruta (máx 10 elementos)

#### 6: Gerar Listas Automáticas
Cria listas de teste com tamanhos:
- 10 elementos (teste rápido)
- 1.000 elementos (pequeno)
- 10.000 elementos (médio)
- 100.000 elementos (grande)

#### 7: Comparar Todos
Executa todos os algoritmos (exceto Bogosort se lista > 10) e exibe tabela comparativa.

#### 8: Estatísticas
Calcula médias de tempo, energia e CO2 de todos os algoritmos executados.

#### 9: Gráficos Python
Gera visualizações comparativas com matplotlib:
- Tempo de execução
- Consumo de energia
- Emissão de CO2

#### 10: Comparar com Outras Linguagens
Compara resultados Python com benchmarks reais de:
- **C** 
- **Java** 
- **Go** 

Opções:
1. Tabela de comparação de um algoritmo
2. Gráfico de um algoritmo específico
3. Gráfico comparativo de todos os algoritmos

#### 11: Medir LLM Local
Compara o impacto ambiental de usar LLMs (via Ollama) para ordenar listas vs algoritmos tradicionais.

**Requer**: Ollama instalado e modelo baixado (ex: `ollama pull llama3.2`)

---

## Metodologia Científica

### Fórmulas Utilizadas

#### Energia Estimada (Wh):
```
E = (P_CPU × T × Uso_CPU%) / 3600
```

**Onde:**
- `P_CPU` = Potência média da CPU (65W padrão)
- `T` = Tempo de execução (em segundos)
- `Uso_CPU%` = Percentual de uso da CPU (0-100)

#### Emissão de CO2 (g):
```
CO2 = E × 426
```

**Fonte**: [IEA - International Energy Agency 2025](https://www.iea.org/reports/electricity-2025/emissions)  
*426 gCO2/kWh é a média global para geração elétrica em 2025*

### Medição de Desempenho

O sistema utiliza:
- **`time.perf_counter()`**: Medição precisa de tempo
- **`psutil.Process().cpu_percent()`**: Uso real de CPU
- **Benchmarks reais**: Dados de C, Java e Go baseados em 50 execuções

---

## Dependências

| Biblioteca    | Versão    | Função                              |
|---------------|-----------|-------------------------------------|
| **matplotlib**| ≥3.10.7   | Geração de gráficos                 |
| **pillow**    | ≥12.0.0   | Processamento de imagens            |
| **psutil**    | ≥7.1.3    | Medição de CPU e processos          |
| **rich**      | ≥14.2.0   | Interface CLI elegante              |
| **numpy**     | ≥2.0.0    | Operações numéricas                 |

---

## Requisitos Funcionais

| ID    | Descrição                                              
|-------|--------------------------------------------------------|
| RF01  | Executar algoritmos clássicos de ordenação             |
| RF02  | Medir tempo de execução e uso de CPU                   |
| RF03  | Calcular consumo energético estimado (kWh)             |
| RF04  | Calcular emissões de CO2 equivalentes                  |
| RF05  | Gerar gráficos comparativos de desempenho e energia    |
| RF06  | Permitir comparação entre linguagens                   |
| RF07  | Permitir comparação com modelos de IA                  |
| RF08  | Exibir resumo e relatório final de resultados          |
------------------------------------------------------------------

---

## Exemplo de Uso

```bash
# Execute o programa
uv run python engine/main.py

# Fluxo recomendado:
# 1. Escolha opção 6 - Gerar listas automáticas
# 2. Escolha opção 7 - Comparar todos os algoritmos
#    → Selecione tamanho: 10000
# 3. Escolha opção 9 - Ver gráficos comparativos
# 4. Escolha opção 10 - Comparar com outras linguagens
#    → Opção 3 - Gráfico de todos os algoritmos
# 5. Escolha opção 11 - Comparar com LLM (se Ollama instalado)
```

### Exemplo de Saída

```
╭──────────────────────────────────────────────────────╮
│              Comparação (10.000 elementos)           │
├──────────────┬──────────┬────────┬──────────┬────────┤
│ Algoritmo    │ Tempo    │ CPU    │ Energia  │ CO2    │
├──────────────┼──────────┼────────┼──────────┼────────┤
│ Merge Sort   │ 0.012448 │ 87.48  │ 0.000039 │ 0.0166 │
│ Quick Sort   │ 0.009974 │ 83.19  │ 0.000015 │ 0.0064 │
│ Bubble Sort  │ 1.750150 │ 99.86  │ 0.031550 │ 13.440 │
│ Insertion    │ 0.146610 │ 98.65  │ 0.002610 │ 1.1119 │
╰──────────────┴──────────┴────────┴──────────┴────────╯
```

---

## Funcionalidades Extras (Bonificação)

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

## Equipe

- **Paulo Victor**
- **Diego Guedes**
- **Rafael Simões de Paula**
- **Kawan Ubirajara Dos Santos Dias Borges**
- **Carlos Eduardo Pereira Dos Santos**
- **Gabriel de Medeiros Matos**

---

## Links Úteis

- **Ollama**: https://ollama.ai
- **IEA Emissions Report**: https://www.iea.org/reports/electricity-2025/emissions
- **Python psutil**: https://psutil.readthedocs.io/
- **Rich Documentation**: https://rich.readthedocs.io/

---
