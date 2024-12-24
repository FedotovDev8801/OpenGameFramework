package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

// Struct to hold game data
type Game struct {
	Name    string `json:"name"`
	Version string `json:"version"`
}

func loadGameData(filename string) (*Game, error) {
	// Load game data from a JSON file
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}

	var game Game
	err = json.Unmarshal(data, &game)
	if err != nil {
		return nil, err
	}

	return &game, nil
}

func handler(w http.ResponseWriter, r *http.Request) {
	// HTTP handler to serve game data
	game, err := loadGameData("game.json")
	if err != nil {
		http.Error(w, "Failed to load game data", http.StatusInternalServerError)
		return
	}

	json.NewEncoder(w).Encode(game)
}

func main() {
	// Start an HTTP server
	http.HandleFunc("/game", handler)
	fmt.Println("Server is running on port 8080")
	http.ListenAndServe(":8080", nil)
}
