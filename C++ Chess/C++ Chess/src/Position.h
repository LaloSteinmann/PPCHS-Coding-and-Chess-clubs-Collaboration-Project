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
};