#pragma once
#include <iostream>
#include "SDL.h"
#include "constants.h"
#include "Piece.h"

#define fillInRect(renderPointer, rect) SDL_RenderFillRect(renderPointer, &rect)
#define drawRect(renderPointer) SDL_RenderPresent(renderPointer)
#define updateDisplay(window) SDL_UpdateWindowSurface(window);

class Game
{
private:
	void init();

	//Pointers for the window and the renderer to use later
	SDL_Window* window;
	SDL_Renderer* renderer;
	SDL_Surface* screen;
	SDL_Event event;

	//This function will draw rectangles to the screen.
	void drawRectangle();

public:
	//Named constants for the screen width and height of the game
	const int SCREEN_WIDTH = 1000;
	const int SCREEN_HEIGHT = 800;

	//Array of pieces that represents the board
	Piece* board[8][8];

	//member variables
	bool gameIsRunning = true;

	//This variable will represent if the game is running or not
	bool running = true;

	//This function creates the game
	void mainloop();

	//This function cleans up the code after the game is quit
	void cleanUp();

	//This function is responsible for displaying the board.
	void displayBoard();

	//This function will display the pieces on the board.
	void displayPieces();

	//constructor
	Game(){}

	//destructor
	~Game();
};