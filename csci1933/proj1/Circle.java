// Written by Emmet Hoversten, hover114
import java.awt.Color;
// Holds attributes and methods of a Circle
public class Circle {
    //initializing attribute variables
    private double xPos = 0.0;
    private double yPos = 0.0;
    private double radius = 0.0;
    private Color circleColor;

    public Circle(double x, double y, double circleRadius) { //constructor
        xPos = x;
        yPos = y;
        radius = circleRadius;
    }

    public double calculatePerimeter() { //returns the perimeter of the circle
        return Math.PI * 2.0 * radius;
    }

    public double calculateArea() { //returns the area of the circle
        return Math.PI * (radius * radius);
    }

    public void setColor(Color newColor) { //takes in a color object and redefines the color of the circle
        circleColor = newColor;
    }

    public void setPos(double x, double y) { //takes in new coordinates and redefines the position of the circle
        xPos = x;
        yPos = y;
    }

    public void setRadius(double circleRadius) { //takes in a radius value and redefines the radius of the circle
        radius = circleRadius;
    }

    public Color getColor() { //accessor method for the circles' color
        return circleColor;
    }

    public double getXPos() { //accessor method for the x position of the circle
        return xPos;
    }

    public double getYPos() { //accessor method for the y position of the cirle
        return yPos;
    }

    public double getRadius() { //accessor method for the radius of the circle
        return radius;
    }
}
