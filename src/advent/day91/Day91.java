package advent.day91;

public class Day91 {
	public static void Assert(boolean test) {
		if (test == false) {
			throw new RuntimeException();
		}
	}

	public static void main(String[] argv) {
		final Day91 day9 = new Day91();
		Day91.Assert(day9.execute(9, 25) == 32);
		Day91.Assert(day9.execute(10, 1618) == 8317);
		Day91.Assert(day9.execute(13, 7999) == 146373);
		Day91.Assert(day9.execute(17, 1104) == 2764);
		Day91.Assert(day9.execute(21, 6111) == 54718);
		Day91.Assert(day9.execute(30, 5807) == 37305);
		System.out.println(day9.execute(427, 7072300));
	}

	private int execute(int playerCount, int lastMarbleScore) {
		System.out.println("====================");
		final Circle circle = new Circle();
		int marbleNumber = 1;
		while (marbleNumber < lastMarbleScore) {
			System.out.print("*");
			for (int player = 1; player <= playerCount; player++) {
				circle.placeMarble(marbleNumber, player);
				marbleNumber++;

				if (marbleNumber > lastMarbleScore) {
					break;
				}
			}
		}
		System.out.println("Top score is " + circle.topScore());
		return circle.topScore();
	}
}
