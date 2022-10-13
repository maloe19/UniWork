Exercise: Help the football fans
--------------------------------

[football-server.js](football-server.js) contains a simple console program for registering live football results. It also serves the live score as JSON using HTTP requests.  
[football-client.html](football-client.html) is a corresponding client that displays the current score (standings), but required page reloading.

- Confirm you can start the server `node football-server.js` and get a response from it
- Open the client in a browser and reload the page as you register a goal on the server
- Help the football fans! Change the client to poll the server, e.g., every 5 seconds and display the live score


Exercise: Improve the chat
--------------------------

In the simple chat in [06-chat-server.js](06-chat-server.js) and [06-chat-client.html](06-chat-client.html) the WebSocket communicates a chat message like this:
```
    Client1:                     Server:                    Client2:
       |                            |                          |
       |            "hej"           |                          |
       |      ---------------->     |                          |
       |                            |                          |
       |                            |                          |
       |   {time: 123, msg: "hej"}  |  {time: 123, msg: "hej"} |
       |      <---------------      |     -------------->      |
       |                            |                          |
```

  Improve the chat by including and displaying a chat name `userid`
  along with each message:
```
    Client1:                       Server:                        Client2:
       |                              |                              |
       | {userid: "finn", msg: "hej"} |                              |
       |      ---------------->       |                              |
       |                              |                              |
       |                              |                              |
       | {time: 123,                  | {time: 123,                  |
       |  userid: "finn", msg: "hej"} |  userid: "finn", msg: "hej"} |
       |      <---------------        |        -------------->       |
       |                              |                              |
```



  There's a skeleton available in files
  [07-better-chat-client.html](07-better-chat-client.html)
  and
  [07-better-chat-server.js](07-better-chat-server.js)


Exercise: Install and run Angular
---------------------------------

 - Install Angular with `npm install -g @angular/cli`
 - Create a new Angular application with `ng new CarDB`  
   (just say `N` to routing and stick to CSS styling)
 - Start the application with `ng serve`
 - Check that you can access the served page at http://localhost:4200
 - Change `src/app/app.component.html` (add/remove HTML
    elements) while `ng serve` is running and check whether the
    changes appear


Exercise: CarList and `*ngFor`
------------------------------

 - Generate a new `CarList` component for your app with `ng generate component CarList`
   (be careful with upper-case/lower-case letters: we recommend CamelCasing to avoid problems)
 - Add its tag `<app-car-list></app-car-list>` to the root
   template in `app/app.component.html` and check that it is rendered.
 - Now add an array property `carArray` to your
   component in `app/car-list/car-list.component.ts`
 - Iterate over the `carArray` in the template with `*ngFor`
   (either inline or in `app/car-list/car-list.component.html`)


Exercise: Extend the game
-------------------------

 - Run `npm install` and `ng serve` in [EmojiGame](EmojiGame) and check that you can run the game

 - Extend the game, so that jumping on a `⬇️` removes the bridge (`🌉🌉🌉🌉🌉🌉🌉🌉`)  
   and exposes the water again (`🌊🌊🌊🌊🌊🌊🌊🌊`)

 - Then: change the water so that if you touch it the game is over.
 
 - Harder: Change the game to a level like
   ```
    ⛔️ ➖ 🏁 ➖ ➖ 🌞 ➖ 🤓 ➖ ➖ ➖ ⬆️ ➖ ➖ 🌊 🌊 🌊 🌊 ➖ ➖ ➖ 🕶 ➖ ⛔️
   ```
   where `🕶` are sunglasses you must put on in order to pass through `🌞` (the sun).
   
   So `🤓` has to go to `🕶`.  
   Passing over the `🕶` the `🤓` changes into a `😎` (person carrying sunglasses) and
   the `🕶` disappears and turns into `➖`.  
   Then the player is able to pass through the sun (which is otherwise not a walkable tile).
