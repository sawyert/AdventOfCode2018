package advent.day101;

import java.util.ArrayList;
import java.util.List;

public class Grid {

	private final List<GridPoint> points = new ArrayList<>();
	private int minX = 0;
	private int minY = 0;
	private int maxX = 0;
	private int maxY = 0;
	private int tick = 0;
	private int prevY;
	private int prevX;

	public void init(String testdata) {
		String[] lines = testdata.split("\n");
		for (String line : lines) {
			this.points.add(new GridPoint(line));
		}
	}

	public void tick() {
		this.tick++;
		for (GridPoint point : this.points) {
			point.tick();
		}
	}

	public void printGrid() {
		System.out.println();
		this.calcExtents();
		for (int y = this.minY; y <= this.maxY; y++) {
			for (int x = this.minX; x <= this.maxX; x++) {
				boolean found = false;
				for (GridPoint point : this.points) {
					if (point.at(x, y)) {
						found = true;
					}
				}

				if (found) {
					System.out.print("#");
				} else {
					System.out.print(".");
				}
			}
			System.out.println();
		}
	}

	private void calcExtents() {
		this.maxX = 0;
		this.minX = 0;
		this.maxY = 0;
		this.minY = 0;
		for (GridPoint point : this.points) {
			if (point.x < this.minX) {
				this.minX = point.x;
			}
			if (point.x > this.maxX) {
				this.maxX = point.x;
			}
			if (point.y < this.minY) {
				this.minY = point.y;
			}
			if (point.y > this.maxY) {
				this.maxY = point.y;
			}
		}

	}

	public void printGridDimensions() {
		this.prevX = this.maxX - this.minX;
		this.prevY = this.maxY - this.minY;
		this.calcExtents();
		int newX = this.maxX - this.minX;
		int newY = this.maxY - this.minY;
		System.out.print(this.tick);
		System.out.print(":");
		System.out.print(newX);
		System.out.print(",");
		System.out.print(newY);
		System.out.print("      ");
		System.out.print(newX - this.prevX);
		System.out.print(",");
		System.out.print(newY - this.prevY);
		System.out.println();

	}

}
