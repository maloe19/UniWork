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
public class SpaceObject {
    protected float x;
    protected float y;
            
    protected float dx;
    protected float dy;
    
    protected float radians;
    protected float speed;
    protected float rotationspeed;

    protected float width;
    protected float height;   
    
    protected float[] shapex;
    protected float[] shapey;
    
    protected void wrap(){
        if(x < 0) x = Game.WIDTH;
	if(x > Game.WIDTH) x = 0;
	if(y < 0) y = Game.HEIGHT;
	if(y > Game.HEIGHT) y = 0; 
    }
}
