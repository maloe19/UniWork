Exercise: Looping a trangle
---------------------------

Solve the first exercise "Looping a trangle"
here: https://eloquentjavascript.net/02_program_structure.html#i_umoXp9u0e7



Exercise: Parametric triangles
------------------------------

Extend your triangle code to a `triangle`-function
that expects a size parameter.


For example, the call `triangle(5)` should give the following output in the console:
```
     #
     ##
     ###
     ####
     #####
```

Bonus: extend the `triangle` function with an optional "character parameter"
such that `triangle(3,"%")` prints the triangles with `%` instead.



Exercise: The sum of a range
----------------------------

Solve the first exercise "The sum of a range"
here: https://eloquentjavascript.net/04_data.html#i_8ZspxiCEC/



Exercise: Show objects
--------------------------

Look at [02_DOM/showObjects.html](02_DOM/showObjects.html)
  
The JavaScript in the page declares an array of objects (representing cars).

You should write a `DIV` in the DOM for each element of
the array. The resulting page should show producer and model name
for each car, using one `SPAN` for each property of a car object.


Hint: You can iterate over your array and use `innerHTML` to add the
HTML elements.



Exercise: CarPage
-----------------

Create a "car database page" which is able to
 - add a new car by typing producer and model name.  
   Use a form with some buttons to do that.
 - refresh the list of existing cars (eventually after you have 
   added a car). Make a button for that. (Remember to remove the old
    list before you create a new one.)
 - show some statistics (e.g., count) in a `DIV` somewhere on the page


The car data should be stored in an array of objects and be visible
to your functions.


There's a skeleton file here to get you started: [03_GUI/carPage.html](03_GUI/carPage.html)
