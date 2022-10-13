import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent {

  public playerX = 3;
	public walkableTiles = ["➖","🌉","⬆️","⬇️","🏁"];
  public gameOver = false;
  public tiles: Array<{ index: number, emoji: string }>;

  constructor() { 
    let s = ["⛔️","➖","➖","➖","➖","➖","➖","➖","➖","⬆️","➖","➖","➖","➖","➖","➖",
              "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","➖","➖","➖","➖","➖","🏁","➖","⛔️"];
    this.tiles = []; 
    for (let i=0; i<s.length; i++) {
      this.tiles.push({ index: i, emoji: s[i] });
    }
  }

  public left() {
		let newX = this.playerX - 1;
		if (this.walkableTiles.indexOf(this.tiles[newX].emoji) != -1) {
      this.playerX = newX;
      if (this.tiles[this.playerX].emoji == '🏁') this.gameOver = true;
		}
  }

  public right() {
		let newX = this.playerX + 1;
		if (this.walkableTiles.indexOf(this.tiles[newX].emoji) != -1) {
      this.playerX = newX;
      if (this.tiles[this.playerX].emoji == '🏁') this.gameOver = true;
		}
  }

	public jump() {
		if (this.tiles[this.playerX].emoji == '⬆️') {
      this.tiles[this.playerX] = { index: this.playerX, emoji: '⬇️' };
      for (let i=0; i<this.tiles.length; i++) {
        if (this.tiles[i].emoji == '🌊') this.tiles[i].emoji = '🌉';
      }
		}
  }
}

