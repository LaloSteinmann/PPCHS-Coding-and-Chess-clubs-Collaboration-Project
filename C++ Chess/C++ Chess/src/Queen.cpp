#include "Queen.h"

Queen::Queen(int row, int col, int color) : Piece(row, col, 9, color)
{
	if (color == WHITE)
	{
		setImage("assets/white_queen80x80.png");
	}
	else
	{
		setImage("assets/black_queen80x80.png");
	}
}

Queen::~Queen(){}

void Queen::calculateLegalMoves(Piece* board[ROWS][COLS])
{
	//The way the queen works
	Position moveSet[] =
	{
		{1, 0},
		{-1, 0},
		{0, 1 },
		{0, -1},
		{1, 1},
		{1, -1},
		{-1, -1},
		{-1, 1}
	};

	for (auto offset : moveSet)
	{
		Position newCoordinates = { coordinates.x, coordinates.y };

		while (validRowAndCol(newCoordinates.x, newCoordinates.y))
		{
			newCoordinates.x += offset.x;
			newCoordinates.y += (offset.y * direction);

			if (validRowAndCol(newCoordinates.x, newCoordinates.y))
			{
				if (!board[newCoordinates.y][newCoordinates.x])
				{
					legalMoves.push_back({ newCoordinates.x, newCoordinates.y });
				}
				else
				{
					if (board[newCoordinates.y][newCoordinates.x] && board[newCoordinates.y][newCoordinates.x]->color != color)
					{
						legalMoves.push_back({ newCoordinates.x, newCoordinates.y });
					}
					break;
				}
			}
		}
	}
}