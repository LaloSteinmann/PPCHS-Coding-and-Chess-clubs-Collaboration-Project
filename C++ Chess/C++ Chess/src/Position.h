#pragma once

struct Position
{
	int x;
	int y;

	Position()
	{}

	Position(int col, int row)
	{
		x = col;
		y = row;
	}

	bool operator == (const Position compare)
	{
		if (x == compare.x && y == compare.y)
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	Position operator + (const Position toAdd)
	{
		Position newPos;
		newPos.x = x + toAdd.x;
		newPos.y = y + toAdd.y;

		return newPos;
	}

	//checks if a row and column are within the board
	bool validCoordinate()
	{
		if ((x >= 0 && x < 8) && (y >= 0 && y < 8))
		{
			return true;
		}
		return false;
	}
};
