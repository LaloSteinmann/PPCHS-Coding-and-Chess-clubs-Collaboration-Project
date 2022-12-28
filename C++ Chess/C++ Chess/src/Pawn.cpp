#include "Pawn.h"
#include <typeinfo>

Pawn::Pawn(int row, int col, int color) : Piece(row, col, 1, color)
{
	if (color == WHITE)
	{
		setImage("assets/white_pawn80x80.png");
	}
	else
	{
		setImage("assets/black_pawn80x80.png");
	}
}

Pawn::~Pawn(){}

void Pawn::calculateLegalMoves(Piece* board[ROWS][COLS])
{
	int rightEnPassantCol = coordinates.x + 1;
	int leftEnPassantCol = coordinates.x - 1;

	//En passant
	if ((color == WHITE && coordinates.y == 3) || (color == BLACK && coordinates.y == 4))
	{
		//Right en passant
		if (validRowAndCol(rightEnPassantCol, coordinates.y))
		{
			if (board[coordinates.y][rightEnPassantCol] && board[coordinates.y][rightEnPassantCol]->color != color && typeid(this) == typeid(board[coordinates.y][rightEnPassantCol]))
			{
				legalMoves.push_back({ rightEnPassantCol, coordinates.y + direction });
			}
		}

		//Left en passant
		if (validRowAndCol(leftEnPassantCol, coordinates.y))
		{
			if (board[coordinates.y][leftEnPassantCol] && board[coordinates.y][leftEnPassantCol]->color != color && typeid(this) == typeid(board[coordinates.y][leftEnPassantCol]))
			{
				legalMoves.push_back({ leftEnPassantCol, coordinates.y + direction });
			}
		}
	}

	//Initial pawn jump
	else if (!moved && validRowAndCol(coordinates.x, coordinates.y + (2 * direction)))
	{
		int initialPawnJump = coordinates.y + (2 * direction);

		if (!board[initialPawnJump][coordinates.x] && !board[coordinates.y + direction][coordinates.x])
		{
			legalMoves.push_back({ coordinates.x, initialPawnJump });
		}
	}

	//Regular pawn jump
	if (validRowAndCol(coordinates.x, coordinates.y + direction))
	{
		if (!board[coordinates.y + direction][coordinates.x])
		{
			legalMoves.push_back({ coordinates.x, coordinates.y + direction });
		}
	}

	//Right diagonal capture
	if (validRowAndCol(coordinates.x + 1, coordinates.y + direction))
	{
		if (board[coordinates.y + direction][coordinates.x + 1] && board[coordinates.y + direction][coordinates.x + 1]->color != color)
		{
			legalMoves.push_back({ coordinates.x + 1, coordinates.y + direction });
		}
	}

	//Left diagonal capture
	if (validRowAndCol(coordinates.x - 1, coordinates.y + direction))
	{
		if (board[coordinates.y + direction][coordinates.x - 1] && board[coordinates.y + direction][coordinates.x - 1]->color != color)
		{
			legalMoves.push_back({ coordinates.x - 1, coordinates.y + direction });
		}
	}
}