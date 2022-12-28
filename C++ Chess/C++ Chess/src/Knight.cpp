#include "Knight.h"

Knight::Knight(int row, int col, int color) : Piece(row, col, 3, color)
{
	if (color == WHITE)
	{
		setImage("assets/white_knight80x80.png");
	}
	else
	{
		setImage("assets/black_knight80x80.png");
	}
}

Knight::~Knight(){}

void Knight::calculateLegalMoves(Piece* board[ROWS][COLS])
{
	//The way the knight moves
	Position moveSet[8] = 
	{
		{2, direction},
		{-2, direction},
		{-2, -direction},
		{2, -direction},
		{1, direction * 2},
		{1, direction * -2},
		{-1, direction * -2},
		{-1, direction * 2}
	};

	for (auto offset : moveSet)
	{
		Position newCoordinates = coordinates + offset;

		if (validRowAndCol(newCoordinates.x, newCoordinates.y))
		{
			if (!board[newCoordinates.y][newCoordinates.x])
			{
				legalMoves.push_back(coordinates + offset);
			}
			else
			{
				if (board[newCoordinates.y][newCoordinates.x]->color != color)
				{
					legalMoves.push_back(coordinates + offset);
				}
			}
		}
	}
}