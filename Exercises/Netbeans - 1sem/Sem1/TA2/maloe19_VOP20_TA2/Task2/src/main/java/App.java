/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package vop;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import vop.FXMLDocumentController;

import java.io.IOException;

/**
 *
 * @author erso
 */
public class App extends Application {
    private static Scene scene;

    @Override
    public void start(Stage stage) throws IOException {
        scene = new Scene(loadFXML("FXMLDocument"));
        stage.setScene(scene);
        stage.setTitle("VOP TA");
        stage.show();
    }

    static void setRoot(String fxml) throws IOException {
        scene.setRoot(loadFXML(fxml));
    }

    private static Parent loadFXML(String fxml) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(FXMLDocumentController.class.getResource(fxml + ".fxml"));
        return fxmlLoader.load();
    }

    public static void launch(String[] args) {
        launch();
    }

}
