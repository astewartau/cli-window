import unittest
from cli_window import Window

class TestWindowMethods(unittest.TestCase):
    def test_normal_init(self):
        w = Window(
            width     = 30,
            height    = 10,
            title     = 'Game',
            border_on = False,
            border_fg = 'black',
            border_bg = 'yellow'
        )
        
        self.assertEqual(w.width, 30)
        self.assertEqual(w.height, 10)
        self.assertEqual(w.title, 'Game')
        self.assertEqual(w.border_on, False)
        self.assertEqual(w.border_fg, 'black')
        self.assertEqual(w.border_bg, 'yellow')

    def test_bad_window_init(self):
        self.assertRaises(ValueError, Window, width=0, height=0)
        self.assertRaises(ValueError, Window, width=-1, height=1)
        self.assertRaises(ValueError, Window, width=1, height=-1)

    def test_bad_border_color_init(self):
        self.assertRaises(ValueError, Window, width=1, height=1, border_fg='foo')
        self.assertRaises(ValueError, Window, width=1, height=1, border_bg='foo')

    def test_bad_border_color_after_init(self):
        w = Window(1, 1)
        with self.assertRaises(ValueError) as context:
            w.border_fg = 'foo'
        with self.assertRaises(ValueError) as context:
            w.border_bg = 'foo'

    def test_bad_width_after_init(self):
        w = Window(1, 1)
        with self.assertRaises(ValueError) as context:
            w.width = -5
        with self.assertRaises(ValueError) as context:
            w.width = 0
        with self.assertRaises(ValueError) as context:
            w.width = 'foo'

    def test_bad_height_after_init(self):
        w = Window(1, 1)
        with self.assertRaises(ValueError) as context:
            w.height = -5
        with self.assertRaises(ValueError) as context:
            w.height = 0
        with self.assertRaises(ValueError) as context:
            w.height = 'foo'

    def test_1x1_window_output(self):
        w = Window(1, 1)
        self.assertEqual(w.__repr__(), ' \n')

    def test_3x5_window_output(self):
        w = Window(3, 5)
        self.assertEqual(w.__repr__(), (' ' * 3 + '\n') * 5)

    def test_set_cell_char_normal(self):
        w = Window(3, 3)
        w.set_cell_char(x=1, y=0, char='@')
        self.assertEqual(w.__repr__(), ' @ \n   \n   \n')

    def test_set_cell_char_bad(self):
        w = Window(3, 3)
        with self.assertRaises(ValueError) as context:
            w.set_cell_char(x=1, y=0, char='multiple characters')

    def test_set_cell_color_normal(self):
        w = Window(3, 3)
        w.set_cell_char(x=0, y=0, char='@')
        w.set_cell_fg(x=0, y=0, fg='brightyellow')
        w.set_cell_bg(x=1, y=0, bg='red')
        self.assertEqual(
            w.__repr__(),
            '\x1b[93;40m@\x1b[0m\x1b[37;41m \x1b[0m \n   \n   \n'
        )

    def test_set_cell_color_bad(self):
        w = Window(3, 3)
        with self.assertRaises(ValueError) as context:
            w.set_cell_fg(0, 0, 'foo')
        with self.assertRaises(ValueError) as context:
            w.set_cell_bg(0, 0, 'foo')

    def test_set_cell_normal(self):
        w = Window(3, 3)
        w.set_cell(x=0, y=0, char='@')
        w.set_cell(x=0, y=0, bg='red')
        w.set_cell(x=0, y=0, fg='brightyellow')
        self.assertEqual(w.__repr__(), '\x1b[93;41m@\x1b[0m  \n   \n   \n')

    def test_set_cell_bad(self):
        w = Window(3, 3)
        with self.assertRaises(ValueError) as context:
            w.set_cell(0, 0, char='multiple chars')
        with self.assertRaises(ValueError) as context:
            w.set_cell(0, 0, bg='foo')
        with self.assertRaises(ValueError) as context:
            w.set_cell(0, 0, fg='foo')

    def test_clear(self):
        w = Window(2, 2)
        w.set_cell_char(x=1, y=0, char='a')
        w.clear()
        self.assertEqual(w.__repr__(), '  \n  \n')

if __name__ == "__main__":
    unittest.main()
