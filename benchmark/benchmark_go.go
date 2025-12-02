package main

import (
	"fmt"
	"math/rand"
	"os"
	"runtime"
	"time"
)

// ============================================
// ALGORITMOS DE ORDENAÇÃO
// ============================================

func bubbleSort(arr []int) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
}

func insertionSort(arr []int) {
	for i := 1; i < len(arr); i++ {
		chave := arr[i]
		j := i - 1
		for j >= 0 && arr[j] > chave {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = chave
	}
}

func merge(arr []int, l, m, r int) {
	n1 := m - l + 1
	n2 := r - m
	L := make([]int, n1)
	R := make([]int, n2)

	for i := 0; i < n1; i++ {
		L[i] = arr[l+i]
	}
	for j := 0; j < n2; j++ {
		R[j] = arr[m+1+j]
	}

	i, j, k := 0, 0, l
	for i < n1 && j < n2 {
		if L[i] <= R[j] {
			arr[k] = L[i]
			i++
		} else {
			arr[k] = R[j]
			j++
		}
		k++
	}

	for i < n1 {
		arr[k] = L[i]
		i++
		k++
	}

	for j < n2 {
		arr[k] = R[j]
		j++
		k++
	}
}

func mergeSortRec(arr []int, l, r int) {
	if l < r {
		m := l + (r-l)/2
		mergeSortRec(arr, l, m)
		mergeSortRec(arr, m+1, r)
		merge(arr, l, m, r)
	}
}

func mergeSort(arr []int) {
	mergeSortRec(arr, 0, len(arr)-1)
}

func partition(arr []int, low, high int) int {
	pivot := arr[high]
	i := low - 1

	for j := low; j < high; j++ {
		if arr[j] <= pivot {
			i++
			arr[i], arr[j] = arr[j], arr[i]
		}
	}

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i + 1
}

func quickSortRec(arr []int, low, high int) {
	if low < high {
		pi := partition(arr, low, high)
		quickSortRec(arr, low, pi-1)
		quickSortRec(arr, pi+1, high)
	}
}

func quickSort(arr []int) {
	quickSortRec(arr, 0, len(arr)-1)
}

// ============================================
// MEDIÇÃO DE DESEMPENHO
// ============================================

func calcularImpacto(tempo float64, cpuPercent float64) (float64, float64) {
	TDP_CPU := 65.0 // Watts
	usoCpuDecimal := cpuPercent / 100.0
	potenciaW := TDP_CPU * usoCpuDecimal
	energia := (potenciaW * tempo) / 3600.0           // Wh
	fatorEmissao := 0.233                             // kg CO2/kWh (média Brasil)
	co2 := (energia / 1000.0) * fatorEmissao * 1000.0 // gramas
	return energia, co2
}

// ============================================
// MAIN - EXECUTA BENCHMARKS
// ============================================

func main() {
	algoritmos := []string{"merge", "quick", "bubble", "insertion"}
	tamanhos := []int{1000, 10000, 100000}
	numExecucoes := 50

	fmt.Println("BENCHMARKS_GO = {")

	for a, alg := range algoritmos {
		fmt.Printf("    \"%s\": {\n", alg)

		for t, tamanho := range tamanhos {
			var somaTempo float64
			var somaCpu float64
			var somaEnergia float64
			var somaCo2 float64

			fmt.Fprintf(os.Stderr, "[Go] Executando %s com %d elementos (50x)...\n", alg, tamanho)

			for exec := 0; exec < numExecucoes; exec++ {
				// Gerar lista aleatória
				arr := make([]int, tamanho)
				rand.Seed(time.Now().UnixNano() + int64(exec)*1000)
				for i := 0; i < tamanho; i++ {
					arr[i] = rand.Intn(10000)
				}

				// Forçar garbage collection
				runtime.GC()

				// Medir tempo
				inicio := time.Now()

				// Executar algoritmo
				switch alg {
				case "merge":
					mergeSort(arr)
				case "quick":
					quickSort(arr)
				case "bubble":
					bubbleSort(arr)
				case "insertion":
					insertionSort(arr)
				}

				duracao := time.Since(inicio)
				tempoTotal := duracao.Seconds()

				// Estimar CPU (Go não tem API nativa fácil)
				// Estimativa baseada no tamanho e algoritmo
				var cpuPercent float64
				if tamanho <= 1000 {
					cpuPercent = 45.0
				} else if tamanho <= 10000 {
					cpuPercent = 60.0
				} else {
					cpuPercent = 75.0
				}

				// Ajustar baseado no algoritmo
				switch alg {
				case "merge", "quick":
					cpuPercent *= 0.9
				case "bubble", "insertion":
					cpuPercent *= 1.1
				}

				if cpuPercent > 100.0 {
					cpuPercent = 100.0
				}

				energia, co2 := calcularImpacto(tempoTotal, cpuPercent)

				somaTempo += tempoTotal
				somaCpu += cpuPercent
				somaEnergia += energia
				somaCo2 += co2
			}

			// Calcular médias
			mediaTempo := somaTempo / float64(numExecucoes)
			mediaCpu := somaCpu / float64(numExecucoes)
			mediaEnergia := somaEnergia / float64(numExecucoes)
			mediaCo2 := somaCo2 / float64(numExecucoes)

			virgula := ","
			if t == len(tamanhos)-1 {
				virgula = ""
			}

			fmt.Printf("        %d: {\"tempo\": %.6f, \"cpu\": %.2f, \"energia\": %.6f, \"co2\": %.4f}%s\n",
				tamanho, mediaTempo, mediaCpu, mediaEnergia, mediaCo2, virgula)
		}

		virgula := ","
		if a == len(algoritmos)-1 {
			virgula = ""
		}
		fmt.Printf("    }%s\n", virgula)
	}

	fmt.Println("}")
}
