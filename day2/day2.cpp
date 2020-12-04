#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

int parse_start(std::string pass) {
    return std::stoi(pass.substr(0,1));
}

int parse_end(std::string pass) {
    std::size_t pos = pass.find("-");
    return std::stoi(pass.substr(pos));
}

std::string parse_char(std::string pass) {
    std::size_t pos = pass.find(" ");
    return pass.substr(pos);
}

std::string parse_pass(std::string pass) {
    std::size_t pos = pass.find(": ");
    return pass.substr(pos);
}

bool is_valid_pass(std::string pass) {
    // define policies
    int pol_start{-1};
    int pol_end{-1};
    std::string pol_char{" "};
    std::string pol_pass{" "};
    // parse password
    pol_start = parse_start(pass);
    pol_end = parse_end(pass);
    pol_char = parse_char(pass);
    pol_pass = parse_pass(pass);

    char pol_char_2[pol_char.size() + 1];

    pol_char.copy(pol_char_2, pol_char.size() + 1);
    
    std::cout << pol_char_2;

    const char pol_char_3 = *pol_char_2;

    int pol_count = std::count(
        pol_pass.begin(), 
        pol_pass.end(), 
        pol_char_3
    );

    

    if(pol_count >= pol_start && pol_count < pol_end) {
        return true;
    };
    return false;
}


int main(){

    // For testing purposes
    std::vector<std::string> examplelst{
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc"
    };
    //assert();
    
    int valid_count{0};

    std::string inpt;

    std::ifstream infile("input.txt");

    if (!infile.is_open()) {
        std::cout << "failed to open " << '\n';
        return 1;
    }

    while(std::getline(infile, inpt)) {
        if(!is_valid_pass(inpt)) valid_count++;
    }

    std::cout << "Number of valid passwords: "
    << valid_count << std::endl;

    return 0;
}