package advent.day92;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class Circle {

	private final Map<Integer, Integer> scores = new HashMap<>();
	private final LinkedList<Integer> data = new LinkedList<>();
	private int currentMarbleNumber = 0;
	private int lastPlayerNumber = 0;
	private int time = 0;

	public Circle() {
		this.data.add(new Integer(0));
	}

	private void addScore(int player, int score) {
		Integer existingScore = this.scores.get(new Integer(player));
		if (existingScore == null) {
			existingScore = new Integer(0);
		}

		this.scores.put(new Integer(player), new Integer(existingScore.intValue() + score));
		// System.out.println("Score for player " + player + " is now " +
		// this.scores.get(player));
	}

	public void placeMarble(int marbleNumber, int player) {
		this.lastPlayerNumber = player;
		if (marbleNumber % 10000 == 0) {
			System.out.println(marbleNumber);
		}

		if (marbleNumber % 23 == 0) {
			this.addScore(player, marbleNumber);

			int marblePositionToRemove = this.currentMarbleNumber - 7;
			if (marblePositionToRemove < 0) {
				marblePositionToRemove = this.data.size() + marblePositionToRemove;
			}
			final int score = this.data.get(marblePositionToRemove);
			this.addScore(player, score);
			this.data.remove(marblePositionToRemove);
			this.currentMarbleNumber = marblePositionToRemove;

			this.printStructure();
			return;
		}

		if (this.data.size() == 1) {
			this.data.add(new Integer(marbleNumber));
			this.currentMarbleNumber = 1;
		} else if (this.data.size() == 2) {
			this.data.add(1, new Integer(marbleNumber));
			this.currentMarbleNumber = 1;
		} else if (this.data.size() == 3) {
			this.data.add(new Integer(marbleNumber));
			this.currentMarbleNumber = 3;
		} else {
			if (this.currentMarbleNumber == this.data.size() - 1) {
				this.data.add(1, new Integer(marbleNumber));
				this.currentMarbleNumber = 1;
			} else {
				this.data.add(this.currentMarbleNumber + 2, new Integer(marbleNumber));
				this.currentMarbleNumber = this.currentMarbleNumber + 2;
			}
		}
		this.time++;
		this.printStructure();
	}

	public void printStructure() {
		if (false) {
			System.out.print("[" + this.lastPlayerNumber + "]");
			System.out.print(" ");
			int count = 0;
			for (final Integer value : this.data) {
				if (count == this.currentMarbleNumber) {
					System.out.print("[" + value + "]");
				} else {
					System.out.print(value);
				}
				System.out.print(" ");
				count++;
			}
			System.out.println();
		}
	}

	public int topScore() {
		int topScore = 0;
		for (final Integer score : this.scores.values()) {
			if (score.intValue() > topScore) {
				topScore = score.intValue();
			}
		}
		return topScore;
	}

}
