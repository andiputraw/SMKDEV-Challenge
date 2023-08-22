/// Ada dua jawaban untuk challenge ini
/// Pertama. melalui pendekatan imperative
/// dan kedua. menggunakan pendekatan functional/declarative
/// 
/// Pertanyaan
/// 5 4 3 2 1
/// 4 3 2 1
/// 3 2 1
/// 2 1
/// 1
/// Write a program to use for loop to print the following reverse number pattern

use std::time::Instant;

fn main(){
    //////////////
    // Imperative
    /////////////
    
    let now_imper = Instant::now();

    for i in (1..=5).rev() {
         for j in (1..=i).rev() {
             print!("{} ",j);
         }
         print!("\n");
     };

    println!("\nImperative Time elapsed: {} nano second", now_imper.elapsed().as_nanos());

    println!("\n//////////////////////////////////////\n");
    
    //////////////
    // Functional / Declarative
    /////////////

    const MAX_ITERATION: i32 = 5;

    let now_decl = Instant::now();

    (1..=MAX_ITERATION)
        .rev()
        .for_each(|x| {
        (1..=x).rev().for_each(print_num);
        print!("\n");
    });

    println!("\nFunctional Time elapsed: {} nano seconds", now_decl.elapsed().as_nanos());
}

fn print_num(number: i32){
    print!("{number} ");
}