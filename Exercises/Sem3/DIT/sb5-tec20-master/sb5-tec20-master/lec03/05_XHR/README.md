AJAX requests with XMLHttpRequest (XHR)
---------------------------------------

This directory contains two examples of an asynchronous
request: to a local webserver on localhost and to a remote host.

To run [example-localhost.html](example-localhost.html)
start an Nginx webserver inside docker with
```
 $ docker-compose up
```
from *this* directory.

Then access http://localhost:8080/example-localhost.html in a browser
