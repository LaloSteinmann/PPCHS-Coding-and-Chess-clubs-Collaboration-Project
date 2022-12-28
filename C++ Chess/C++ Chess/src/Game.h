#pragma once
#include <iostream>
#include <list>
#include "SDL.h"
#include "constants.h"
#include "Pawn.h"
#include "Knight.h"
#include "Bishop.h"
#include "Rook.h"
#include "Queen.h"
#include "King.h"
#include "Mouse.h"

using std::list;

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

	//Mouse object
	Mouse mouse;

	//Initial setup of white pieces
	Rook* wR1 = new Rook(WHITE_PIECE_ROW, 0, WHITE);
	Knight* wN1 = new Knight(WHITE_PIECE_ROW, 1, WHITE);
	Bishop* wB1 = new Bishop(WHITE_PIECE_ROW, 2, WHITE);
	Queen* wQ = new Queen(WHITE_PIECE_ROW, 3, WHITE);
	King* wK = new King(WHITE_PIECE_ROW, 4, WHITE);
	Bishop* wB2 = new Bishop(WHITE_PIECE_ROW, 5, WHITE);
	Knight* wN2 = new Knight(WHITE_PIECE_ROW, 6, WHITE);
	Rook* wR2 = new Rook(WHITE_PIECE_ROW, 7, WHITE);

	//Initial setup of white pawns
	Pawn* wP1 = new Pawn(WHITE_PAWN_ROW, 0, WHITE);
	Pawn* wP2 = new Pawn(WHITE_PAWN_ROW, 1, WHITE);
	Pawn* wP3 = new Pawn(WHITE_PAWN_ROW, 2, WHITE);
	Pawn* wP4 = new Pawn(WHITE_PAWN_ROW, 3, WHITE);
	Pawn* wP5 = new Pawn(WHITE_PAWN_ROW, 4, WHITE);
	Pawn* wP6 = new Pawn(WHITE_PAWN_ROW, 5, WHITE);
	Pawn* wP7 = new Pawn(WHITE_PAWN_ROW, 6, WHITE);
	Pawn* wP8 = new Pawn(WHITE_PAWN_ROW, 7, WHITE);

	//Initial setup of black pieces
	Rook* bR1 = new Rook(BLACK_PIECE_ROW, 0, BLACK);
	Knight* bN1 = new Knight(BLACK_PIECE_ROW, 1, BLACK);
	Bishop* bB1 = new Bishop(BLACK_PIECE_ROW, 2, BLACK);
	Queen* bQ = new Queen(BLACK_PIECE_ROW, 3, BLACK);
	King* bK = new King(BLACK_PIECE_ROW, 4, BLACK);
	Bishop* bB2 = new Bishop(BLACK_PIECE_ROW, 5, BLACK);
	Knight* bN2 = new Knight(BLACK_PIECE_ROW, 6, BLACK);
	Rook* bR2 = new Rook(BLACK_PIECE_ROW, 7, BLACK);

	//Initial setup of black pawns
	Pawn* bP1 = new Pawn(BLACK_PAWN_ROW, 0, BLACK);
	Pawn* bP2 = new Pawn(BLACK_PAWN_ROW, 1, BLACK);
	Pawn* bP3 = new Pawn(BLACK_PAWN_ROW, 2, BLACK);
	Pawn* bP4 = new Pawn(BLACK_PAWN_ROW, 3, BLACK);
	Pawn* bP5 = new Pawn(BLACK_PAWN_ROW, 4, BLACK);
	Pawn* bP6 = new Pawn(BLACK_PAWN_ROW, 5, BLACK);
	Pawn* bP7 = new Pawn(BLACK_PAWN_ROW, 6, BLACK);
	Pawn* bP8 = new Pawn(BLACK_PAWN_ROW, 7, BLACK);

	//Array of pieces that represents the board
	//Defined with initial setup of the board
	Piece* board[ROWS][COLS] = 
	{
		{bR1, bN1, bB1, bQ, bK, bB2, bN2, bR2},
		{bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8},
		{nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr},
		{nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr},
		{nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr},
		{nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr},
		{wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8},
		{wR1, wN1, wB1, wQ, wK, wB2, wN2, wR2}
	};

	//This list will contain all the current active pieces in the game
	list <Piece*> activePieces;

	//initializes the active piece list with all the pieces at the start of the game
	void initActivePieces();

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

	//This function will display the piece that is currently being dragged by the mouse
	void displayDraggedPiece();

	//This function will calculate all the legal moves for all the current pieces in the game
	void calculateAllMoves();

	//constructor
	Game();

	//destructor
	~Game();
};