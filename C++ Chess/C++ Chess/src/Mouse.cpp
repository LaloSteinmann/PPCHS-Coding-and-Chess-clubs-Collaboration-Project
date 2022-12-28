#include "Mouse.h"

Mouse::Mouse()
{}

Mouse::~Mouse(){}

bool Mouse::inMoveVector(Position moveToCheck, vector<Position> &legalMoves)
{
	for (Position move : legalMoves)
	{
		if (moveToCheck == move)
		{
			return true;
		}
	}
	return false;
}

void Mouse::dragPiece(Piece* clickedPiece)
{
	draggingPiece = true;
	piece = clickedPiece;
}

void Mouse::dropPiece(int& turn, Piece* board[ROWS][COLS], list<Piece*> &activePieces)
{
	if (move(board, activePieces))
	{
		turn++;
	}
	draggingPiece = false;
	piece = nullptr;
}

bool Mouse::move(Piece* board[ROWS][COLS], list<Piece*> &activePieces)
{
	int currentRow = int(mouseCoordinates.y / TILE_SIZE);
	int currentCol = int(mouseCoordinates.x / TILE_SIZE);

	if (piece)
	{
		if (inMoveVector({ currentCol, currentRow }, piece->legalMoves))
		{
			if (board[currentRow][currentCol] && board[currentRow][currentCol]->color != piece->color)
			{
				activePieces.remove(board[currentRow][currentCol]);
			}

			board[piece->coordinates.y][piece->coordinates.x] = nullptr;
			board[currentRow][currentCol] = piece;

			piece->coordinates.y = currentRow;
			piece->coordinates.x = currentCol;

			piece->moved = true;

			return true;
		}
	}
}

void Mouse::savePiecePos(int col, int row)
{
	piece->coordinates.x = col;
	piece->coordinates.y = row;
}