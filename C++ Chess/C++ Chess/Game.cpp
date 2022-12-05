#include "SDL.h"
#include <iostream>

using string = std::string;

class Game 
{
public:
	//Named constants for the screen width and height of the game
	const int SCREEN_WIDTH = 800;
	const int SCREEN_HEIGHT = 1000;

	//Pointers for the window and the renderer to use later
	SDL_Window* window;
	SDL_Renderer* renderer;

	//This variable will represent if the game is running or not
	bool running = true;

	// = SDL_CreateWindow("Chess", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 1000, 0);

	//This function creates the game
	void init();

	//This function cleans up the code after the game is quit
	void cleanUp();

	//This function is responsible for setting up the board.
	void displayBoard();

	//This function will display the pieces on the board.
	void displayPieces(string fileName);

	//constructor
	Game(string gameName);

	//destructor
	~Game();
};