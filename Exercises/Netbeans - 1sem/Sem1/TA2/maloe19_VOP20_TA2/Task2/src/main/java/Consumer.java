import java.util.Random;

public class Consumer implements Runnable {
    private int randomNumber;
    private Random random = new Random();

    public Consumer() {
        new Thread(this).start();
        randomNumber = random.nextInt(300);
    }

    public void run() {
        try {
            while(true){
               //buffer
                Thread.sleep(randomNumber);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
    }
}}
