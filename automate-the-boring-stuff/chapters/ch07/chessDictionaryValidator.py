def isValidChessBoard(board):
    # Track counts for validation
    piece_counts = {}
    white_piece_count = 0
    black_piece_count = 0
    white_pawn_count = 0
    black_pawn_count = 0
    
    # Valid spaces coordinates (files '1'-'8', ranks 'a'-'h')
    valid_spaces = []
    for num in '12345678':
        for letter in 'abcdefgh':
            valid_spaces.append(num + letter)
            
    valid_pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    for position, piece in board.items():
        # 1. Check if square name is valid (e.g. not '9z')
        if position not in valid_spaces:
            return False
            
        # 2. Check piece color and name formatting
        if piece[0] == 'w':
            color = 'w'
            white_piece_count += 1
        elif piece[0] == 'b':
            color = 'b'
            black_piece_count += 1
        else:
            return False # Invalid color prefix
            
        piece_type = piece[1:]
        if piece_type not in valid_pieces:
            return False # Invalid piece type name
            
        # Count specific pieces
        piece_counts[piece] = piece_counts.get(piece, 0) + 1
        
        if piece == 'wpawn':
            white_pawn_count += 1
        elif piece == 'bpawn':
            black_pawn_count += 1

    # 3. Check total piece limits per player (max 16)
    if white_piece_count > 16 or black_piece_count > 16:
        return False
        
    # 4. Check pawn limits (max 8 per player)
    if white_pawn_count > 8 or black_pawn_count > 8:
        return False
        
    # 5. Check king counts (exactly 1 white king, 1 black king)
    if piece_counts.get('wking', 0) != 1 or piece_counts.get('bking', 0) != 1:
        return False

    return True