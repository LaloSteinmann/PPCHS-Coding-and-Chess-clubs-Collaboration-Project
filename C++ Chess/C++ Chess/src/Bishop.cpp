#include "Bishop.h"
#include "constants.h"
#include "SDL.h"
#include "SDL_image.h"

Bishop::Bishop(int row, int col, int color) : Piece(row, col, 3.0001, color)
{
	if (color == WHITE)
	{
		setImage("assets/white_bishop80x80.png");
	}
	else
	{
		setImage("assets/black_bishop80x80.png");
	}
}

Bishop::~Bishop()
{}

void Bishop::calculateLegalMoves(Piece* board[ROWS][COLS])
{
	//The way the bishop moves
	Position moveSet[] = 
	{
		{1, 1},
		{1, -1},
		{-1, -1},
		{-1, 1}
	};

	for (auto offset : moveSet)
	{
		Position newCoordinates = {coordinates.x, coordinates.y};

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