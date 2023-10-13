// Written by Emmet Hoversten, hover114
import java.awt.Color;
// Holds attributes and methods of a Triangle
public class Triangle {
    //initializing attribute variables
    private double xPos = 0.0;
    private double yPos = 0.0;
    private double width = 0.0;
    private double height = 0.0;
    private Color triangleColor;

    public Triangle(double x, double y, double triWidth, double triHeight) { // constructor
        xPos = x;
        yPos = y;
        width = triWidth;
        height = triHeight;
    }

    public double calculatePerimeter() { // calculates and returns perimeter with objects' width and height
        return 2 * (Math.sqrt((width/2) * (width/2) + (height * height))) + width;
    }

    public double calculateArea() { // calculates  and returns area with objects' width and height
        return 0.5 * width * height;
    }

    public void setColor(Color newColor) { // takes in Color object and modifies the objects' color
        this.triangleColor = newColor;
    }

    public void setPos(double x, double y) { // takes in x,y position and sets to objects x,y attributes
        xPos = x;
        yPos = y;
    }

    public void setHeight(double newHeight) { // takes in height and sets as objects' height attribute
        height = newHeight;
    }

    public void setWidth(double newWidth) { // takes in width adn sets to the width of the object
        width = newWidth;
    }

    public Color getColor() { // getter method for the color attribute
        return this.triangleColor;
    }

    public double getXPos() { // getter method for x position
        return xPos;
    }

    public double getYPos() { // getter method for y position
        return yPos;
    }

    public double getHeight() { // getter method for height
        return height;
    }

    public double getWidth() { // getter method for width
        return width;
    }
}
