package vop;

import javafx.application.Platform;

import java.util.function.Consumer;

public class CircularBuffer {
    private String[] array;

    public CircularBuffer(int size, vop.CallbackInterface callback) {
        array = new String[5];
        array[0] = "0";
        array[1] = "0";
    }

    public synchronized String get() {
        Producer producer = new Producer(new Runnable() {
            public void run() {
                if (array == "null") {
                    for (int i = 0; i < array.length; i++) {
                        array.add(producer.readFile(String word));
                    }
                } else {
                    wait();
            }
        });
    }

    public synchronized void put(String word) {
        Consumer consumer = new Consumer((new Runnable() {
            public void run() {
                if (!array == "null") {
                    for (int i = 0; i < array.length; i++) {
                        array.remove(producer.readFile(String word));
                }
            });
    }

    @Override
    public String toString() {
        StringBuilder formatted = new StringBuilder();
        /*for (int i = 0; i < size; i++) {
            String value = buffer[i] == null ? "*Empty*" : buffer[i];
            formatted.append(String.format("[%d]: %s\n", i + 1, value));
        }*/
        return formatted.toString();
    }


    public static void main(String[] args) {
        CircularBuffer circularBuffer = new CircularBuffer(5, new vop.CallbackInterface() {
            @Override
            public void producerNotify(String word) {
                System.out.println("Producer: \"" + word + "\" added.");
            }

            @Override
            public void consumerNotify(String word) {
                System.out.println("Consumer: \"" + word + "\" retrieved.");
            }
        });
        new Producer(circularBuffer, "loremipsum1.txt");
        new Producer(circularBuffer, "loremipsum2.txt");
        new Producer(circularBuffer, "loremipsum3.txt");
        new Consumer(circularBuffer);
    }
}

