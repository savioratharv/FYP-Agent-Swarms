# Graphics Utils

## Module Purpose
The `graphicsUtils` module provides a simple interface for creating graphical 
windows and rendering basic geometric shapes using the Tkinter library. This 
module allows users to manage graphical elements such as polygons, circles, 
and images, as well as handle basic user interactions like mouse clicks and 
keyboard events. It is particularly useful for educational purposes and 
beginner projects that require a quick setup for graphical output.

## Author List
- John DeNero - Project Lead
- Dan Klein - Project Lead
- Brad Miller - Developer
- Nick Hay - Developer
- Pieter Abbeel - Developer

## Creation/Modification Dates
- Creation Date: 2023-03-01
- Last Modification Date: 2023-10-02

## Version
- Version: 1.0.0

## Dependency List
- Tkinter (Python standard library)

---

## Public Interface Exports
- `begin_graphics(width, height, color, title)`
- `end_graphics()`
- `clear_screen(background)`
- `polygon(coords, outlineColor, fillColor, filled, smoothed, behind, width)`
- `square(pos, r, color, filled, behind)`
- `circle(pos, r, outlineColor, fillColor, endpoints, style, width)`
- `image(pos, file)`
- `refresh()`
- `moveCircle(id, pos, r, endpoints)`
- `edit(id, *args)`
- `text(pos, color, contents, font, size, style, anchor)`
- `changeText(id, newText, font, size, style)`
- `changeColor(id, newColor)`
- `line(here, there, color, width)`
- `wait_for_click()`
- `keys_pressed(d_o_e, d_w)`
- `keys_waiting()`
- `wait_for_keys()`
- `remove_from_screen(x, d_o_e, d_w)`

## Internal Implementation Details
The module uses a global Tkinter canvas to manage graphical output. Key 
presses and mouse events are tracked using global variables. Functions are 
available for different geometric shapes, allowing for the customization of 
colors, outlines, and fill styles. Basic event handling allows for real-time 
user interactions. The canvas can be cleared and redrawn as needed.

## Constant Definitions
- `_Windows`: Determines if the operating system is Windows.
- `_canvas_tfonts`: Fonts used for text rendering, depending on the OS.
- `_bg_color`: Background color used in the graphics window.
- `_canvas_tsize`: Default text size.
- `_keysdown`: Dictionary that tracks currently pressed keys.
- `_keyswaiting`: Dictionary that tracks unprocessed key events.

## Function Relationships
- `begin_graphics` initializes the window and canvas, preparing for drawing.
- `refresh` updates the canvas to reflect current state.
- `clear_screen` clears the canvas and redraws the background.
- Functions such as `polygon`, `circle`, and `square` are responsible 
  for drawing shapes.
- `move_to` and `move_by` adjust the position of shapes on the canvas.

---

## Function Docstrings

### `begin_graphics(width=640, height=480, color='#000000', title=None)`
Initializes the Tkinter graphics window with specified dimensions and color.

**Parameters**  
| Parameter | Type | Description |
|-----------|------|-------------|
| `width`   | int  | The width of the graphics window. Default is 640. |
| `height`  | int  | The height of the graphics window. Default is 480. |
| `color`   | str  | Background color in hex format. Default is black. |
| `title`   | str  | Title of the window. Default is 'Graphics Window'. |

**Returns**  
None

**Usage Example**  
```python
begin_graphics(800, 600, '#FFFFFF', 'My Graphics Window')
```

### `end_graphics()`
Closes the graphics window and cleans up resources.

**Parameters**  
None

**Returns**  
None

**Usage Example**  
```python
end_graphics()
```

### `clear_screen(background=None)`
Clears the canvas and resets the position counters.

**Parameters**  
| Parameter   | Type  | Description |
|-------------|-------|-------------|
| `background`| str   | Optional new background color in hex format. |

**Returns**  
None

**Usage Example**  
```python
clear_screen('#0000FF')
```

### `polygon(coords, outlineColor, fillColor=None, filled=1, smoothed=1, behind=0, width=1)`
Draws a polygon on the canvas based on the provided coordinates.

**Parameters**  
| Parameter     | Type               | Description |
|---------------|--------------------|-------------|
| `coords`      | list of tuples     | List of (x, y) tuples that define the vertices of the polygon. |
| `outlineColor`| str                 | Color of the outline in hex format. |
| `fillColor`   | str or None        | Color to fill the polygon. Default is same as `outlineColor`. |
| `filled`      | int (0 or 1)       | 1 to fill the polygon, 0 otherwise. |
| `smoothed`    | int (0 or 1)       | 1 to enable anti-aliasing, 0 otherwise. |
| `behind`      | int                | Draw behind other elements; affects visibility order. |
| `width`       | int                | Width of the polygon outline. |

**Returns**  
int - Identifier for the created polygon.

**Usage Example**  
```python
polygon([(0, 0), (100, 100), (100, 0)], '#FF0000')
```

### `square(pos, r, color, filled=1, behind=0)`
Draws a square based on the specified parameters.

**Parameters**  
| Parameter | Type  | Description |
|-----------|-------|-------------|
| `pos`     | tuple | Center position as (x, y). |
| `r`       | int   | Half the length of the square's side. |
| `color`   | str   | Color in hex format. |
| `filled`  | int   | 1 for filled, 0 for just outline. |
| `behind`  | int   | Draw behind other elements. |

**Returns**  
int - Identifier for the created square.

**Usage Example**  
```python
square((50, 50), 20, '#00FF00')
```

### `circle(pos, r, outlineColor, fillColor=None, endpoints=None, style='pieslice', width=2)`
Draws a circle or arc on the canvas.

**Parameters**  
| Parameter     | Type         | Description |
|---------------|--------------|-------------|
| `pos`         | tuple       | Center position as (x, y). |
| `r`           | int          | Radius of the circle. |
| `outlineColor`| str          | Color of the outline in hex format. |
| `fillColor`   | str or None  | Color to fill the circle. |
| `endpoints`   | list         | Angles to draw the arc (start, end). |
| `style`       | str          | Drawing style; default is 'pieslice'. |
| `width`       | int          | Width of the outline. |

**Returns**  
int - Identifier for the created circle or arc.

**Usage Example**  
```python
circle((150, 150), 30, '#0000FF', endpoints=[0, 180], style='arc')
```

### `move_to(object, x, y=None, d_o_e, d_w)`
Moves the specified object to new coordinates.

**Parameters**  
| Parameter | Type   | Description |
|-----------|--------|-------------|
| `object`  | int    | Identifier of the object to move. |
| `x`       | int    | Target x coordinate. |
| `y`       | int or None | Target y coordinate; if None, x must be a tuple. |
| `d_o_e`   | func   | Event-processing function to call. |
| `d_w`     | int    | Option for event processing. |

**Returns**  
None

**Usage Example**  
```python
move_to(object_id, (200, 200))
```

### Exception Hierarchy Documentation
Functions in this module can raise various exceptions due to user input 
or internal errors. The most common exceptions include:
- `ValueError`: Raised when an invalid parameter type or value is passed.
- `OSError`: Raised when file operations fail, such as loading an image.
- `IndexError`: Raised when accessing lists with out-of-bounds indices.

---

## Revision History Table

| Date Modified | Version Delta | Change Description                    | Author Initials |
|---------------|---------------|---------------------------------------|------------------|
| 2023-03-01    | 1.0.0         | Initial version                      | JD                |
| 2023-10-02    | 1.0.1         | Minor bug fixes and performance tweaks| JD                |