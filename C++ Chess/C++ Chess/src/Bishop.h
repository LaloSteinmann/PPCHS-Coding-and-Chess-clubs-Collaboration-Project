#include "Piece.h"
#pragma once

class Bishop: public Piece
{
private:
	int value = 3;

public:

	Bishop(int row, int col, int color);

	~Bishop();

	//Version of move calculation for Bishops
	void calculateLegalMoves(Piece* Board[ROWS][COLS]) override;
};