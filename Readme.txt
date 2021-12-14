MIT License

Copyright (c) [2021]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Game References:
1. PyGame example from http://sloankelly.net
2. Background midi reference from https://inventwithpython.com/invent4thed/

Game environment requirements:
1. Python version 3.8
2. pygame 2.1.0 (SDL 2.0.16, Python 3.8.5)
3. Display screen resolution: 720p (1280 x 720)

Files included:
1. Readme.txt
2. Screen capture: GameUI.png
3. Assets: apple.png, banana.png, monkey.png
4. Multimedia audio file: background.mid (background music audio file: midi format)
5. startGame.py (Python Game file)

Function used in the project:

1.pygame.init()
initialize all imported pygame modules

2.pygame.time.Clock()
update the clock
tick(framerate=0) -> milliseconds
This method should be called once per frame.
It will compute how many milliseconds have passed since the previous call.

3. pygame.display.set_mode()
Initialize a window or screen for display
set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
This function will create a display Surface.
The arguments passed in are requests for a display type.
The actual created display will be the best possible match supported by the system.

4. pygame.display.set_caption()
Set the current window caption
set_caption(title, icontitle=None) -> None
If the display has a window title, this function will change the name on the window.
Some systems support an alternate shorter title to be used for minimized displays.

5. pygame.display.update()
Update portions of the screen for software displays

6. pygame.Color()
pygame object for color representations
Color(r, g, b) -> Color

7. pygame.mixer.music module
pygame module for controlling streamed audio

8. pygame.image.load()
load new image from a file (

9. pygame.font.Font()
create a new Font object from a file

10. pygame.event.get()
get events from the queue (for example mouse move event, keyboard press event)

11. pygame.key.get_pressed()
get the state of all keyboard buttons

12. pygame.quit()
uninitialize all pygame modules








