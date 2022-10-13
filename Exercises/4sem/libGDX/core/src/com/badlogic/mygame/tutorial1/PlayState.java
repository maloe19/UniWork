/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.badlogic.mygame.tutorial1;

import com.badlogic.mygame.tutorial1.Player;
import com.badlogic.mygame.tutorial1.GameState;
import com.badlogic.mygame.tutorial1.GameKeys;
import com.badlogic.mygame.tutorial1.GameStateManager;

/**
 *
 * @author Bruger
 */
public class PlayState extends GameState{
    private ShapeRenderer sr;
    private Player player;
    public PlayState(GameStateManager gsm){
        super(gsm);
        //init();
    }
    public void init(){
    sr = new ShapeRenderer();
    player = new Player();
    }
    public void update(float dt){
        //System.out.println("PLAY STATE UPDATING");
        handleInput();
        player.update(dt);
    }
    public void draw(){
        //System.out.println("PLAY STATE DRAWING");
        player.draw(sr);
    }
    public void handleInput(){
	player.setLeft(GameKeys.isDown(GameKeys.LEFT));
	player.setRight(GameKeys.isDown(GameKeys.RIGHT));
	player.setUp(GameKeys.isDown(GameKeys.UP));    
    }
    public void dispose(){}
}
