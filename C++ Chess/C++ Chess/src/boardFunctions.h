#pragma once
#include "constants.h"

inline bool validRowAndCol(int x, int y)
{
    if ((x >= 0 && x < 8) && (y >= 0 && y < 8))
    {
        return true;
    }
    return false;
}
