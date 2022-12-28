#include "Rook.h"

Rook::Rook(int row, int col, int color) : Piece(row, col, 5, color)
{
	if (color == WHITE)
	{
		setImage("assets/white_rook80x80.png");
	}
	else
	{
		setImage("assets/black_rook80x80.png");
	}
}

Rook::~Rook(){}

void Rook::calculateLegalMoves(Piece* board[ROWS][COLS])
{
	//The way the rook moves
	Position moveSet[] =
	{
		{1, 0},
		{-1, 0},
		{0, 1},
		{0, -1}
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