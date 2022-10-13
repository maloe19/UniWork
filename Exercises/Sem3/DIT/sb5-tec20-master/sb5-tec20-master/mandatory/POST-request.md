Mandatory POST request assignment:
----------------------------------

- Sign up for the assignment by opening the following link in your browser  

  > https://scalableteaching.sdu.dk/assignment/join/b7dd68da-5863-400e-bca9-8f3a4caf3242

  log on and receive a token (example token: `abc123`)


- Recall your SDU username (example username: `finn2020`)

- Now make an HTTP POST request to `tek-cv-jmid-01.stud-srv.sdu.dk/finn2020` on port 8080

  * including the HTTP headers:
    ```
     Authorization: Bearer abc123
     Content-type: text/plain
    ````
    
  * with the body
    ```
    Pretty please?
    ```

  Remember to replace the username and token with your own.

  Note: The host `tek-cv-jmid-01.stud-srv.sdu.dk` is only available on SDU's network.  
  If you plan to make requests from home, you need to [use VPN](https://www.sdu.dk/da/om_sdu/faellesomraadet/sdu_it/services/netvaerksadgang/vpn).

- The request is successful once you receive a 200 OK response

  You can also check your assignment status on https://scalableteaching.sdu.dk under 'Assignments'
