from PIL import Image
import random

#size of section being analyzed
size = 50
#size of picture being analyzed
width = 3000
height = 2400

#tracks how much is done for console %
done = 0

def main():

    random.seed()
    with Image.open("ocean.png") as originalPic:
        #top right of first square to evaluate
        left = width - size
        top = height - size
        #bottom right of crop
        right = width
        bottom = height

        global done     

        generatedIm = Image.new('RGB',(3000,2400))
        for y in range(int(height / size)):
            #move horizontally from right to left finding dominant colors and placing in final image
            left = width - size
            right = width
            for x in range(int(width / size)):
                
                section = originalPic.crop((left,top,right,bottom))

                #I like the idea of changing the shape of the sections being analyzed but it over
                #generalizes the colors of the section because we currently only use the most dom color
                '''
                if random.randint(0,1):
                    #horizontal
                    if x < int(width / size):
                        section = section.crop((left-size,top,right,bottom))
                    else:
                        section = section.crop((left,top,right+size,bottom))
                else:
                    #vertical
                    if y != int(height / size):
                        section = section.crop((left,top-size,right,bottom))
                    else:
                        section = section.crop((left,top,right,bottom+size))
                '''
                #quantize to find dominant color in section
                colors = section.convert('RGB').getcolors()
                #print(f"section:{section}") #DEBUG
                #print(f"colors:{colors}") #DEBUG
                biggest = (max(colors))
                generatedIm.paste(biggest[1],(left,top,right,bottom))
                #reduce left and right so next loop quantizes 50px to the left
                left += -size
                right += -size
            #reduce top and bottom so next loop quantizes 50px toward the top
            top += -size
            bottom += -size
            if ((y / int(height / size)) * 100 >= done + 10):
                done = (y / int(height / size)) * 100
                print(f"{(y / int(height / size)) * 100}%")
        generatedIm.show()
        generatedIm.save("pixelpainting.png")
    print(f"end")

if __name__ == "__main__":
    main()