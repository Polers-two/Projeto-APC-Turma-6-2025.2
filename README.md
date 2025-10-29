## Grupo
- **Paulo Victor**
- **Diego Guedes**
- **Rafael Simões de Paula**
- **Kawan Ubirajara Dos Santos Dias Borges**
- **Carlos Eduardo Pereira Dos Santos**

---

## Especificação do Projeto

### Problema
O crescimento exponencial do uso de tecnologias e do desenvolvimento de softwares vem aumentando o **consumo global de energia elétrica**, especialmente em aplicações que demandam **grande poder computacional**, como algoritmos de ordenação massivos e **modelos de Inteligência Artificial (IA)**.

Apesar disso, muitos desenvolvedores e usuários desconhecem o **impacto ambiental** causado pela execução de algoritmos ineficientes, que consomem mais energia e geram maiores emissões de carbono.  
Esse desconhecimento impede a adoção de práticas de **programação sustentável**.

---

### Objetivo Geral
Desenvolver um sistema em **Python 3** que analisa e compara o **gasto energético estimado** de algoritmos comuns (como *Merge Sort*, *Quick Sort*, *Bubble Sort*, etc.) com implementações em outras linguagens de programação e, se possível, com modelos de IA de uso comum (como ChatGPT e LLaMA).

O sistema deve apresentar relatórios e gráficos que demonstrem como a **eficiência de algoritmos e linguagens impacta o meio ambiente**, incentivando práticas de **computação sustentável**.

---

### Objetivos Específicos
- Implementar um simulador que:
  - Meça o **tempo de execução** e o **uso de CPU** de diferentes algoritmos;
  - Converta esses dados em **consumo energético (kWh)** e **emissão de CO₂**;
  - Gere **gráficos comparativos** entre algoritmos e linguagens;
- Aplicar **conceitos de análise de complexidade** e **pensamento computacional**;
- Relacionar eficiência computacional com **sustentabilidade ambiental**;
- Utilizar **metodologia científica** para coleta e análise de dados reais;
- Exportar relatórios de resultados em formatos como **CSV** e **PNG**;
- Apresentar os resultados de forma visual, clara e replicável.

---

## ⚙️ Requisitos Funcionais
| ID | Descrição |
|----|------------|
| RF01 | Executar algoritmos clássicos de ordenação (Merge, Quick, Bubble, Insertion, Selection) |
| RF02 | Medir tempo de execução e uso de CPU |
| RF03 | Calcular consumo energético estimado (kWh) |
| RF04 | Calcular emissões de CO₂ e uso de água equivalentes |
| RF05 | Gerar gráficos comparativos de desempenho e energia |
| RF06 | Exportar resultados em formatos CSV e imagem |
| RF07 | Permitir comparação entre linguagens e modelos de IA |
| RF08 | Exibir resumo e relatório final de resultados |

---

## Requisitos Não Funcionais
- **Linguagem:** Python 3.10+  
- **Bibliotecas Principais:** `pandas`, `numpy`, `matplotlib`, `psutil`, `seaborn`  
- **Interface:** CLI (linha de comando) com visualização gráfica de resultados  
- **Código:** Modular, comentado e de fácil manutenção  
- **Documentação:** README completo, relatório metodológico e pôster de apresentação  

---

## Fórmulas e Cálculos Utilizados

**Energia estimada (kWh):**

E = (P_CPU × T) / 3600

onde:
- P_CPU = potência média da CPU (em watts)
- T = tempo de execução (em segundos)

**Emissão de CO₂ (g):**

CO₂ = E × 426

fonte: https://www.iea.org/reports/electricity-2025/emissions

(475 gCO₂/kWh é uma média global para geração elétrica)

---

## Metodologia Científica
1. **Problema:** Como a eficiência de diferentes algoritmos e linguagens influencia o consumo energético computacional?  
2. **Hipótese:** Algoritmos com menor complexidade consomem menos energia e emitem menos CO₂.  
3. **Coleta de Dados:** Medições de tempo de execução e uso de CPU em diferentes algoritmos e linguagens.  
4. **Cálculo Ambiental:** Conversão dos resultados em energia, CO₂ e água.  
5. **Análise:** Comparação entre algoritmos e visualização gráfica.  
6. **Conclusão:** Identificação de práticas e algoritmos mais sustentáveis.

---

