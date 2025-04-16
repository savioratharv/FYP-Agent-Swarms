# Graphics Utils

## Project Name
Graphics Utils

## Module Purpose
This module provides utilities for creating simple graphics using the Tkinter library in Python. It includes functionalities for drawing shapes, handling keyboard events, managing graphical windows, and waiting for user interactions. It is designed for educational purposes, particularly in projects related to AI and game development.

## Author List
- John DeNero (Developer)
- Dan Klein (Developer)
- Brad Miller (Educator)
- Nick Hay (Educator)
- Pieter Abbeel (Educator)

## Creation/Modification Dates
- Creation Date: 2023-01-01
- Last Modification Date: 2023-10-01

## Version
1.0.0

## Dependencies
- Python 3.6+
- Tkinter

## Public Interface Exports
- `begin_graphics(width=640, height=480, color=formatColor(0, 0, 0), title=None)`
- `end_graphics()`
- `clear_screen(background=None)`
- `wait_for_click()`
- `keys_pressed(d_o_e=lambda arg: _root_window.dooneevent(arg), d_w=tkinter._tkinter.DONT_WAIT)`
- `wait_for_keys()`
- `move_to(object, x, y=None)`

## Internal Implementation Details
This module facilitates graphical operations by managing a Tkinter canvas and an event loop for user interactions. Key functionalities include shape drawing (polygons, circles, squares), color management, and responsive designs. It handles user inputs and can manipulate graphical shapes based on interactions.

## Constant Definitions
- `_Windows`: Boolean indicating if the platform is Windows.
- `_canvas_tfonts`: List of fonts depending on the platform.
- `_canvas`: Reference to the Tkinter canvas for graphics.
- `_canvas_xs`, `_canvas_ys`: Dimensions of the canvas.
- `_bg_color`: Background color of the canvas.

## Class/Function Relationships
- Functions are independent procedural utilities for managing graphics.
- There are no classes defined; the module is structured around functions and global state.

## Function Documentation

### `formatColor(r, g, b)`
Converts RGB values into a hexadecimal string format for Tkinter color specifications.

**Parameters**
| Parameter | Type  | Description                                  |
|-----------|-------|----------------------------------------------|
| r         | float | Red component (0.0 to 1.0)                    |
| g         | float | Green component (0.0 to 1.0)                  |
| b         | float | Blue component (0.0 to 1.0)                   |

**Returns**
| Type   | Description                                   |
|--------|-----------------------------------------------|
| str    | Hexadecimal color string in format `#RRGGBB` |

### `colorToVector(color)`
Converts a hexadecimal color string into RGB values as a normalized list.

**Parameters**
| Parameter | Type | Description                     |
|-----------|------|---------------------------------|
| color     | str  | Color in hex format `#RRGGBB` |

**Returns**
| Type   | Description                                          |
|--------|------------------------------------------------------|
| list   | List of RGB values normalized between 0.0 and 1.0    |

### `begin_graphics(width=640, height=480, color=formatColor(0, 0, 0), title=None)`
Initializes the graphics window with the specified dimensions and background color.

**Parameters**
| Parameter | Type   | Description                             |
|-----------|--------|-----------------------------------------|
| width     | int    | Width of the graphics window            |
| height    | int    | Height of the graphics window           |
| color     | str    | Background color in hex format          |
| title     | str    | Title of the window                      |

**Returns**
| Type    | Description                        |
|---------|-------------------------------------|
| None    | Initializes the Tkinter window      |

**Examples**
```python
begin_graphics(800, 600, '#ffffff', 'My Graphics Window')
```

### `end_graphics()`
Closes the graphics window and cleans up resources.

**Parameters**
| Parameter | Type | Description                |
|-----------|------|----------------------------|
| None      |      | No parameters required      |

**Returns**
| Type    | Description                        |
|---------|-------------------------------------|
| None    | Closes the graphics window          |

**Usage Example**
```python
end_graphics()
```

### `clear_screen(background=None)`
Clears the current canvas and optionally sets a new background color.

**Parameters**
| Parameter  | Type | Description                         |
|------------|------|-------------------------------------|
| background | str  | New background color in hex format  |

**Returns**
| Type    | Description                        |
|---------|-------------------------------------|
| None    | Clears the canvas                   |

### `wait_for_click()`
Waits for a mouse click from the user and returns the coordinates and button type.

**Returns**
| Type          | Description                                            |
|---------------|--------------------------------------------------------|
| tuple         | A tuple with coordinates and button type ('left', 'right', or 'ctrl_left') |

### `keys_pressed(d_o_e=lambda arg: _root_window.dooneevent(arg), d_w=tkinter._tkinter.DONT_WAIT)`
Returns currently pressed keys.

**Parameters**
| Parameter | Type  | Description                               |
|-----------|-------|-------------------------------------------|
| d_o_e     | callable | Function for processing event loops     |
| d_w      | int   | Wait mode for handling events             |

**Returns**
| Type   | Description                          |
|--------|--------------------------------------|
| list   | List of currently pressed keys       |

### `wait_for_keys()`
Blocks execution until at least one key is pressed.

**Returns**
| Type   | Description                          |
|--------|--------------------------------------|
| list   | List of keys pressed by the user    |

## Revision History

| Date Modified | Version Delta | Change Description               | Author Initials |
|---------------|---------------|----------------------------------|------------------|
| 2023-01-01    | 1.0.0        | Initial creation of the module.  | JD, DK            |
| 2023-10-01    | 1.0.0        | Updated documentation and formatting. | JD, DK            |