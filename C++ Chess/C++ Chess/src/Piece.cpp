#include "Piece.h"
#include "constants.h"
#include <iostream>
#include "SDL_image.h"

//Initializer list and constructor for the Piece parent class
Piece::Piece(int row, int col, int value, int color): value(value), color(color)
{
	coordinates.x = col;
	coordinates.y = row;

	if (color == WHITE)
	{
		direction = -1;
	}
	else
	{
		direction = 1;
	}
}

Piece::~Piece()
{}

void Piece::calculateLegalMoves(Piece* board[ROWS][COLS])
{
	std::cout << "Legal moves calculation for a default Piece object ... Calculation failed";
}

void Piece::setImage(const char* fileName)
{
	file = fileName;
	image = IMG_Load(fileName);
}

SDL_Surface* Piece::getImage()
{
	return image;
}

const char* Piece::getFileName()
{
	return file;
}