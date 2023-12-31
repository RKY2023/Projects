import cairo
# python3 -m pip install pycairo
  
# creating a SVG surface
# # here geek is file name & 700, 700 is dimension
# with cairo.SVGSurface("geek.svg", 700, 700) as surface:
  
#     # creating a cairo context object
#     context = cairo.Context(surface)
  
#     # creating a rectangle(square) for left eye
#     context.rectangle(100, 100, 100, 100)
  
#     # creating a rectangle(square) for right eye
#     context.rectangle(500, 100, 100, 100)
  
#     # creating position for the curves
#     x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
#     x2, y2, x3, y3 = 0.4, 0.1, 0.9, 0.6
#     # x, y, x1, y1 = 0.1, 0.5, 0.5, 0.9
#     # x2, y2, x3, y3 = 0.5, 0.9, 0.9, 0.5
  
#     # setting scale of the context
#     context.scale(700, 700)
  
#     # setting line width of the context
#     context.set_line_width(0.01)
  
#     # move the context to x,y position
#     context.move_to(x, y)
  
#     # draw the curve for smile
#     context.curve_to(x1, y1, x2, y2, x3, y3)
  
#     # setting color of the context
#     context.set_source_rgba(0.4, 1, 0.4, 1)
  
#     # stroke out the color and width property
#     context.stroke()
# # printing message when file is saved
# print("File Saved")
import math
import cairo

WIDTH, HEIGHT = 256, 256

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba(.5, .5, .5, 0, 0.5)  # First stop, 50% opacity
pat.add_color_stop_rgba(.5, .5, .5, 0.2, 1)  # Last stop, 100% opacity

ctx.rectangle(0.1, 0.1, 1, 1)  # Rectangle(x0, y0, x1, y1)

ctx.set_source(pat)
ctx.fill()

ctx.translate(0.1, 0.1)  # Changing the current transformation matrix

# ctx.move_to(0, 0)
# # Arc(cx, cy, radius, start_angle, stop_angle)
# ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
# ctx.line_to(0.5, 0.1)  # Line to (x,y)
# # Curve(x1, y1, x2, y2, x3, y3)
# ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
# ctx.close_path()

# ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
# ctx.set_line_width(0.02)
ctx.stroke()

surface.write_to_png("example.png")  # Output to PNG
  
  
