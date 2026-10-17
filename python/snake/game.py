from models.board import Board

def run():
    board = Board(3, 2)
    render = board.cli_render()
    print(render)

if __name__ == "__main__":
    run()
