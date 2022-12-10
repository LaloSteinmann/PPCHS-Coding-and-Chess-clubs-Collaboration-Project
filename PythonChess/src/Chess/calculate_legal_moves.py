from pieces import *
from tile import *
from constants import *
import pygame as pg
import sys as system
from button import *

def calculate_legal_moves_loop(piece_list, tiles):
    for piece in piece_list:
        piece.tile_num_of_moves.clear()
        piece.moves.clear()
        calculate_legal_moves(tiles, piece, piece.row, piece.col)
    
# def pawn_promotion(mouse, tiles, pawn, screen, piece_list):
#     while True:
#         mouse.update_mouse(pg.mouse.get_pos())
#         for row in range(pawn.row, pawn.row - 3):
#             color = 'aliceblue'
#             rect = (pawn.col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
#             pg.draw.rect(screen, color, rect)
#             if row == pawn.row:
#                 img = pg.image.load(os.path.join(f'PieceImages/{pawn.color}_queen80x80.png'))
#                 img_centering = pawn.col * TILE_SIZE + (TILE_SIZE / 2), row * TILE_SIZE + (TILE_SIZE / 2)
#                 img_rect = img.get_rect(center=img_centering)
#                 screen.blit(img, img_rect)
#             elif row == pawn.row - 1:
#                 img = pg.image.load(os.path.join(f'PieceImages/{pawn.color}_rook80x80.png'))
#                 img_centering = pawn.col * TILE_SIZE + (TILE_SIZE / 2), row * TILE_SIZE + (TILE_SIZE / 2)
#                 img_rect = img.get_rect(center=img_centering)
#                 screen.blit(img, img_rect)
#             elif row == pawn.row - 2:
#                 img = pg.image.load(os.path.join(f'PieceImages/{pawn.color}_bishop80x80.png'))
#                 img_centering = pawn.col * TILE_SIZE + (TILE_SIZE / 2), row * TILE_SIZE + (TILE_SIZE / 2)
#                 img_rect = img.get_rect(center=img_centering)
#                 screen.blit(img, img_rect)
#             elif row == pawn.row - 3:
#                 img = pg.image.load(os.path.join(f'PieceImages/{pawn.color}_knight80x80.png'))
#                 img_centering = pawn.col * TILE_SIZE + (TILE_SIZE / 2), row * TILE_SIZE + (TILE_SIZE / 2)
#                 img_rect = img.get_rect(center=img_centering)
#                 screen.blit(img, img_rect)

#         current_col = int(mouse.mouseX / TILE_SIZE)
#         current_row = int(mouse.mouseY / TILE_SIZE)

#         if current_row == pawn.row and current_col == pawn.col:
#             piece_list.remove(pawn)
#             tiles[pawn.row][pawn.col].piece_on_tile = Queen(pawn.color, pawn.row, pawn.col)
#             new_piece = tiles[pawn.row][pawn.col].piece_on_tile
#             piece_list.append(pawn)
#             return
#         elif current_row - 1 == pawn.row and current_col == pawn.col:
#             piece_list.remove(pawn)
#             tiles[pawn.row][pawn.col].piece_on_tile = Rook(pawn.color, pawn.row, pawn.col)
#             new_piece = tiles[pawn.row][pawn.col].piece_on_tile
#             piece_list.append(new_piece)
#             return
#         elif current_row - 2 == pawn.row and current_col == pawn.col:
#             piece_list.remove(pawn)
#             tiles[pawn.row][pawn.col].piece_on_tile = Bishop(pawn.color, pawn.row, pawn.col)
#             new_piece = tiles[pawn.row][pawn.col].piece_on_tile
#             piece_list.append(pawn)
#             return
#         elif current_row - 3 == pawn.row and current_col == pawn.col:
#             piece_list.remove(pawn)
#             tiles[pawn.row][pawn.col].piece_on_tile = Knight(pawn.color, pawn.row, pawn.col)
#             new_piece = tiles[pawn.row][pawn.col].piece_on_tile
#             piece_list.append(pawn)
#             return

#         pg.display.update()

def return_tile_num(tile: Tile):
    tile_row = tile.row * 8
    tile_num = tile_row + tile.col
    return tile_num

def return_row_and_col(tile_num: int):
    running_total = 0
    for row in range(ROWS):
        for col in range(COLUMNS):
            if running_total == tile_num:
                tile = (row, col)
                return tile
            running_total += 1

# method to calculate the legal moves for a knight
def calculate_knight_moves(tiles, knight: Knight, row, col):
    #The way the knight moves applied to our current position
    move_scheme = [ (row + knight.dir, col + 2),
                    (row - knight.dir, col + 2),
                    (row - knight.dir, col - 2),
                    (row + knight.dir, col - 2),
                    (row + (knight.dir * 2), col + 1),
                    (row - (knight.dir * 2), col + 1),
                    (row - (knight.dir * 2), col - 1),
                    (row + (knight.dir * 2), col - 1)
                  ]
    #loops through the list of movements
    for possible_move in move_scheme:
        #creates our new possible position
        #possible_row, possible_col = possible_move
        possible_row = possible_move[0]
        possible_col = possible_move[1]

        #creates our new possible tile that we will land on
        if is_valid_coordinate(possible_row, possible_col):
            possible_destination: Tile = get_tile(tiles, possible_row, possible_col)

            #our current position
            #current_pos = Tile(row, col)
            #the piece on our candidate tile
            #piece_on_final_pos = tiles[possible_row][possible_col].piece
            #our final tile if the move is valid
            final_pos = tiles[possible_row][possible_col]
            tile_num = return_tile_num(final_pos)
            #the move that would be made
            move = final_pos

            #checks if the new tile is actually a possible tile on a board
            
            #checks for the first possibility; if the tile is empty
            if not possible_destination.is_tile_occupied():
                knight.add_move(move, tile_num)
            #checks for the second possibility; if the tile is occupied, but the piece on it is an enemy piece
            else:
                if possible_destination.piece_on_tile.color != knight.color:
                    knight.add_move(move, tile_num)

def calculate_bishop_moves(tiles, bishop: Bishop, row, col):
        move_scheme = [ (1, -1),
                        (-1, 1),
                        (1, 1),
                        (-1, -1)
                      ]
        
        for possible_move in move_scheme:
             #creates our new possible position
            possible_row = row
            possible_col = col

            while is_valid_coordinate(possible_row, possible_col):
                possible_row += (bishop.dir * possible_move[0])
                possible_col += possible_move[1]
                
                if is_valid_coordinate(possible_row, possible_col):
                    #our current position
                    #current_pos = Tile(row, col)
                    #the piece on our candidate tile
                    #piece_on_final_pos = tiles[possible_row][possible_col].piece
                    #our final tile if the move is valid
                    final_pos = tiles[possible_row][possible_col]
                    tile_num = return_tile_num(final_pos)
                    #the move that would be made
                    move = final_pos
                    #creates our new possible tile that we will land on
                    possible_destination: Tile = get_tile(tiles, possible_row, possible_col)
                    if not possible_destination.is_tile_occupied():
                        bishop.add_move(move, tile_num)
                    else:
                        if possible_destination.has_enemy_piece(bishop.color):
                            bishop.add_move(move, tile_num)
                        break

def calculate_rook_moves(tiles, rook: Rook, row, col):
        move_scheme = [ (1, 0),
                        (-1, 0),
                        (0, 1),
                        (0, -1)
                      ]
        
        for possible_move in move_scheme:
             #creates our new possible position
            possible_row = row
            possible_col = col

            while is_valid_coordinate(possible_row, possible_col):
                possible_row += (rook.dir * possible_move[0])
                possible_col += possible_move[1]
                
                if is_valid_coordinate(possible_row, possible_col):
                    #our current position
                    #current_pos = Tile(row, col)
                    #the piece on our candidate tile
                    #piece_on_final_pos = tiles[possible_row][possible_col].piece
                    #our final tile if the move is valid
                    final_pos = tiles[possible_row][possible_col]
                    tile_num = return_tile_num(final_pos)
                    #the move that would be made
                    move = final_pos
                    #creates our new possible tile that we will land on
                    possible_destination: Tile = get_tile(tiles, possible_row, possible_col)
                    if not possible_destination.is_tile_occupied():
                        rook.add_move(move, tile_num)
                    else:
                        if possible_destination.has_enemy_piece(rook.color):
                            rook.add_move(move, tile_num)
                        break

def calculate_queen_moves(tiles, queen: Queen, row, col):
        move_scheme = [ (1, 0),
                        (-1, 0),
                        (0, 1),
                        (0, -1),
                        (-1, 1),
                        (-1, -1),
                        (1, 1),
                        (1, -1)
                      ]
        
        for possible_move in move_scheme:
             #creates our new possible position
            possible_row = row
            possible_col = col

            while is_valid_coordinate(possible_row, possible_col):
                possible_row += (queen.dir * possible_move[0])
                possible_col += possible_move[1]
                
                if is_valid_coordinate(possible_row, possible_col):
                    #our current position
                    #current_pos = Tile(row, col)
                    #the piece on our candidate tile
                    #piece_on_final_pos = tiles[possible_row][possible_col].piece
                    #our final tile if the move is valid
                    final_pos = tiles[possible_row][possible_col]
                    #the move that would be made
                    move = final_pos
                    tile_num = return_tile_num(final_pos)
                    #creates our new possible tile that we will land on
                    possible_destination: Tile = get_tile(tiles, possible_row, possible_col)
                    
                    if not possible_destination.is_tile_occupied():
                        # king = get_king(tiles, queen.color)
                        # if (not is_king_in_check(tiles, king)) or (is_king_in_check(tiles, king)
                        # and would_remove_check(tiles, queen.color, queen, possible_row, possible_col)):
                            queen.add_move(move, tile_num)
                    else:
                        if possible_destination.has_enemy_piece(queen.color):
                            # king = get_king(tiles, queen.color)
                            # if (not is_king_in_check(tiles, king)) or (is_king_in_check(tiles, king)
                            # and would_remove_check(tiles, queen.color, queen, possible_row, possible_col)):
                                queen.add_move(move, tile_num)
                        break

def calculate_pawn_moves(tiles, pawn: Pawn, row, col):

    possible_row = row + pawn.dir
    possible_col_right = col + 1
    possible_col_left = col - 1

    if (pawn.color == 'white' and row == 3) or (pawn.color != 'white' and row == 4):

        if is_valid_coordinate(row, possible_col_right):
            if tiles[row][possible_col_right].is_tile_occupied() and (isinstance(tiles[row][possible_col_right].get_piece(), Pawn) 
            and tiles[row][possible_col_right].has_enemy_piece(pawn.color)) and (tiles[row][possible_col_right].get_piece().jumped_two_tiles):
                #current_pos = Tile(row, col)
                final_pos = Tile(row + pawn.dir, possible_col_right)
                move = final_pos
                tile_num = return_tile_num(final_pos)
                pawn.add_move(move, tile_num)
                pawn.en_passant = True
            
        if is_valid_coordinate(row, possible_col_left):
            if tiles[row][possible_col_left].is_tile_occupied() and (isinstance(tiles[row][possible_col_left].get_piece(), Pawn) 
            and tiles[row][possible_col_left].has_enemy_piece(pawn.color)) and (tiles[row][possible_col_left].get_piece().jumped_two_tiles):
                #current_pos = Tile(row, col)
                final_pos = tiles[(row + pawn.dir)][possible_col_left]
                tile_num = return_tile_num(final_pos)
                move = final_pos
                pawn.add_move(move, tile_num)
                pawn.en_passant = True

    elif (not pawn.moved) and (not tiles[row + pawn.dir][col].is_tile_occupied()) and (not tiles[row + (2 * pawn.dir)][col].is_tile_occupied()):
        #current_pos = Tile(row, col)
        final_pos = Tile(row + (2 * pawn.dir), col)
        tile_num = return_tile_num(final_pos)
        move = final_pos
        pawn.add_move(move, tile_num)

    if is_valid_coordinate(possible_row, possible_col_right):
        if tiles[possible_row][possible_col_right].is_tile_occupied() and tiles[possible_row][possible_col_right].has_enemy_piece(pawn.color):
            #current_pos = Tile(row, col)
            final_pos = tiles[possible_row][possible_col_right]
            tile_num = return_tile_num(final_pos)
            move = final_pos
            pawn.add_move(move, tile_num)

    if is_valid_coordinate(possible_row, possible_col_left):
        if tiles[possible_row][possible_col_left].is_tile_occupied() and tiles[possible_row][possible_col_left].has_enemy_piece(pawn.color):
            #current_pos = Tile(row, col)
            final_pos = tiles[possible_row][possible_col_left]
            tile_num = return_tile_num(final_pos)
            move = final_pos
            pawn.add_move(move, tile_num)

    if is_valid_coordinate(possible_row, col):
        if not tiles[possible_row][col].is_tile_occupied():
            #current_pos = Tile(row, col)
            final_pos = tiles[possible_row][col]
            tile_num = return_tile_num(final_pos)
            move = final_pos
            pawn.add_move(final_pos, tile_num)

def pawn_promotion(screen, pawn, tiles, piece_list):

    while True:

        menu_pos = pg.mouse.get_pos()

        queen_button = Promotion_Button((pawn.col * TILE_SIZE + (TILE_SIZE / 2), 
        (pawn.row - (pawn.dir * 1)) * TILE_SIZE + (TILE_SIZE / 2)), pawn.color, 'queen',
        ((pawn.col * TILE_SIZE), (pawn.row - (pawn.dir * 1)) * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        rook_button = Promotion_Button((pawn.col * TILE_SIZE + (TILE_SIZE / 2), 
        (pawn.row - (pawn.dir * 2)) * TILE_SIZE + (TILE_SIZE / 2)), pawn.color, 'rook',
        ((pawn.col * TILE_SIZE), (pawn.row - (pawn.dir * 2)) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        
        bishop_button = Promotion_Button((pawn.col * TILE_SIZE + (TILE_SIZE / 2), 
        (pawn.row - (pawn.dir * 3)) * TILE_SIZE + (TILE_SIZE / 2)), pawn.color, 'bishop',
        ((pawn.col * TILE_SIZE), (pawn.row - (pawn.dir * 3)) * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        knight_button = Promotion_Button((pawn.col * TILE_SIZE + (TILE_SIZE / 2), 
        (pawn.row - (pawn.dir * 4)) * TILE_SIZE + (TILE_SIZE / 2)), pawn.color, 'knight',
        ((pawn.col * TILE_SIZE), (pawn.row - (pawn.dir * 4)) * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        
        # screen.blit(menu_text, menu_rect)

        for piece in [queen_button, rook_button, bishop_button, knight_button]:
            piece.update(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                system.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if queen_button.check_input(menu_pos):
                    #promote to queen
                    piece_list.remove(pawn)
                    tiles[pawn.row][pawn.col].piece_on_tile = Queen(pawn.color, pawn.row, pawn.col)
                    piece_list.append(tiles[pawn.row][pawn.col].piece_on_tile)
                    return

                elif rook_button.check_input(menu_pos):
                    #promote to rook
                    piece_list.remove(pawn)
                    tiles[pawn.row][pawn.col].piece_on_tile = Rook(pawn.color, pawn.row, pawn.col)
                    piece_list.append(tiles[pawn.row][pawn.col].piece_on_tile)
                    return

                elif bishop_button.check_input(menu_pos):
                    #promote to bishop
                    piece_list.remove(pawn)
                    tiles[pawn.row][pawn.col].piece_on_tile = Bishop(pawn.color, pawn.row, pawn.col)
                    piece_list.append(tiles[pawn.row][pawn.col].piece_on_tile)
                    return

                elif knight_button.check_input(menu_pos):
                    #promote to knight
                    piece_list.remove(pawn)
                    tiles[pawn.row][pawn.col].piece_on_tile = Knight(pawn.color, pawn.row, pawn.col)
                    piece_list.append(tiles[pawn.row][pawn.col].piece_on_tile)
                    return

        pg.display.update()

def calculate_king_moves(tiles, king: King, row, col):
    #The way the knight moves applied to our current position
    move_scheme = [ (row + king.dir, col + 1),
                    (row - king.dir, col + 1),
                    (row - king.dir, col - 1),
                    (row + king.dir, col - 1),
                    (row, col + 1),
                    (row, col - 1),
                    (row + king.dir, col),
                    (row - king.dir, col)
                  ]
    #loops through the list of movements
    for possible_move in move_scheme:
        #creates our new possible position
        possible_row, possible_col = possible_move

        #creates our new possible tile that we will land on
        if is_valid_coordinate(possible_row, possible_col):
            possible_destination: Tile = get_tile(tiles, possible_row, possible_col)

            #our current position
            # current_pos = Tile(row, col)
            #the piece on our candidate tile
            # piece_on_final_pos = tiles[possible_row][possible_col].piece
            #our final tile if the move is valid
            final_pos = tiles[possible_row][possible_col]
            tile_num = return_tile_num(final_pos)
            #(possible_row, possible_col, piece_on_final_pos)
            #the move that would be made
            move = final_pos

            #checks if the new tile is actually a possible tile on a board
            #checks for the first possibility; if the tile is empty
            if not possible_destination.is_tile_occupied():
                king.add_move(move, tile_num)
            #checks for the second possibility; if the tile is occupied, but the piece on it is an enemy piece
            else:
                if possible_destination.has_enemy_piece(king.color):
                    king.add_move(move, tile_num)

def calculate_legal_moves(tiles, piece: Piece, row, col):
    if isinstance(piece, Pawn):
        calculate_pawn_moves(tiles, piece, row, col)
    elif isinstance(piece, Knight):
        calculate_knight_moves(tiles, piece, row, col)
    elif isinstance(piece, Bishop):
        calculate_bishop_moves(tiles, piece, row, col)
    elif isinstance(piece, Rook):
        calculate_rook_moves(tiles, piece, row, col)
    elif isinstance(piece, Queen):
        calculate_queen_moves(tiles, piece, row, col)
    elif isinstance(piece, King):
        calculate_king_moves(tiles, piece, row, col)
