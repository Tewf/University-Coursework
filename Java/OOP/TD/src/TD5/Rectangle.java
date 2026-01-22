package TD5;

/**
 * Simple integer rectangle used to describe layout boxes for expression trees.
 * The fields are public for convenience in this teaching example.
 */
public class Rectangle {
    public int x, y, width, height;

    /**
     * Create a rectangle with top-left corner (x,y) and given width/height.
     */
    public Rectangle(int x, int y, int width, int height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    @Override
    public String toString() {
        return "Rectangle(" + x + "," + y + "," + width + "," + height + ")";
    }
}
