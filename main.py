import checkers

def game():
    request_again_flag = True
    while request_again_flag:

        size = int(input('Please designate a square board size between minimum of 4 and maximum of 16: '))
        if 4 <= size <= 16:
            print('\nHere is your game board:')
            request_again_flag = False
        else:
            print('That entry is not valid, please try again.')

    board1 = checkers.build_board(size)
    print(board1)

    empty_count = checkers.get_count(board1, 'Empty')
    print(empty_count)
    red_count = checkers.get_count(board1, 'Red')
    print(red_count)
    black_count = checkers.get_count(board1, 'Black')
    print(black_count)


if __name__ == '__main__':
    game()