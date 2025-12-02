#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// ============================================
// ALGORITMOS DE ORDENAÇÃO
// ============================================

void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void insertion_sort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int chave = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > chave) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = chave;
    }
}

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    int *L = malloc(n1 * sizeof(int));
    int *R = malloc(n2 * sizeof(int));
    
    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
    
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
    
    free(L);
    free(R);
}

void merge_sort_rec(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        merge_sort_rec(arr, l, m);
        merge_sort_rec(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

void merge_sort(int arr[], int n) {
    merge_sort_rec(arr, 0, n - 1);
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    
    return i + 1;
}

void quick_sort_rec(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quick_sort_rec(arr, low, pi - 1);
        quick_sort_rec(arr, pi + 1, high);
    }
}

void quick_sort(int arr[], int n) {
    quick_sort_rec(arr, 0, n - 1);
}

// ============================================
// MEDIÇÃO DE DESEMPENHO
// ============================================

double get_time() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec / 1e9;
}

void calcular_impacto(double tempo, double cpu_percent, double *energia, double *co2) {
    double TDP_CPU = 65.0;  // Watts
    double uso_cpu_decimal = cpu_percent / 100.0;
    double potencia_W = TDP_CPU * uso_cpu_decimal;
    *energia = (potencia_W * tempo) / 3600.0;  // Wh
    double fator_emissao = 0.233;  // kg CO2/kWh (média Brasil)
    *co2 = (*energia / 1000.0) * fator_emissao * 1000.0;  // gramas
}

// ============================================
// MAIN - EXECUTA BENCHMARKS
// ============================================

int main() {
    const char *algoritmos[] = {"merge", "quick", "bubble", "insertion"};
    int tamanhos[] = {1000, 10000, 100000};
    int num_algoritmos = 4;
    int num_tamanhos = 3;
    int num_execucoes = 50;
    
    printf("BENCHMARKS_C = {\n");
    
    for (int a = 0; a < num_algoritmos; a++) {
        const char *alg = algoritmos[a];
        printf("    \"%s\": {\n", alg);
        
        for (int t = 0; t < num_tamanhos; t++) {
            int tamanho = tamanhos[t];
            
            double soma_tempo = 0.0;
            double soma_cpu = 0.0;
            double soma_energia = 0.0;
            double soma_co2 = 0.0;
            
            fprintf(stderr, "[C] Executando %s com %d elementos (50x)...\n", alg, tamanho);
            
            for (int exec = 0; exec < num_execucoes; exec++) {
                // Gerar lista aleatória
                int *arr = malloc(tamanho * sizeof(int));
                srand(time(NULL) + exec * 1000);
                for (int i = 0; i < tamanho; i++) {
                    arr[i] = rand() % 10000;
                }
                
                // Medir tempo e CPU
                clock_t cpu_inicio = clock();
                double tempo_inicio = get_time();
                
                // Executar algoritmo
                if (strcmp(alg, "merge") == 0) {
                    merge_sort(arr, tamanho);
                } else if (strcmp(alg, "quick") == 0) {
                    quick_sort(arr, tamanho);
                } else if (strcmp(alg, "bubble") == 0) {
                    bubble_sort(arr, tamanho);
                } else if (strcmp(alg, "insertion") == 0) {
                    insertion_sort(arr, tamanho);
                }
                
                double tempo_fim = get_time();
                clock_t cpu_fim = clock();
                
                double tempo_total = tempo_fim - tempo_inicio;
                double cpu_time = (double)(cpu_fim - cpu_inicio) / CLOCKS_PER_SEC;
                double cpu_percent = (cpu_time / tempo_total) * 100.0;
                if (cpu_percent > 100.0) cpu_percent = 100.0;
                if (cpu_percent < 1.0) cpu_percent = 50.0;  // Fallback
                
                double energia, co2;
                calcular_impacto(tempo_total, cpu_percent, &energia, &co2);
                
                soma_tempo += tempo_total;
                soma_cpu += cpu_percent;
                soma_energia += energia;
                soma_co2 += co2;
                
                free(arr);
            }
            
            // Calcular médias
            double media_tempo = soma_tempo / num_execucoes;
            double media_cpu = soma_cpu / num_execucoes;
            double media_energia = soma_energia / num_execucoes;
            double media_co2 = soma_co2 / num_execucoes;
            
            printf("        %d: {\"tempo\": %.6f, \"cpu\": %.2f, \"energia\": %.6f, \"co2\": %.4f}%s\n",
                   tamanho, media_tempo, media_cpu, media_energia, media_co2,
                   (t < num_tamanhos - 1) ? "," : "");
        }
        
        printf("    }%s\n", (a < num_algoritmos - 1) ? "," : "");
    }
    
    printf("}\n");
    
    return 0;
}