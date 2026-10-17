class Board:
    def __init__(self, rows: int, columns: int):
        """Constructs a Board object

        Args:
            rows (int) - rows the Board object created has
            columns (int) - columns the Board object created has

        Returns:
            Board: The board object created
        """
        self.columns = columns
        self.rows = rows
        self._board = []

        for row in range(rows):
            self._board.append([])
            for column in range(columns):
                self._board[row].append([])
    def cli_render(self)->str:
        """Create render string that shows the entirety of the Board
        Returns:
            str: The string that contains the render of the board for a command line interface environment
        """

        render = ""

        for row in range(self.rows):
            for column in range(self.columns):
                render += "[ ]"
            render += "\n"

        return render
