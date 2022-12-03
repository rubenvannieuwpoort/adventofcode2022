use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    // Create a path to the desired file
    let path = Path::new("input.txt");
    //let display = path.display();

    // Read the file contents into a string, returns `io::Result<usize>`
    let file = File::open(path).unwrap();
    let buf_reader: std::io::BufReader<File> = std::io::BufReader::new(file);
    let lines: std::vec::Vec<i32> = buf_reader.lines().map(|l| l.unwrap().parse::<i32>().unwrap()).collect();
    //for line in lines {
    //    println!("{}", line);
    //}

    for n in 1..lines.len()-1 {
        if lines[n] > lines[n - 1] {
            println!("{} is bigger", n);
        }
    }

    // `file` goes out of scope, and the "hello.txt" file gets closed
}
