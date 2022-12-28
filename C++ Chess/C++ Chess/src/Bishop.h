#pragma once
#include "Piece.h"

class Bishop: public Piece
{
public:

	Bishop(int row, int col, int color);

	~Bishop();

	//Version of move calculation for Bishops
	void calculateLegalMoves(Piece* Board[ROWS][COLS]) override;
};