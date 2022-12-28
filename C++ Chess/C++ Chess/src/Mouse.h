#pragma once
#include "Piece.h"
#include "Position.h"
#include <list>

using std::list;

class Mouse
{
public:
	Mouse();

	~Mouse();

	//Coordinates of the piece when clicked
	Position mouseCoordinates;

	//clicked row and columns
	int clickedRow;
	int clickedCol;

	//offset for clicking the x coordinate of the center of the piece
	int mouseColOffset = -(TILE_SIZE * (0.25 * 0.5));

	//offset for clicking the y coordinate of the center of the piece
	int mouseRowOffset = -(TILE_SIZE * (0.25 * 0.5));

	//The piece being dragged
	Piece* piece;

	//tracks if a piece is being dragged
	bool draggingPiece;

	//Checks if a move is in the piece's valid moves
	bool inMoveVector(Position moveToCheck, vector<Position> &legalMoves);

	//This function will be responsible for making moves. 
	//If the move is valid, then it will return true, otherwise, false
	bool move(Piece* board[ROWS][COLS], list<Piece*> &activePieces);

	//This function will drop the piece after it's done being dragged
	void dropPiece(int& turn, Piece* board[ROWS][COLS], list<Piece*> &activePieces);

	//This function will drag the piece and update the curret piece being dragged
	void dragPiece(Piece* clickedPiece);

	//This function will save the initial position of the dragged piece
	void saveInitialPos(int col, int row);

	//saves inital position of the piece
	void savePiecePos(int col, int row);
};