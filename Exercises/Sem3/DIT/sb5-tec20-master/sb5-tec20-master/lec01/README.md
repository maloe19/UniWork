Exercise: a local webserver
---------------------------

- Install Docker https://docs.docker.com/get-docker/

- Start a nginx web server in Docker container. In this folder just run:

  ```
    docker-compose up
  ```

- Open a browser and visit your local webserver on

  >   http://localhost:8080/

  The port 8080 is specified in `docker-compose.yml`

- The webserver serves files from the current directory.

  Put a few other files in here (a small image, a text file, ...)
  + confirm that you can load them from your browser.



Exercise: a manual request with telnet
--------------------------------------

- Enable/install the `telnet` client on your machine.

  >    Win10: https://www.technipages.com/windows-10-enable-telnet
      
  >    Mac+Linux: already installed?


- Write an HTTP GET request by hand:

  ```
   $ telnet
   ...
   > open localhost 8080
   ...
   GET /index.html HTTP/1.1
   Host: localhost:8080
   (press return twice for an extra blank line)
  ```

  (You can also omit the `open`-line if you simply run `telnet localhost 8080`)   

  Do you get a `200 OK` response? Why/why not?

- Can you request the small image from earlier?

- Windows users: the telnet on Windows is slightly broken.

  * If the screen is not clearing so you overwrite any previous
    characters, this is a known issue:

     > https://learningpassion.wordpress.com/2013/11/10/http-request-via-telnet/

  * If you cannot see what you are typing, an escape code
    (`Ctrl + ]`) followed by `set localecho` and `Enter` may fix it as
    explained here:

     > https://stackoverflow.com/questions/1098503/how-to-unsupress-local-echo
  
  * If you are not allowed to enter the HTTP request, you might
    not be in echo mode.
    In order to enter echo mode: 
    From the C:\> command prompt type telnet localhost 8080 then enter
    Then press the escape character, and you will see the Microsoft Telnet> prompt, and press enter again to get into echo mode. 
    Now you can type in GET / HTTP/1.1 or multiple lines (get and headers). Press ctrl-enter when you have finished, or press enter on a blank line

    It is explained in an answer by robocat here:

     > https://serverfault.com/questions/493313/telnet-doesnt-accept-enter-as-a-newline


Exercise: make HTTP requests with `curl`
----------------------------------------

`telnet` can be easy for checking basic connectivity.

For a more powerful tool, `curl` is a good option.


- Install the `curl` program on your machine
    (again: it may already be installed)

- Run `curl` from the command line to request pages from your webserver:

  ```
    $ curl -v localhost:8080/file.html
  ```

  (The `-v` option -- for verbose -- prints both
  the underlying request and response headers)

- Study the headers. How much do they reveal?

- Make a `curl` request to https://icanhazdadjoke.com/ with the HTTP
  request header `Accept: text/plain` to tell the server that you
  would like a plain text response.

  Compare the response to what you get when sending the header
  `Accept: text/html`.

- Make `curl` perform an HTTP HEAD request   
  (this asks the server to only send response headers - but no data).



Exercise: VS Code and HTML
--------------------------

- Install the VS Code editor  https://code.visualstudio.com/download
  and the Live Server extension  https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer 

- Write an HTML file in VS Code including the elements from the slides   

  Can you get the Live Server working like in this video? https://www.youtube.com/watch?v=T0SInJ7Eo8M


- Save the HTML file in this directory so that the nginx web server serves it.

- Check that you can view your page from your browser
