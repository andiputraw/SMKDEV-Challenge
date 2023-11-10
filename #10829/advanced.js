//fungsi untuk men-kuadrat-kan setiap satuan di sebuah angka
/**
 *
 * @param {number} number angka yang ingin dicari jumlah dari kuadrat setiap satuan
 * @returns {number} hasil dari penjumlahan tersebut
 */
function square_each_unit(number) {
  return (
    number
      //ubah angka nya jadi string
      .toString()
      //pecah setiap angkanya
      .split("")
      //gunakan fungsi reduce untuk menjumlahkan hasil dari mengkuadratkan setiap satuan
      .reduce((pre, curr) => pre + curr ** 2, 0)
  );
}
//fungsi untuk mencari tahu jika angka yang diberikan apakah "bahagia" atau tidak
/**
 *
 * @param {number} number angka yang di test
 * @returns {boolean} apakah angka bahagia atau tidak
 */
function happy_number(number) {
  // buat variable baru untuk menyimpan angka, karena number akan di modifikasi
  let result = number;
  // jika result adalah dibawah 5, maka kita bisa tahu jika angka itu bahagia atau tidak
  while (result > 5) {
    // opsional jika ingin tahu hasil dari setiap kalkulasi
    // console.log(result);
    // reassign dengan hasil dari kuadrat setiap satuan
    result = square_each_unit(result);
  }
  //jika result adalah 1, angka tersebut adalah bahagia
  if (result === 1) return true;
  // jika tidak maka angka bukan bahagia
  // tidak perlu else, karena kita sudah melakukan "return" di line sebelumnya
  return false;
}

const isHappy = happy_number(19);

console.log(isHappy);
