/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.badlogic.mygame.tutorial1;

/**
 *
 * @author Bruger
 */
public class GameStateManager {
    private GameState gameState;
    public static final int MENU = 0;
    public static final int PLAY = 893746;
    
    public GameStateManager(){
        setState(PLAY);
    }
    public void setState(int state){
        if(gamestate != null)gameState.dispose();
        if(state == MENU){
            
        }
        if(state == PLAY){
            gameState = new PlayState(this);
        }
    }
    public void update(float dt){
        gameState.update(dt);
    }
    public void draw(){
        gameState.draw();
    }
}
