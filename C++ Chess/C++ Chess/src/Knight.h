#pragma once
#include "Piece.h"

class Knight : public Piece
{
public:

	Knight(int row, int col, int color);

	~Knight();

	//To be the version of legal move calculation for knights
	void calculateLegalMoves(Piece* board[ROWS][COLS]) override;
};