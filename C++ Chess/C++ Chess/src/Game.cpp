#include <iostream>
#include "Game.h"

Game::~Game()
{
    SDL_FreeSurface(screen);
    SDL_DestroyWindow(window);
    SDL_DestroyRenderer(renderer);
    SDL_Quit();
}

void Game::init()
{
    SDL_Init(SDL_INIT_VIDEO);


    //SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
    //SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED
    window = SDL_CreateWindow("Chess", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, 0);

    renderer = SDL_CreateRenderer(window, -1, 0);

    screen = SDL_GetWindowSurface(window);
}

void Game::displayBoard()
{
    for (int row = 0; row < ROWS; row++)
    {
        for (int col = 0; col < COLS; col++)
        {
            //Checks if the square is even
            if ((row + col) % 2 == 0)
            {
                //even and light square
                SDL_SetRenderDrawColor(renderer, 255, 211, 155, SDL_ALPHA_OPAQUE);
            }
            else
            {
                //odd and dark squares
                SDL_SetRenderDrawColor(renderer, 160, 82, 45, SDL_ALPHA_OPAQUE);
            }

            SDL_Rect tile = {col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE};

            fillInRect(renderer, tile);
            drawRect(renderer);
        }
    }
}

void Game::mainloop()
{
	Game::init();
    while (gameIsRunning)
    {
        displayBoard();

        while (SDL_WaitEvent(&event))
        {

            if (event.type == SDL_QUIT)
            {
                gameIsRunning = false;
                break;
            }

        }

        updateDisplay(window);
    }
}