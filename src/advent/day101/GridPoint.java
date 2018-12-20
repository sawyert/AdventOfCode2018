package advent.day101;

public class GridPoint {
	public int x;
	public int y;
	private final int vx;
	private final int vy;

	public GridPoint(String pointdesc) {
		// position=< 3, -2> velocity=<-1, 1>
		String processed = pointdesc.substring("position=<".length());
		String location = processed.substring(0, processed.indexOf(">")).trim();
		processed = processed.substring(processed.indexOf(">") + 1);
		processed = processed.substring(" velocity=<".length());
		String velocity = processed.trim().substring(0, processed.trim().length() - 1);
		String[] locations = location.split(",");
		this.x = Integer.parseInt(locations[0].trim());
		this.y = Integer.parseInt(locations[1].trim());
		String[] velocities = velocity.split(",");
		this.vx = Integer.parseInt(velocities[0].trim());
		this.vy = Integer.parseInt(velocities[1].trim());
	}

	public void tick() {
		this.x = this.x + this.vx;
		this.y = this.y + this.vy;
	}

	public boolean at(int x2, int y2) {
		if (x2 == this.x && y2 == this.y) {
			return true;
		}
		return false;
	}
}
