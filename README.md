# painting
This is a WIP python script that takes an image and attempts to pixelate it in an aesthetically pleasing way

My inspiration comes from [reddit user alternateartreality](https://www.reddit.com/user/alternateartreality/?sort=top) who makes very cool art work with
large blocky brush strokes. More specifically, [this](https://i.redd.it/ekooxh1zknm61.jpg) painting of the earth gave me the idea of making a program that
could make similar art with large blocky sections.

I wanted to make the program generate something that I could use as a guide for my own painting in this style

At first I was making this program super specialized to make me a pixelated image that resembled the ocean from a top down perspective, but I've since tried making
the program more generalized. Here's a quick history of this projects developement:
- Tried using python PIL
- Tried using random rectangles to generate image
- Tried mathplotlib quantization to get average colors
- Tried numpy grid to work with mathplotlib
- couldn't get them to work
- Tried PIL again
- Tried PIL and numpy
- Tried PIL and numpy and mathplotlib
- Tried PIL Quantization
- It works!
- Quantization isn't actually what I want
- Quantization gets average of colors, I want mode
- use PIL to get frequency of each color
- success!

that's pretty much where I'm at. Here is my to do list:
- prioritize representation of secondary colors to break up solid blocks of color
