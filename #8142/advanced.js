//Fungsi yang dipanggil secara recusif
function incrementCube(i) {
  // Guard untuk memberhentikan panggilan recursive
  if (i === 0) return;
  //Panggil sekarang karena kita akan menggunakan angka dari 1 - n bukan sebaliknya
  incrementCube(i - 1);
  //proses ini akan dijalankan setelah proses diatas beres
  console.log(`Current Number is : ${i} and the cube is ${i ** 3}`);
}
//Jalankan fungsinya
incrementCube(6);
