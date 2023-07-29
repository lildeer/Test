import java.io.*;
public class ToyWrite {
    public void writeToText (ToyStore toy) {
        File myFile = new File("text.txt");
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(myFile, true));
            writer.write(toy.toString());
            writer.write(",\n");
            writer.flush();
            writer.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}