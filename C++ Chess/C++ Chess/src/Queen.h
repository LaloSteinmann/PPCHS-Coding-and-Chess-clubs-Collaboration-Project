#pragma once
#include "Piece.h"

class Queen : public Piece
{
public:
	Queen(int row, int col, int color);

	~Queen();

	void calculateLegalMoves(Piece* board[ROWS][COLS]) override;
};