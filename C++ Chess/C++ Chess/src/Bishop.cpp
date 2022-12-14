#include "Bishop.h"
#include "constants.h"
#include "SDL.h"
#include "SDL_image.h"

Bishop::Bishop(int row, int col, int color) : Piece(row, col, value, color)
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
	Position moveManner[] = 
	{
								Position(1, 1),
								Position(-1, 1),
								Position(1, -1),
								Position(-1, -1)
	};



}