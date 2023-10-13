import hw3_images
import turtle
#initialize list
sc = turtle.Screen()
#setting up turtle
def setup_turtle():
    sc.colormode(255)
    sc.setup(450, 450)
    sc.setworldcoordinates(-225, -225, 225, 225)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-255, -255)
#convert color lists to grayscale
def grayscale_conversion(img):
    for pos1, i in enumerate(img):
        for pos2, j in enumerate(i):
            gray = sum(j)//3
            img[pos1][pos2] = [gray, gray, gray]
    return(img)
#draw's pixel given the position and color
def draw_pixel(x, y, color, pixel_size):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(pixel_size)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
#iterate through length of image and print pixel
def draw_image(img):
    pixel_size = (450/len(img))
    x = -230
    y = -215 + (pixel_size*(len(img)-1))
    for i in img:
        for j in i:
            draw_pixel(x, y, j, pixel_size)
            x += pixel_size
        x = -230
        y -= pixel_size
def main():
    #get image input and grayscale input
    image = input("Which image would you like?(img1, img2, img3, img4, bonus) ")
    ans = input("Do you want grayscale conversion?(y/n) ")
    #setup screen
    setup_turtle()
    #return image under given constraints
    if ans == "y":
        if image == "img1":
            draw_image(grayscale_conversion(hw3_images.img1))
        elif image == "img2":
            draw_image(grayscale_conversion(hw3_images.img2))
        elif image == "img3":
            draw_image(grayscale_conversion(hw3_images.img3))
        elif image == "img4":
            draw_image(grayscale_conversion(hw3_images.img4))
        elif image == "bonus":
            draw_image(grayscale_conversion(hw3_images.bonus))
    elif ans == "n":
        if image == "img1":
            draw_image(hw3_images.img1)
        elif image == "img2":
            draw_image(hw3_images.img2)
        elif image == "img3":
            draw_image(hw3_images.img3)
        elif image == "img4":
            draw_image(hw3_images.img4)
        elif image == "bonus":
            draw_image(hw3_images.bonus)
    else:
        print("Error. Bad input.")
if __name__ == "__main__":
    main()
#stop screen when user clicks on the screen
sc.exitonclick()