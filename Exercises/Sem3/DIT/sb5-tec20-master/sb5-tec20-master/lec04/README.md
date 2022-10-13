Exercise: Retry
---------------

Solve the exercise "Retry" from chapter 8 in Eloquent JavaScript: https://eloquentjavascript.net/08_error.html#i_n1zYouiAfX


Exercise: Make it sluggish
--------------------------

Consider the program in [exercise01-slow.html](exercise01-slow.html)

It contains a handler counting and displaying a text-input's length.

Now, be a bad person:
- Change the handler to make the page feel slow.
- Can you make typing almost unbearable?


Exercise: Help the lecturer!
----------------------------

Jan is stuck on the IC-train with bad Wifi.

Print him an error message using the
promise returned by the function `networkStatus`:

```javascript
 function networkStatus() {
   if (Math.random()<0.3) {
      return Promise.reject("Dang, DSB Wifi is down");
    } else {
      return Promise.resolve("Yay, facebook here we come");
    }
 }
 ```

You can use the skeleton in [exercise02-badwifi.html](exercise02-badwifi.html).


Exercise: `await`
-----------------

The code in [exercise03-async.html](exercise03-async.html)
contains an `async roll` function for dice throwing:

```javascript
  async function roll() {
      await new Promise(r => setTimeout(r, 500));
      return 1+Math.floor(6*Math.random());
  }
```

Complete the `rollPair` function by calling `roll` twice
and returning the result as an object or string:
```javascript
  async function rollPair() {
    //TODO
  }
```

Note: `await` is only allowed in `async` functions.


Exercise: REST
--------------

Consider the code in [exercise04-rest.html](exercise04-rest.html)

It uses the REST API from https://jsonplaceholder.typicode.com/users
to build a table and fetch a user.

Complete the code to 
- update a user entry with PUT
- delete a user entry with DELETE

Caveat: https://jsonplaceholder.typicode.com
will return status codes but not actually perform the server changes.

Bonus exercise for the brave: rewrite the code to use `async` and `await` instead.
