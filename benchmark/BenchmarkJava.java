import java.util.Random;
import java.lang.management.ManagementFactory;
import com.sun.management.OperatingSystemMXBean;

public class BenchmarkJava {
    
    // ============================================
    // ALGORITMOS DE ORDENAÇÃO
    // ============================================
    
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
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
    
    public static void insertionSort(int[] arr) {
        int n = arr.length;
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
    
    public static void merge(int[] arr, int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;
        int[] L = new int[n1];
        int[] R = new int[n2];
        
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
    }
    
    public static void mergeSortRec(int[] arr, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;
            mergeSortRec(arr, l, m);
            mergeSortRec(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }
    
    public static void mergeSort(int[] arr) {
        mergeSortRec(arr, 0, arr.length - 1);
    }
    
    public static int partition(int[] arr, int low, int high) {
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
    
    public static void quickSortRec(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSortRec(arr, low, pi - 1);
            quickSortRec(arr, pi + 1, high);
        }
    }
    
    public static void quickSort(int[] arr) {
        quickSortRec(arr, 0, arr.length - 1);
    }
    
    // ============================================
    // MEDIÇÃO DE DESEMPENHO
    // ============================================
    
    public static double[] calcularImpacto(double tempo, double cpuPercent) {
        double TDP_CPU = 65.0;  // Watts
        double usoCpuDecimal = cpuPercent / 100.0;
        double potenciaW = TDP_CPU * usoCpuDecimal;
        double energia = (potenciaW * tempo) / 3600.0;  // Wh
        double fatorEmissao = 0.233;  // kg CO2/kWh (média Brasil)
        double co2 = (energia / 1000.0) * fatorEmissao * 1000.0;  // gramas
        return new double[]{energia, co2};
    }
    
    // ============================================
    // MAIN - EXECUTA BENCHMARKS
    // ============================================
    
    public static void main(String[] args) {
        String[] algoritmos = {"merge", "quick", "bubble", "insertion"};
        int[] tamanhos = {1000, 10000, 100000};
        int numExecucoes = 50;
        
        OperatingSystemMXBean osBean = ManagementFactory.getPlatformMXBean(OperatingSystemMXBean.class);
        
        System.out.println("BENCHMARKS_JAVA = {");
        
        for (int a = 0; a < algoritmos.length; a++) {
            String alg = algoritmos[a];
            System.out.println("    \"" + alg + "\": {");
            
            for (int t = 0; t < tamanhos.length; t++) {
                int tamanho = tamanhos[t];
                
                double somaTempo = 0.0;
                double somaCpu = 0.0;
                double somaEnergia = 0.0;
                double somaCo2 = 0.0;
                
                System.err.println("[Java] Executando " + alg + " com " + tamanho + " elementos (50x)...");
                
                // Warm-up da JVM (5 execuções)
                for (int w = 0; w < 5; w++) {
                    int[] arrWarmup = new int[tamanho];
                    Random randWarmup = new Random();
                    for (int i = 0; i < tamanho; i++) {
                        arrWarmup[i] = randWarmup.nextInt(10000);
                    }
                    if (alg.equals("merge")) mergeSort(arrWarmup);
                    else if (alg.equals("quick")) quickSort(arrWarmup);
                }
                
                // Execuções reais
                for (int exec = 0; exec < numExecucoes; exec++) {
                    // Gerar lista aleatória
                    int[] arr = new int[tamanho];
                    Random rand = new Random(System.nanoTime() + exec * 1000);
                    for (int i = 0; i < tamanho; i++) {
                        arr[i] = rand.nextInt(10000);
                    }
                    
                    // Forçar garbage collection
                    System.gc();
                    
                    // Medir CPU antes
                    double cpuAntes = osBean.getProcessCpuLoad() * 100.0;
                    
                    // Medir tempo
                    long inicio = System.nanoTime();
                    
                    // Executar algoritmo
                    switch (alg) {
                        case "merge":
                            mergeSort(arr);
                            break;
                        case "quick":
                            quickSort(arr);
                            break;
                        case "bubble":
                            bubbleSort(arr);
                            break;
                        case "insertion":
                            insertionSort(arr);
                            break;
                    }
                    
                    long fim = System.nanoTime();
                    
                    // Medir CPU depois
                    double cpuDepois = osBean.getProcessCpuLoad() * 100.0;
                    
                    double tempoTotal = (fim - inicio) / 1_000_000_000.0;
                    double cpuPercent = (cpuAntes + cpuDepois) / 2.0;
                    if (cpuPercent < 0) cpuPercent = 50.0;  // Fallback
                    if (cpuPercent > 100.0) cpuPercent = 100.0;
                    
                    double[] impacto = calcularImpacto(tempoTotal, cpuPercent);
                    double energia = impacto[0];
                    double co2 = impacto[1];
                    
                    somaTempo += tempoTotal;
                    somaCpu += cpuPercent;
                    somaEnergia += energia;
                    somaCo2 += co2;
                }
                
                // Calcular médias
                double mediaTempo = somaTempo / numExecucoes;
                double mediaCpu = somaCpu / numExecucoes;
                double mediaEnergia = somaEnergia / numExecucoes;
                double mediaCo2 = somaCo2 / numExecucoes;
                
                System.out.printf("        %d: {\"tempo\": %.6f, \"cpu\": %.2f, \"energia\": %.6f, \"co2\": %.4f}%s\n",
                    tamanho, mediaTempo, mediaCpu, mediaEnergia, mediaCo2,
                    (t < tamanhos.length - 1) ? "," : "");
            }
            
            System.out.println("    }" + (a < algoritmos.length - 1 ? "," : ""));
        }
        
        System.out.println("}");
    }
}