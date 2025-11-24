package main

import (
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"time"
)

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

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Uso: go run ordenacao.go <algoritmo> <tamanho>")
		fmt.Println("Algoritmos: bubble, insertion, merge, quick")
		return
	}

	algoritmo := os.Args[1]
	n, _ := strconv.Atoi(os.Args[2])

	arr := make([]int, n)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < n; i++ {
		arr[i] = rand.Intn(1000000)
	}

	inicio := time.Now()

	switch algoritmo {
	case "bubble":
		bubbleSort(arr)
	case "insertion":
		insertionSort(arr)
	case "merge":
		mergeSort(arr)
	case "quick":
		quickSort(arr)
	default:
		fmt.Println("Algoritmo desconhecido")
		return
	}

	fim := time.Since(inicio)
	fmt.Printf("%.6f\n", fim.Seconds())
}