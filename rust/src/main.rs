use regex::Regex;
use std::process::Command;

fn main() {
    let res = xrandr();
    let lines: Vec<&str>;
    match res.ok() {
        Some(output) => {
            lines = output.split("\n").collect();

            match_line(lines[1]);
            let filter_lines: Vec<&str> = lines.into_iter().collect();
            println!("filtered");
            println!("{:?}", filter_lines);
        }
        None => println!("test"),
    }
}

fn xrandr() -> Result<String, ()> {
    let output = Command::new("xrandr")
        .output()
        .expect("failed to execute process");

    let res = String::from_utf8_lossy(&output.stdout).to_string();

    Ok(res)
}

fn match_line(line: &str) {
    println!("{:?}", line);

    let re = Regex::new(r"(.*) (connected) (.*)").unwrap();
    if let Some(caps) = re.captures(line) {
        let cap = caps.get(1).unwrap().as_str();
        println!("Display: {}", cap);
    }
}
