#include <iostream>
#include <fstream>
#include <string>

void loadGame(const std::string& filePath) {
    std::ifstream file(filePath);
    if (file.is_open()) {
        std::string gameData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        std::cout << "Loaded game data: " << gameData << std::endl;
    }
    else {
        std::cout << "Game file not found." << std::endl;
    }
}