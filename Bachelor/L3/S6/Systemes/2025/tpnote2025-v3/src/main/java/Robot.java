
public class Robot implements Runnable {

	private int x, y, diam;
	private int dx, dy;

	private Room space;

	public Robot(Room s) {
		space = s;
		diam = 20;
		x = (int) (Math.random() * (s.getWidth() - diam));
		y = (int) (Math.random() * (s.getHeight() - diam));
		dx = (int) (diam / 2 - Math.random() * diam);
		dy = (int) (diam / 2 - Math.random() * diam);
		s.add(this);
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

	public int getDiam() {
		return diam;
	}

	@Override
	public void run() {
		try {
			while (true) {

				Thread.sleep(25);

				x += dx;
				y += dy;
                				
				if (x + diam + dx >= space.getWidth()) {
				    dx -= 1;
				    x = space.getWidth() - diam;
				    space.rightBorderTouched();
				} else if (x + dx <= 0) {
				    dx -= 1;
				    x = 0;
				    space.leftBorderTouched();
				}

				if (y + diam + dy >= space.getHeight()) {
				    dy -= 1;
				    y = space.getHeight() - diam;
				    space.bottomBorderTouched();
				} else if (y + dy <= 0) {
				    dy -= -1;
				    y = 0;
				    space.topBorderTouched();
				}
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}

}
