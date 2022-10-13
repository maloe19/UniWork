Exercise: Installing Node.js
----------------------------

Install Node.js from https://nodejs.org

Start the top-level and confirm that you can evaluate JS:
```javascript
  $ node
  > 2+2
  4
  > let x = 2
  undefined
  > x+x
  4
```

Write a js-file `test.js` containing, e.g.:
```javascript
  console.log("Hello, world!");
```
and confirm that you can run it with `node test.js`


Exercise: Reacting to requests
------------------------------

Make a Node web-server that responds to

 - GET requests to url `"/"` with status code
    `200 (OK)` and some text or html string
 - other HTTP method requests (PUT, POST, DELETE, ...)
    with `405 (Method not allowed)`
 - other URLs, e.g., `"/path/resource"` with `404 (Not found)`


Exercise: Make the server sluggish
----------------------------------

Consider the basic server in [03-hello-server.js](03-hello-server.js)

It contains a call-back handler responding to HTTP requests.

Now, be a bad person:
- Change the handler to make the server feel slow.
- Can you make HTTP communication almost unbearable?


Exercise: CORS
--------------

If you try a `fetch("http://localhost:8080/users/0")`
 - to our local JSON node server in [08-json-server.js](08-json-server.js)
 - from Chrome's JavaScript console (or from a client-side script)
you get a CORS failure.

First: Confirm that this is the case.

Next: Patch the server, by setting the CORS header.

Note: Depending on whether your request requires a preflight request,
you may also have to return the header
```
 'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS'
```

Exercise: CommonJS and ECMAScript Modules
-----------------------------------------

Extend the CommonJS module in [13-commonjs-modules](13-commonjs-modules) with an extra function:
```
 reset()
```
that sets the `innerState` to `undefined`. Check that your implementation works as intended. 

Similarly extend the ECMAScript module in [14-es-modules](14-es-modules) with `reset()`.


Exercise: Vectors in TypeScript
-------------------------------

Revise the exercise ``A vector type''
from https://eloquentjavascript.net/06_object.html#i_zO8FRQBMAy
but now in TypeScript
  
(You can annotate your old JS solution with types)

Now:
- install the TypeScript compiler
  ```
   npm install -g typescript
   ```
- compile your TypeScript code to JS:
  ```
   tsc filename.ts
  ```
- compare the output JavaScript code to your original JS version
