package main

//Package yang dibutuhkan.
import (
	"fmt"
	"log"
	"math"
	"time"
)

//Entry Function
func main() {
	log.Println("INFO: Mulai menghitung")
	// Mulai Timestamp
	start := time.Now()
	// Mulai menghitung. silahkan masukan angka sebesar apapun
	// Note: Angka yang terlalu besar memungkinkan terjadinya integer overflow
	// https://en.wikipedia.org/wiki/Integer_overflow
	result := sumByN(5023)
	// Timestamp beres
	end := time.Since(start)
	
	// Log waktu yang diperlukan untuk menghitung
	// NOTE!!: Saking cepatnya komputer menghitung. jika angka yang dimasukan pada fungsi
	// sumByN terlalu kecil. waktu yang akan ditampilkan adalah 0 nanosecond
	log.Printf("INFO: Beres menghitung. Waktu yang digunakan: %d nanosecond", end.Nanoseconds())
	fmt.Println("Hasilnya adalah : ",result)
}

// Ini adalah fungsi recursif. yaitu fungsi yang memanggil dirinya sendiri
// sehingga kita dapat melakukan looping tanpa menggunakan for loop
func sumByN(num uint64) uint64 {
	// Tentukan "guard" atau batas dari fungsi recursif sehigga tidak terjadi stack overflow (infinity loopnya fungsi recursif)
	// https://en.wikipedia.org/wiki/Stack_overflow
	if num == 1 {
		return 2
	}
	// Disini kita panggil getNum2ByLength dan juga fungsi sumByN (dirinya sendiri) dengan parameter yang dikurangi 1
	return getNum2ByLength(num) + sumByN(num - 1 )
}

// Sama seperti fungsi sumByN fungsi ini adalah fungsi rekursif
func getNum2ByLength(num uint64) uint64 {
	// "guard" sama seperti fungsi sumByN
	if num == 1 {
		return 2
	}
	
	return 2 * uint64(math.Pow(10, float64(num - 1))) + getNum2ByLength(num - 1)
	// Untuk rumus memusingkan diatas. anggap saja inputnya adalah 3
	// 2 * 10^3-1 = 2 * 10^2 = 2 * 100   = 200  
	// 2 * 10^2-1 = 2 * 10^1 = 2 * 10    =  20  
	// Karena angka n disini adalah satu =   2
	// berdasarkan line 45               ----- +
	// maka angka outpunya adalah 2        222  
}
