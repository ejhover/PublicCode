#using turtles, prints random binary tree on the screen
import random
import turtle
class Node:
    def __init__(self, num):
        self.num = num
        self.right = None
        self.left = None
    def __repr__(self):
        return str(self.num)
class Tree():
    def __init__(self):
        self.head = None
        self.trt = turtle.Turtle()
        self.trtscreen = turtle.Screen()
        self.nodelist = []
    def sor(self, lis, median):
        try:
            median.right = lis[lis.index(median)+1:][len(lis[lis.index(median)+1:])//2]
            median.left = lis[:lis.index(median)][len(lis[:lis.index(median)])//2]
            self.sor(lis[:lis.index(median)], median.left)
            self.sor(lis[lis.index(median)+1:], median.right)
        except:
            try:
                median.right = lis[lis.index(median)+1:][len(lis[lis.index(median)+1:])//2]
            except:
                pass
            try:
                median.left = lis[:lis.index(median)][len(lis[:lis.index(median)])//2]
            except:
                pass
    def randomize(self):
        length = random.randint(3, 20)
        num_list = []
        node_list = []
        for i in range(length):
            num_list.append(random.randint(1, 99))
        for i in set(num_list):
            node_list.append(Node(i))
        node_list.sort(key=lambda x: int(x.__repr__()))
        self.nodelist = node_list
        self.head = node_list[len(node_list)//2]
        self.sor(node_list, self.head)
    def recurse_draw(self, currx, curry, currnode, leftangle, rightangle, length):
        if currnode.left != None:
            self.trt.penup()
            self.trt.setx(currx-20)
            self.trt.sety(curry+12)
            self.trt.setheading(leftangle)
            self.trt.pendown()
            self.trt.fd(length)
            self.trt.penup()
            self.trt.goto(self.trt.xcor(), self.trt.ycor()-40)
            self.trt.setheading(0)
            self.trt.pendown()
            self.trt.circle(20)
            self.trt.penup()
            self.trt.setx(self.trt.xcor()-8)
            self.trt.sety(self.trt.ycor()+10)
            self.trt.write(f'{currnode.left.__repr__()}', font=("Verdana", 12, "normal"))
            self.trt.setx(self.trt.xcor()+8)
            self.trt.sety(self.trt.ycor()-10)
            self.recurse_draw(self.trt.xcor(), self.trt.ycor(), currnode.left, leftangle+32, rightangle-32, length-15)
        if currnode.right != None:
            self.trt.penup()
            self.trt.setx(currx+20)
            self.trt.sety(curry+12)
            self.trt.setheading(rightangle)
            self.trt.pendown()
            self.trt.fd(length)
            self.trt.penup()
            self.trt.goto(self.trt.xcor(), self.trt.ycor()-40)
            self.trt.setheading(0)
            self.trt.pendown()
            self.trt.circle(20)
            self.trt.penup()
            self.trt.setx(self.trt.xcor()-8)
            self.trt.sety(self.trt.ycor()+10)
            self.trt.write(f'{currnode.right.__repr__()}', font=("Verdana", 12, "normal"))
            self.trt.setx(self.trt.xcor()+8)
            self.trt.sety(self.trt.ycor()-10)
            self.recurse_draw(self.trt.xcor(), self.trt.ycor(), currnode.right, leftangle+32, rightangle-32, length-15)
    def draw_tree(self):
        self.trt.penup()
        self.trt.speed(0)
        self.trt.hideturtle()
        self.trt.setheading(90)
        self.trt.fd(300)
        self.trt.setheading(0)
        self.trt.pendown()
        self.trt.circle(20)
        self.trt.penup()
        self.trt.setx(self.trt.xcor()-8)
        self.trt.sety(self.trt.ycor()+10)
        self.trt.write(f'{self.head.__repr__()}', font=("Verdana", 12, "normal"))
        self.trt.setx(self.trt.xcor()+8)
        self.trt.sety(self.trt.ycor()-10)
        self.recurse_draw(self.trt.xcor(), self.trt.ycor(), self.head, -155, -25, 90)
        self.trtscreen.mainloop()
    def print_tree(self):
        # supposed to print out characters representing the binary tree
        spaces = 0
        for i in self.nodelist:
            if (i.left == None) and (i.right == None):
                spaces+=1
        spaces*=2
    def __repr__(self):
        val_list = []
        for i in self.nodelist:
            val_list.append(str(i.num))
        return "<-".join(val_list[:self.nodelist.index(self.head)+1]) + "->" + "->".join(val_list[self.nodelist.index(self.head)+1:])
def main():
    rand_tree = Tree()
    rand_tree.randomize()
    print(rand_tree)
    rand_tree.draw_tree()
if __name__ == "__main__":
    main()
