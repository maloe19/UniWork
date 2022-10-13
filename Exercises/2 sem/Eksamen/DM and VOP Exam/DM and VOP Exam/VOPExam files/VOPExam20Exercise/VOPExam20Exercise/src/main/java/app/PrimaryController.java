package app;

import callback.CallBackInterface;
import javafx.collections.FXCollections;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.stage.FileChooser;
import sprinter.ReadCSV;
import java.io.File;
import java.net.URL;
import java.util.ResourceBundle;

public class PrimaryController implements CallBackInterface, Initializable {
    private File selectedFile;
    private ReadCSV readCSV;

    @FXML
    private Button btn;
    @FXML
    private ComboBox cbx;
    @FXML
    private Label lbl1;
    @FXML
    private Label lbl2;
    @FXML
    private RadioButton rbtn1;
    @FXML
    private RadioButton rbtn2;
    @FXML
    private RadioButton rbtn3;
    @FXML
    private TextArea txta;

    public void readFile(ActionEvent actionEvent) {
        FileChooser fileChooser = new FileChooser();
        selectedFile = fileChooser.showOpenDialog(null);
        if (selectedFile!=null){
            readCSV = new ReadCSV(this, selectedFile);
            Thread t = new Thread(readCSV);
            t.isDaemon();
            t.start();
        }

    }

    public void sortAction(ActionEvent actionEvent) {
        //TODO

    }

    @Override
    public void updateStatus(String message) {
        cbx.setDisable(false);
        txta.setDisable(false);
        rbtn1.setDisable(false);
        rbtn2.setDisable(false);
        rbtn3.setDisable(false);
    }

    @Override
    public void updateView() {
        cbx.setItems(FXCollections.observableList(readCSV.getMap().keySet()));
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        cbx.setDisable(true);
        txta.setDisable(true);
        rbtn1.setDisable(true);
        rbtn2.setDisable(true);
        rbtn3.setDisable(true);
    }
}
