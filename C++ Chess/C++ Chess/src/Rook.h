#pragma once
#include "Piece.h"

class Rook : public Piece
{
public:

	Rook(int row, int col, int color);

	~Rook();

	//Version of move calculation for Rooks
	void calculateLegalMoves(Piece* Board[ROWS][COLS]) override;
};