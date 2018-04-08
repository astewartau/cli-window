"""Command-line Interface Window

This module contains a class Window which can be used to represent a window in
standard output.

"""

from ansi_colors import ansi_colors as ac

class Window:
    """Represents a Virtual Window that can be printed to standard output.
    Primarily a data class that maintains invariants.

    Printing windows with colored borders requires a terminal supporting ANSII
    coloring (using the colors defined in the console_utilities module).

    """

    def __init__(
            self,
            width,
            height,
            title="",
            border_on=None,
            border_fg='black',
            border_bg='white'
    ):
        """Initialize a Window instance.
        
        Args:
            width: the width of the window in columns (width > 0)
            height: the height of the window in rows (height > 0)
            title: the title of the window as a string
            border_on: enables or disables a colored border
            border_fg: the text color on the border (see console_utilities)
            border_bg: the color of the border (see console_utilities)

        """

        # initialise private variables to prevent exceptions raised in the width
        # and height setters
        self._width = 1
        self._height = 1

        # represents the window's contents
        self._chars = [[' ' for x in range(self.width)]
                            for y in range(self.height)]
        self._bgs = [['black' for x in range(self.width)]
                              for y in range(self.height)]
        self._fgs = [['white' for x in range(self.width)]
                              for y in range(self.height)]

        # setting properties
        self.width = width
        self.height = height
        self.title = title
        self.border_fg = border_fg
        self.border_bg = border_bg

        if border_on is None:
            if self.title != "":
                self.border_on = True
            else:
                self.border_on = False
        else:
            self.border_on = border_on

    @property
    def border_on(self):
        """Get or set the border's state (True or False for enabled or 
        disabled)."""
        return self._border_on

    @border_on.setter
    def border_on(self, value):
        self._border_on = bool(value)    

    @property
    def border_fg(self):
        """Get or set the border foreground color. Choosing an invalid color
        as defined in console_utilities will raise a ValueError.
        """
        return self._border_fg

    @border_fg.setter
    def border_fg(self, value):
        if value not in ac.color_string.ansi_foreground:
            raise ValueError("Invalid foreground color: {}".format(value))
        self._border_fg = value

    @property
    def border_bg(self):
        """Get or set the border color (background). Choosing an invalid color
        as defined in console_utilities will raise a ValueError.
        """
        return self._border_bg

    @border_bg.setter
    def border_bg(self, value):
        if value not in ac.color_string.ansi_background:
            raise ValueError("Invalid background color: {}".format(value))
        self._border_bg = value
    
    @property
    def title(self):
        """Get or set the window title."""
        return self._title

    @title.setter
    def title(self, value):
        self._title = str(value)

    @property
    def width(self):
        """Get or set the window width > 0. Setting clears all cells.
        """
        return self._width

    @width.setter
    def width(self, value):
        try:
            value = int(value)
        except Exception:
            raise ValueError(
                "Window width must be a positive integer! "
                "Encountered {}"
                .format(type(value))
            )
        
        if value <= 0:
            raise ValueError(
                "Window dimensions must be positive! "
                "Encountered {}".format(value)
            )
        
        self._width = value
        if len(self._chars[0]) != self._width:
            self._chars = [[' ' for x in range(self.width)]
                                for y in range(self.height)]
            self._bgs = [['black' for x in range(self.width)]
                                  for y in range(self.height)]
            self._fgs = [['white' for x in range(self.width)]
                                  for y in range(self.height)]

    @property
    def height(self):
        """Get or set the window height > 0. Setting clears all cells.
        """
        return self._height

    @height.setter
    def height(self, value):
        if value == self._height:
            return
        
        try:
            value = int(value)
        except Exception:
            raise ValueError(
                "Window height must be a positive integer! "
                "Encountered {}"
                .format(type(value))
            )
        
        if value <= 0:
            raise ValueError(
                "Window dimensions must be positive! "
                "Encountered {}".format(value)
            )

        self._height = value
        
        if len(self._chars) != self._height:
            self._chars = [[' ' for x in range(self.width)]
                                for y in range(self.height)]
            self._bgs = [['black' for x in range(self.width)]
                                  for y in range(self.height)]
            self._fgs = [['white' for x in range(self.width)]
                                  for y in range(self.height)]

    def set_cell_char(self, x, y, char):
        """Set the given cell to store the given character.
        
        Args:
            x: integer representing the column of the cell to set.
            y: integer representing the row of the cell to set.
            char: string with len(char) == 1 representing the character to store
                  (if any).
        """
        if len(str(char)) != 1:
            raise ValueError(
                "Character must be a single character! Got {}".format(char)
            )

        self._chars[y][x] = str(char)

    def set_cell_bg(self, x, y, bg):
        """Set the given cell to use the given background color.

        Args:
            x: integer representing the column of the cell to set.
            y: integer representing the row of the cell to set.
            bg: string representing the new background color of the cell.
        """
        if bg not in ac.color_string.ansi_background:
            raise ValueError("Invalid background color: {}".format(bg))
        
        self._bgs[y][x] = bg

    def set_cell_fg(self, x, y, fg):
        """Set the given cell to use the given foreground color.

        Args:
            x: integer representing the column of the cell to set.
            y: integer representing the row of the cell to set.
            bg: string representing the new foreground color of the cell.
        """
        if fg not in ac.color_string.ansi_foreground:
            raise ValueError("Invalid foreground color: {}".format(fg))
        
        self._fgs[y][x] = fg

    def set_cell(self, x, y, char=None, fg=None, bg=None):
        """Set the given cell position with any of a character, foreground color
           or background color.

        Args:
            x: integer representing the column of the cell to set.
            y: integer representing the row of the cell to set.
            char: string with len(char) == 1 representing the character to store
                  (if any).
            fg: string representing the new foreground color of the cell, if any
                (see console_utilities).
            bg: string representing the new background color of the cell, if any
                (see console_utilities).

        """
        
        if char:
            self.set_cell_char(x, y, char)
        if fg:
            self.set_cell_fg(x, y, fg)
        if bg:
            self.set_cell_bg(x, y, bg)

    def __repr__(self):
        """Return a printable string to represent the window."""
        output = ""

        # Top border (top row)
        if self.border_on:
            title = self._title
            if len(title) > self._width:
                title = title[0:self._width-2]
                
            output += ac.color_string(
                title.center(self._width + 2),
                self.border_fg,
                self.border_bg
            ) + '\n'

        # Cells (middle rows)
        for row in range(self.height):
            if self.border_on:
                output += ac.color_string(' ', self.border_fg, self.border_bg)

            for char, fg, bg in zip(self._chars[row], self._fgs[row], self._bgs[row]):
                output += ac.color_string(char, fg, bg)
                
            if self.border_on:
                output += ac.color_string(' ', self.border_fg, self.border_bg)
                
            output += '\n'

        # Bottom border (bottom row)
        if self.border_on:
            output += ac.color_string(' ' * (self._width + 2), 'white', self.border_bg)

        return output

    def clear(self):
        """Clear all cells."""
        self._chars = [[' ' for x in range(self.width)]
                            for y in range(self.height)]
        self._bgs = [['black' for x in range(self.width)]
                              for y in range(self.height)]
        self._fgs = [['white' for x in range(self.width)]
                              for y in range(self.height)]
