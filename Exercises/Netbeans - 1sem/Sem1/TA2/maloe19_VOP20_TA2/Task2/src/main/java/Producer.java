import java.io.File;
import java.io.FileNotFoundException;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Producer implements Runnable{
    private int randomNumber;
    private Random random = new Random();

    public Producer() {
        new Thread(this).start();
        randomNumber = random.nextInt(300);
    }

    public Set<String> readFile(String myfile) {
        try {
            File myFile = new File("C:\\Users\\Bruger\\Downloads\\TASK2\\ta-proposal-test-time\\loremipsum1");
            Scanner reader = new Scanner(myFile);
            for (int i = 0; i < myFile.length(); i++) {
                readFile(myfile).add(reader.nextLine());
            }
            reader.close();
        } catch (FileNotFoundException ex) {
            Logger.getLogger(Producer.class.getName()).log(Level.SEVERE, null, ex);
        }
    }


    public void run() {
        try {
            String myfile = new String("C:\\Users\\Bruger\\Downloads\\TASK2\\ta-proposal-test-time\\loremipsum1");;
            readFile(myfile);
            //buffer
            Thread.sleep(randomNumber);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
