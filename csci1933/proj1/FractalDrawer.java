// Written by Emmet Hoversten, hover114
// FractalDrawer class draws a fractal of a shape indicated by user input

import java.awt.Color; // in order to use colors
import java.util.Scanner; // in order to take input


public class FractalDrawer {
    private double totalArea=0;  // member variable for tracking the total area
    private Color[] shapeColors = {Color.RED , Color.GREEN , Color.BLUE , Color.MAGENTA , Color.CYAN , Color.YELLOW , Color.BLACK, Color.GRAY , Color.DARK_GRAY , Color.LIGHT_GRAY , Color.ORANGE , Color.PINK};

    public FractalDrawer() {}  // constructor

    // drawFractal creates a new Canvas object
    // and determines which shapes to draw a fractal by calling appropriate helper function
    // drawFractal returns the area of the fractal
    public double drawFractal(String type) {
        Canvas fractalScreen = new Canvas(1000, 1000);

        if (type.equals("triangle")) {
            Triangle baseTriangle = new Triangle(450, 500, 150, 130);
            totalArea = totalArea + baseTriangle.calculateArea();
            fractalScreen.drawShape(baseTriangle);
            drawTriangleFractal(150, 130, 450, 500, shapeColors[0], fractalScreen, 7);
        }

        if (type.equals("circle")) {
            Circle baseCircle = new Circle(500, 500, 100);
            totalArea = totalArea + baseCircle.calculateArea();
            fractalScreen.drawShape(baseCircle);
            drawCircleFractal(100, 500, 500, shapeColors[0], fractalScreen, 7);
        }

        if (type.equals("rectangle")) {
            Rectangle baseRectangle = new Rectangle(450, 450, 100, 100);
            totalArea = totalArea + baseRectangle.calculateArea();
            fractalScreen.drawShape(baseRectangle);
            drawRectangleFractal(100, 100, 450, 450, shapeColors[0], fractalScreen, 7);
        }

        return totalArea;
    }

    // drawTriangleFractal draws a triangle fractal using recursive techniques
    public void drawTriangleFractal(double width, double height, double x, double y, Color c, Canvas can, int level){
        if (level == 0) {
            return;
        }
        else {
            double newY = y-((width*Math.tan(Math.atan((2*height)/width)))/4);
            Triangle outerTriangle1 = new Triangle(x+(width*.75), newY, width*.59, height*.59);
            Triangle outerTriangle2 = new Triangle(x+(width*.5)-(.5*.59*width), y+(height*.59), width*.59, height*.59);
            Triangle outerTriangle3 = new Triangle(x+(width*.25)-(width*.59), newY, width*.59, height*.59);
            outerTriangle1.setColor(c);
            totalArea = totalArea + outerTriangle1.calculateArea() + outerTriangle2.calculateArea() + outerTriangle3.calculateArea();
            can.drawShape(outerTriangle1);
            can.drawShape(outerTriangle2);
            can.drawShape(outerTriangle3);
            drawTriangleFractal(width*.59, height*.59, x+(width*.75), newY, shapeColors[level], can, level-1);
            drawTriangleFractal(width*.59, height*.59, x+(width*.5)-(.5*.59*width), y+(height*.59), shapeColors[level], can, level-1);
            drawTriangleFractal(width*.59, height*.59, x+(width*.25)-(width*.59), newY, shapeColors[level], can, level-1);
        }
    }

    // drawCircleFractal draws a circle fractal using recursive techniques
    public void drawCircleFractal(double radius, double x, double y, Color c, Canvas can, int level) {
        if (level == 0) {
            return;
        }
        else {
            Circle outerCircle1 = new Circle(x+radius*1.55, y, radius*.55);
            Circle outerCircle2 = new Circle(x-radius*1.55, y, radius*.55);
            Circle outerCircle3 = new Circle(x, y+radius*1.55, radius*.55);
            Circle outerCircle4 = new Circle(x, y-radius*1.55, radius*.55);
            outerCircle1.setColor(c);
            totalArea = totalArea + outerCircle1.calculateArea() + outerCircle2.calculateArea() + outerCircle3.calculateArea() + outerCircle4.calculateArea();
            can.drawShape(outerCircle1);
            can.drawShape(outerCircle2);
            can.drawShape(outerCircle3);
            can.drawShape(outerCircle4);
            drawCircleFractal(radius*.55, x+radius*1.55, y, shapeColors[level], can, level-1);
            drawCircleFractal(radius*.55, x-radius*1.55, y, shapeColors[level], can, level-1);
            drawCircleFractal(radius*.55, x, y+radius*1.55, shapeColors[level], can, level-1);
            drawCircleFractal(radius*.55, x, y-radius*1.55, shapeColors[level], can, level-1);
        }
    }

    // drawRectangleFractal draws a rectangle fractal using recursive techniques
    public void drawRectangleFractal(double width, double height, double x, double y, Color c, Canvas can, int level) {
        if (level == 0) {
            return;
        }
        else {
            Rectangle outerRectangle1 = new Rectangle(x-(width*.59*1.5), y-(height*.59*1.5), width*.59, height*.59);
            Rectangle outerRectangle2 = new Rectangle(x+width+(.5*width*.59), y-(height*.59*1.5), width*.59, height*.59);
            Rectangle outerRectangle3 = new Rectangle(x-(width*.59*1.5), y+(height)+(.5*.59*height), width*.59, height*.59);
            Rectangle outerRectangle4 = new Rectangle(x+width+(.5*width*.59), y+(height)+(.5*.59*height), width*.59, height*.59);
            outerRectangle1.setColor(c);
            totalArea = totalArea + outerRectangle1.calculateArea() + outerRectangle2.calculateArea() + outerRectangle3.calculateArea() + outerRectangle4.calculateArea();
            can.drawShape(outerRectangle1);
            can.drawShape(outerRectangle2);
            can.drawShape(outerRectangle3);
            can.drawShape(outerRectangle4);
            drawRectangleFractal(width*.59, height*.59, x-(width*.59*1.5), y-(height*.59*1.5), shapeColors[level], can, level-1);
            drawRectangleFractal(width*.59, height*.59, x+width+(.5*width*.59), y-(height*.59*1.5), shapeColors[level], can, level-1);
            drawRectangleFractal(width*.59, height*.59, x-(width*.59*1.5), y+(height)+(.5*.59*height), shapeColors[level], can, level-1);
            drawRectangleFractal(width*.59, height*.59, x+width+(.5*width*.59), y+(height)+(.5*.59*height), shapeColors[level], can, level-1);
        }
    }

    // asks user for shape input, and then draw the corresponding fractal.
    // prints area of fractal
    public static void main(String[] args){
        FractalDrawer shapeDrawer = new FractalDrawer();
        Scanner shapeScanner = new Scanner(System.in);
        System.out.print("What shape should make up your fractal?(triangle, circle, rectangle) ");
        String shapeInput = shapeScanner.nextLine();
        System.out.println(shapeDrawer.drawFractal(shapeInput)); // Draws fractal and prints area same line
        shapeScanner.close();
    }
}
