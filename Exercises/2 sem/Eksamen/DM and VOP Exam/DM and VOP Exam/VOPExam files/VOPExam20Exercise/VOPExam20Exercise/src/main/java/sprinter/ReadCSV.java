package sprinter;

import callback.CallBackInterface;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class ReadCSV implements Runnable {
    private CallBackInterface callBack;
    private File file;
    private Map<String, Set<Sprinter>> map;

    public ReadCSV(String fileName){
        callBack = new CallBackInterface() {
            @Override
            public void updateStatus(String message) {
                System.out.println(message);
            }

            @Override
            public void updateView() {
                System.out.println(map);
            }
        };
        this.map = new TreeMap();
        this.file = new File(fileName);

    }

    public ReadCSV(CallBackInterface callBack, File file) {
        this.map = new TreeMap();
        this.file = file;
        this.callBack = callBack;

    }

    public void run() {
        //TODO
        callBack.updateStatus("Reading Started" + "\n");
        callBack.updateStatus("Reading Completed" + "\n");
        callBack.updateView();
    }

    public Map<String, Set<Sprinter>> getMap() {
        return map;
    }

    private void readFile() {
        //TODO
        Scanner scan = null;
        try {
            //scan=new Scanner(new File(fileName));
            scan = new Scanner(file);

            String line;
            String[] split;
            Sprinter sprinter;

            while (scan.hasNextLine()) {
                line = scan.nextLine();
                split = line.split(",");

                sprinter = new Sprinter(Integer.parseInt(split[0]),
                        Integer.parseInt(split[1]),
                        Integer.parseInt(split[2]),
                        split[3],
                        split[4],
                        split[5]
                );
                this.getMap().containsKey(sprinter.getCountry());
                if (!map.containsKey(split[3])) {
                    map.put(split[3], new TreeSet<>());
                } else {
                    //map.put(sprinter, new TreeSet<>());
                    //map.put(split[3], sprinter);
                    //set.add(sprinter);
                }
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        scan.close();
    }

        public static void main(String[] args) {
        ReadCSV readCSV = new ReadCSV("challenge.csv");
        Thread t = new Thread(readCSV);
        t.isDaemon();
        t.start();
    }

}