#include <iostream>
#include "Game.h"
#include "SDL_image.h"

Game::Game(){}

Game::~Game()
{
    SDL_FreeSurface(screen);
    SDL_DestroyWindow(window);
    SDL_DestroyRenderer(renderer);

    //Deletes the array of pointers that represents the board
    //delete board;

    ////deletes all the white pieces
    //delete wR1;
    //delete wN1;
    //delete wB1;
    //delete wQ;
    //delete wK;
    //delete wB2;
    //delete wN2;
    //delete wR2;

    ////deletes all the white pawns
    //delete wP1;
    //delete wP2;
    //delete wP3;
    //delete wP4;
    //delete wP5;
    //delete wP6;
    //delete wP7;
    //delete wP8;

    ////deletes all the black pieces
    //delete bR1;
    //delete bN1;
    //delete bB1;
    //delete bQ;
    //delete bK;
    //delete bB2;
    //delete bN2;
    //delete bR2;

    ////deletes all the black pawns
    //delete bP1;
    //delete bP2;
    //delete bP3;
    //delete bP4;
    //delete bP5;
    //delete bP6;
    //delete bP7;
    //delete bP8;

    SDL_Quit();
}

void Game::initActivePieces()
{
    //Adds the white pieces to the active pieces list
    for (int i = 0; i < 2; i++)
    {
        for (int k = 0; k < 8; k++)
        {
            activePieces.push_back(board[i][k]);
        }
    }

    //Adds the black pieces to the active pieces list
    for (int i = 6; i < 8; i++)
    {
        for (int k = 0; k < 8; k++)
        {
            activePieces.push_back(board[i][k]);
        }
    }
}

void Game::init()
{
    initActivePieces();

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

            SDL_RenderFillRect(renderer, &tile);
        }
    }
}

void Game::displayPieces()
{
    for (int row = 0; row < ROWS; row++)
    {
        for (int col = 0; col < COLS; col++)
        {
            if (board[row][col])
            {
                //creates texture from the piece's image
                SDL_Texture* texture = SDL_CreateTextureFromSurface(renderer, board[row][col]->getImage());

                //how big the texture can be in terms of an SDL rectangle
                SDL_Rect src = { 0, 0, 80, 80 };

                //Tile on which the image is loaded and fitted on
                SDL_Rect tile = { (col * TILE_SIZE + (TILE_SIZE * (0.25 * 0.5))), (row * (TILE_SIZE) + (TILE_SIZE * (0.25 * 0.5))), TILE_SIZE * 0.75, TILE_SIZE * 0.75 };

                if (mouse.piece != board[row][col])
                {
                    SDL_RenderCopy(renderer, texture, &src, &tile);
                }
            }
        }
    }
}

void Game::displayDraggedPiece()
{
	//creates texture from the piece's image
	SDL_Texture* texture = SDL_CreateTextureFromSurface(renderer, mouse.piece->getImage());

	//how big the texture can be in terms of an SDL rectangle
	SDL_Rect src = { 0, 0, 80, 80 };

	//Tile on which the image is loaded and fitted on
	SDL_Rect tile = { (mouse.mouseCoordinates.x) - (TILE_SIZE * (0.25 * 0.5)), (mouse.mouseCoordinates.y) - (TILE_SIZE * (0.25 * 0.5)), TILE_SIZE * 0.75, TILE_SIZE * 0.75 };
	//SDL_Rect tile = { (mouse.clickedCoordinates.y), (mouse.clickedCoordinates.y), TILE_SIZE * 0.75, TILE_SIZE * 0.75 };
	//SDL_Rect tile = { (mouse.clickedCoordinates.y * TILE_SIZE), (mouse.clickedCoordinates.y * (TILE_SIZE)), TILE_SIZE * 0.75, TILE_SIZE * 0.75 };

	SDL_RenderCopy(renderer, texture, &src, &tile);
}

void Game::calculateAllMoves()
{
    for (Piece* piece : activePieces)
    {
        piece->legalMoves.clear();
        piece->calculateLegalMoves(board);
    }
}

void Game::mainloop()
{
	Game::init();

    int turn = 1;

    while (gameIsRunning)
    {
        SDL_RenderClear(renderer);

        displayBoard();
        displayPieces();

        SDL_RenderPresent(renderer);

        calculateAllMoves();

        while (SDL_WaitEvent(&event))
        {
            calculateAllMoves();

            if (event.type == SDL_QUIT)
            {
                gameIsRunning = false;
                break;
            }
            else if (event.type == SDL_MOUSEBUTTONDOWN)
            {
                SDL_GetMouseState(&mouse.mouseCoordinates.x, &mouse.mouseCoordinates.y);                

                mouse.clickedCol = int((mouse.mouseCoordinates.x) / TILE_SIZE);
                mouse.clickedRow = int((mouse.mouseCoordinates.y) / TILE_SIZE);

                if (validRowAndCol(mouse.clickedCol, mouse.clickedRow))
                {
                    if (board[mouse.clickedRow][mouse.clickedCol])
                    {
                        mouse.dragPiece(board[mouse.clickedRow][mouse.clickedCol]);
                        mouse.savePiecePos(mouse.clickedCol, mouse.clickedRow);
                    }
                }
            }
            else if (event.type == SDL_MOUSEMOTION)
            {
                if (mouse.draggingPiece)
                {
                    SDL_GetMouseState(&mouse.mouseCoordinates.x, &mouse.mouseCoordinates.y);

                    displayBoard();
                    displayPieces();

                    displayDraggedPiece();

                    SDL_RenderPresent(renderer);
                }
            }
            else if (event.type == SDL_MOUSEBUTTONUP)
            {
                SDL_GetMouseState(&mouse.mouseCoordinates.x, &mouse.mouseCoordinates.y);

                mouse.dropPiece(turn, board, activePieces);

                displayBoard();
                displayPieces();

                SDL_RenderPresent(renderer);
            }
        }
        
        SDL_UpdateWindowSurface(window);
    }
}