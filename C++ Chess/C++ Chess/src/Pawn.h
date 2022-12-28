#pragma once
#include "Piece.h"

class Pawn : public Piece
{
public:

	Pawn(int row, int col, int color);

	~Pawn();

	//Will track if the pawn does the double pawn jump as their first move.
	bool jumpedTwoTiles = false;

	//method to calculate the legal moves for a pawn
	void calculateLegalMoves(Piece* board[ROWS][COLS]) override;
};