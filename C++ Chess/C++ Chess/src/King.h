#pragma once
#include "Piece.h"

class King : public Piece
{
public:

	King(int row, int col, int color);

	~King();

	//Legal move calculation for the king
	void calculateLegalMoves(Piece* board[ROWS][COLS]) override;

};