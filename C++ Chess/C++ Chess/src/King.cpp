#include "King.h"

King::King (int row, int col, int color) : Piece(row, col, 9001, color)
{
	if (color == WHITE)
	{
		setImage("assets/white_king80x80.png");
	}
	else
	{
		setImage("assets/black_king80x80.png");
	}
}

King::~King(){}

void King::calculateLegalMoves(Piece* board[ROWS][COLS])
{
	Position moveSet[] =
	{
		{1, 0},
		{-1, 0},
		{0, direction},
		{0, -direction},
		{1, direction},
		{1, -direction},
		{-1, -direction},
		{-1, direction}
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