// Written by Emmet Hoversten, hover114
import java.awt.Color;
// Holds attributes and methods of a Rectangle
public class Rectangle {
    //initializing attribute variables
    private double xPos = 0.0;
    private double yPos = 0.0;
    private double width = 0.0;
    private double height = 0.0;
    private Color rectangleColor;

    public Rectangle(double x, double y, double rectWidth, double rectHeight) { // constructor
        xPos = x;
        yPos = y;
        width = rectWidth;
        height = rectHeight;
    }

    public double calculatePerimeter() { // calculates and returns the perimeter of the rectangle object
        return (width * 2) + (height * 2);
    }

    public double calculateArea() { // calculates and returns the area of the rectangle object
        return width * height;
    }

    public void setColor(Color newColor) { // takes in a Color object and modifies the color attribute of the rectangle, outputs nothing
        rectangleColor = newColor;
    }

    public void setPos(double x, double y) { // takes in x,y coordinates and modidfies x,y position attributes of the rectangle
        xPos = x;
        yPos = y;
    }

    public void setHeight(double newHeight) { // takes in height of rectangle and changes the height attribute of the rectangle
        height = newHeight;
    }

    public void setWidth(double newWidth) { // takes in width and modifies the width attribute of the rectangle object to input
        width = newWidth;
    }

    public Color getColor() { // getter method to return the color attribute of the rectangle
        return rectangleColor;
    }

    public double getXPos() { // getter method to return x position
        return xPos;
    }

    public double getYPos() { // getter method to return y position
        return yPos;
    }

    public double getHeight() { // getter method to return height
        return height;
    }

    public double getWidth() { // getter method to return width
        return width;
    }    
}
