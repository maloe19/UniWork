package vop;

import javafx.application.Platform;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;

public class FXMLDocumentController {


    public TextArea producers_log;
    public TextArea consumer_log;
    public Button btn_start;
    public TextField consumer_size;
    public TextField consumer_last_word;
    private CircularBuffer circularBuffer;

    public void start(MouseEvent mouseEvent) {
        //Implement CircularBuffer and instantiate it before starting the producers and consumer
        
        //new Producer(circularBuffer, "loremipsum1.txt");
        //new Producer(circularBuffer, "loremipsum2.txt");
        //new Producer(circularBuffer, "loremipsum3.txt");
        //new Consumer(circularBuffer);
        btn_start.setDisable(true);
    }
}
