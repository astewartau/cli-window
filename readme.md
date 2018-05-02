# Command-line Interface Window for Python

This module allows you to construct and print content within a command-line
interface that resembles a desktop _Window_ or panel. Windows may optionally
include a frame and a title. Frame colors can also be specified, made possible
by the ansi_colors submodule.

## Setup

After cloning the repository, ensure you run the following commands to
initialise the require submodule:

    git submodule init
	git submodule update

## Usage Examples

**Creating a 5x20 window with a title and default frame:**

```
w = Window(
    width=20,
	height=5,
	title='My Window'
)

print(w)
```

**Creating a 10x20 window with a title and custom border colors:**

```
w = Window(
    width=20,
	height=10,
	title='My Window',
	border_bg='yellow',
	border_fg='black'
)

print(w)
```

### Screenshot Examples

![Example 1](https://raw.githubusercontent.com/astewartau/cli-window/master/images/basic1.png)

![Example 2](https://raw.githubusercontent.com/astewartau/cli-window/master/images/basic2.png)

![Example 3](https://raw.githubusercontent.com/astewartau/cli-window/master/images/basic3.png)
