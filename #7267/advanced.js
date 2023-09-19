const filterPrimeRange = (start, end) =>
  Array.from({ length: end - start }, (_, i) => start + i).filter(
    (v) => v % 2 != 0 && v % 3 != 0 && v % 5 != 0 && v % 7 != 0
  );

console.log(filterPrimeRange(30, 50));
