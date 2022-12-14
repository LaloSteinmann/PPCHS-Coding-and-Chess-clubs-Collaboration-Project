#include "SDL.h"
#include "Position.h"
#include "constants.h"
#include <vector>
#pragma once

using std::vector;

class Piece
{
private:
	//Will contain the image of the piece
	SDL_Surface* image;

	//The value of the piece
	int value;

	//What direction the piece will move in relative to making its way across the screen
	int direction;

public:
	Piece(int row, int col, int value, int color);

	~Piece();

	//These variables will store the current position of the piece.
	int row;
	int col;
	Position coordinates;

	//This will contain all the legal moves for a piece at a given moment
	vector<Position> legalMoves;

	//Token string to make adding a move easier and clearer
	#define addMove(move) legalMoves.push_back(move);

	//Will represent the alliance of the piece.
	int color;

	//This function will calculate all the possible moves for a specific piece
	virtual void calculateLegalMoves(Piece* board[ROWS][COLS]);

	//Whether or not the piece has moved
	bool moved = false;

	//This function will change the surface pointer to change the image of the bishop
	void setImage(const char*);
};