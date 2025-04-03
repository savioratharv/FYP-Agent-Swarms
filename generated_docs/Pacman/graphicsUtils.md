# Graphics Utilities Documentation

## Overview
The `graphicsUtils.py` module provides a set of utilities for creating and managing a graphical interface using the Tkinter library in Python. This module includes functions to manage a drawing canvas, handle mouse and keyboard events, and render basic shapes and text.

## Function Overview

### `formatColor(r, g, b)`
Formats RGB values into a hex color string.
- **Parameters**:
  - `r`: Red component (0-1).
  - `g`: Green component (0-1).
  - `b`: Blue component (0-1).
- **Returns**: A hex color string formatted as `#RRGGBB`.

### `colorToVector(color)`
Converts a hex color string into a normalized RGB vector.
- **Parameters**:
  - `color`: A hex color string.
- **Returns**: A list containing the RGB components normalized between 0 and 1.

### `sleep(secs)`
Suspends execution for a specified number of seconds.
- **Parameters**:
  - `secs`: Number of seconds to sleep.

### `begin_graphics(width=640, height=480, color=formatColor(0, 0, 0), title=None)`
Initializes the graphics environment with a specified window size and background color.
- **Parameters**:
  - `width`: Width of the canvas.
  - `height`: Height of the canvas.
  - `color`: Background color of the canvas.
  - `title`: Title of the window.
- **Raises**: Exception if the window fails to initialize.

### `wait_for_click()`
Waits for a mouse click event and returns the position of the click and the button type.
- **Returns**: A tuple containing the position of the click and the button type ('left', 'right', or 'ctrl_left').

### `draw_background()`
Draws the background of the canvas using the specified background color.

### `end_graphics()`
Cleans up the graphics environment and closes the window. It handles exceptions during closure.

### `clear_screen(background=None)`
Clears the canvas and redraws the background.

### `polygon(coords, outlineColor, fillColor=None, filled=1, smoothed=1, behind=0, width=1)`
Draws a polygon on the canvas.
- **Parameters**:
  - `coords`: List of tuples representing the coordinates of the polygon vertices.
  - `outlineColor`: Color of the polygon outline.
  - `fillColor`: (Optional) Color to fill the polygon.
  - `filled`: (Optional) Boolean indicating whether the polygon should be filled.
  - `smoothed`: (Optional) Boolean indicating whether the polygon edges should be smoothed.
  - `behind`: (Optional) Layer position for rendering.
  - `width`: (Optional) Outline width.
- **Returns**: The identifier of the drawn polygon.

### `square(pos, r, color, filled=1, behind=0)`
Draws a square on the canvas.
- **Parameters**:
  - `pos`: Tuple indicating the center position of the square.
  - `r`: Half the length of a side of the square.
  - `color`: Color of the square.
  - `filled`: (Optional) Boolean to determine if the square should be filled.
  - `behind`: (Optional) Layer position for rendering.
- **Returns**: The identifier of the drawn square.

### `circle(pos, r, outlineColor, fillColor=None, endpoints=None, style='pieslice', width=2)`
Draws a circle or arc on the canvas.
- **Parameters**:
  - `pos`: Tuple indicating the center position of the circle.
  - `r`: Radius of the circle.
  - `outlineColor`: Color of the circle outline.
  - `fillColor`: (Optional) Color to fill the circle.
  - `endpoints`: (Optional) List specifying the start and end angles for arcs.
  - `style`: (Optional) Drawing style of the arc (default is 'pieslice').
  - `width`: (Optional) Outline width.
- **Returns**: The identifier of the drawn circle/arc.

### `image(pos, file="../../blueghost.gif")`
Displays an image at the specified position.
- **Parameters**:
  - `pos`: Tuple indicating the position where the image will be displayed.
  - `file`: (Optional) Path to the image file.
- **Returns**: The identifier of the displayed image.

### `refresh()`
Updates the canvas to reflect any changes made.

### `moveCircle(id, pos, r, endpoints=None)`
Moves a circle/arc to a new position and updates its properties.
- **Parameters**:
  - `id`: Identifier of the circle/arc to move.
  - `pos`: New position (x, y).
  - `r`: Radius of the circle.
  - `endpoints`: (Optional) New start and end angles for arcs.

### `edit(id, *args)`
Modifies properties of a graphic object.
- **Parameters**:
  - `id`: Identifier of the graphic object.
  - `*args`: Properties to update in key-value pairs.

### `text(pos, color, contents, font='Helvetica', size=12, style='normal', anchor="nw")`
Draws text onto the canvas.
- **Parameters**:
  - `pos`: Tuple indicating the position of the text.
  - `color`: Color of the text.
  - `contents`: The string content to display.
  - `font`: (Optional) Font type.
  - `size`: (Optional) Font size.
  - `style`: (Optional) Font style.
  - `anchor`: (Optional) Text anchor point.
- **Returns**: The identifier of the drawn text.

### `changeText(id, newText, font=None, size=12, style='normal')`
Changes the text of a previously drawn text object.
- **Parameters**:
  - `id`: Identifier of the text object.
  - `newText`: New text to display.
  - `font`: (Optional) New font type.
  - `size`: (Optional) New font size.
  - `style`: (Optional) New font style.

### `changeColor(id, newColor)`
Changes the color of a graphical object.
- **Parameters**:
  - `id`: Identifier of the object to change.
  - `newColor`: New color for the graphic.

### `line(here, there, color=formatColor(0, 0, 0), width=2)`
Draws a line between two points.
- **Parameters**:
  - `here`: Starting point (x, y).
  - `there`: Ending point (x, y).
  - `color`: (Optional) Color of the line.
  - `width`: (Optional) Width of the line.
- **Returns**: The identifier of the drawn line.

### `wait_for_keys()`
Waits for any key press and returns the pressed key(s).
- **Returns**: A list of keys that were pressed.

### `remove_from_screen(x, d_o_e=lambda arg: _root_window.dooneevent(arg), d_w=tkinter._tkinter.DONT_WAIT)`
Removes a graphical object from the canvas.
- **Parameters**:
  - `x`: Identifier of the object to remove.
  - `d_o_e`: (Optional) Function for event handling.
  - `d_w`: (Optional) Wait indicator.

### `move_to(object, x, y=None, d_o_e=lambda arg: _root_window.dooneevent(arg), d_w=tkinter._tkinter.DONT_WAIT)`
Moves a graphical object to a specified position.
- **Parameters**:
  - `object`: The identifier of the object to move.
  - `x`: New x coordinate.
  - `y`: (Optional) New y coordinate.
  - `d_o_e`: (Optional) Function for event handling.
  - `d_w`: (Optional) Wait indicator.

### `move_by(object, x, y=None, d_o_e=lambda arg: _root_window.dooneevent(arg), d_w=tkinter._tkinter.DONT_WAIT, lift=False)`
Moves a graphical object by a specified offset.
- **Parameters**:
  - `object`: The identifier of the object to move.
  - `x`: Offset for x direction.
  - `y`: (Optional) Offset for y direction.
  - `d_o_e`: (Optional) Function for event handling.
  - `d_w`: (Optional) Wait indicator.
  - `lift`: (Optional) Indicates if the object should be lifted to the foreground.

### `writePostscript(filename)`
Writes the current canvas state to a postscript file.
- **Parameters**:
  - `filename`: Path to the output file.

### Main Program
The main section of the script initializes the graphics window, draws shapes, and calls `sleep` to keep the window open momentarily for demonstration.