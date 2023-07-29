import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ToyStore {
    public static class Toy {
        private int id;
        private String name;
        private int quantity;
        private int weight;

        public Toy(int id, String name, int quantity, int weight) {
            this.id = id;
            this.name = name;
            this.quantity = quantity;
            this.weight = weight;
        }

        public int getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public int getQuantity() {
            return quantity;
        }

        public int getWeight() {
            return weight;
        }
    }

    private List<Toy> toys;

    public ToyStore() {
        toys = new ArrayList<>();
    }

    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public Toy getRandomToy() {
        int totalWeight = 0;
        for (Toy toy : toys) {
            totalWeight += toy.getWeight();
        }

        Random random = new Random();
        int randomNumber = random.nextInt(totalWeight);

        int weightSum = 0;
        for (Toy toy : toys) {
            weightSum += toy.getWeight();
            if (randomNumber < weightSum) {
                return toy;
            }
        }

        return null;
    }
    @Override
    public String toString() {
        return this.getRandomToy().getName();

    }
}