import java.util.Random;

public class Ordenacao {
    
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
    
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Uso: java Ordenacao <algoritmo> <tamanho>");
            System.out.println("Algoritmos: bubble, insertion, merge, quick");
            return;
        }
        
        String algoritmo = args[0];
        int n = Integer.parseInt(args[1]);
        
        int[] arr = new int[n];
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            arr[i] = rand.nextInt(1000000);
        }
        
        long inicio = System.nanoTime();
        
        switch (algoritmo) {
            case "bubble":
                bubbleSort(arr);
                break;
            case "insertion":
                insertionSort(arr);
                break;
            case "merge":
                mergeSort(arr);
                break;
            case "quick":
                quickSort(arr);
                break;
            default:
                System.out.println("Algoritmo desconhecido");
                return;
        }
        
        long fim = System.nanoTime();
        double tempo = (fim - inicio) / 1_000_000_000.0;
        
        System.out.printf("%.6f\n", tempo);
    }
}