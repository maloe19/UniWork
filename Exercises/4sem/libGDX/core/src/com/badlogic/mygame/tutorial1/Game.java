/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.badlogic.mygame.tutorial1;

import com.badlogic.gdx.ApplicationListener;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.mygame.tutorial1.GameInputProcessor;
import com.badlogic.mygame.tutorial1.GameKeys;
import com.badlogic.mygame.tutorial1.GameStateManager;

/**
 *
 * @author Bruger
 */
public class Game implements ApplicationListener {

    public static int WIDTH;
    public static int HEIGHT;
    public static OrthograchicCamera cam;
    private GameStateManager gsm;
    
    public void create() {
        WIDTH = Gdx.graphics.getWidth();
        HEIGHT = Gdx.graphics.getHeight();
        cam = new OrthograchicCamera(WIDTH, HEIGHT);
        cam.translate(WIDTH/2, HEIGHT/2);
        cam.update();
        Gdx.input.setInputProcessor(new GameInputProcessor());
        gsm = new GameStateManager();
    }

    public void render() {
        Gdx.gl.glClearColor(0,0,0,1);
        Gdx.gl.glClear(GL10.GL_COLOR_BUFFER_BIT);
        if(GameKeys.isPressed(GameKeys.SPACE)){
            System.out.println("SPACE");
        }
        gsm.update(Gdx.graphics.getDeltaTime());
        gsm.draw();
        GameKeys.update();
    }

    public void resize(int width, int height) {
    }

    public void pause() {
    }

    public void resume() {
    }

    public void dispose() {

    }
}

