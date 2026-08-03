so in this we would be talking about the Ordering 
1)in the oedering we could receive the output in ascending or descending order depending upon the url is there or not in this the get/products/?ordering=name
2)this would absolutely give the sequence in ascending orderig and if i want the descending order then it would be like get / products/?ordering=-name
3) so in thsi we would be talking about this flow 
| Feature   | Where should it happen? |
| --------- | ----------------------- |
| Filtering | Database                |
| Ordering  | Database                |
| Searching | Database                |

4) in this we would alos be looking at the  AUTHENTICATION
-- ----------------------------------------------------------------------------------------------
5) as when we login from the instagram for example it store the login information in the place so in this we could get like if the login next time so the login information in the form of jwt -- jason web token or a session id   or a token is being given to that user 
 so this is how it would be working 
 Login

↓

Username + Password

↓

Authentication

↓

Session Created

↓

Session ID

↓

Browser Cookie

↓

Future Requests

↓

Cookie Sent

↓

Server Checks Session

↓

User Identified

↓

Permission Check

↓

APIView

↓

ORM

↓

Database

6)so the thing is that i would be the seesion is being stored in the server itself and also in the session id 

so server is being used to store the information about the session id and the browser send the sessionid cookie with every request 

so each and every diffrent browser has its own cookie setting which it uses to store the cookie information 

so the thing is 
Chrome Login
        │
        ▼
Username + Password
        │
        ▼
Authentication
        │
        ▼
Session ID = ABC123
        │
        ▼
Cookie Stored in Chrome


Edge Login
        │
        ▼
Username + Password
        │
        ▼
Authentication
        │
        ▼
Session ID = XYZ789
        │
        ▼
Cookie Stored in Edge

-- so the problem with cookies is that it is not being used nowadays cause it had several drawback one of them being that when the frontend and backend are not on same domain then the errors like these show up Cross-Origin (CORS)
Cookie configuration
SameSite policies
CSRF protection
Credentials handling
-- so we introduced instead of that JWT - json web token in this the useful information is being stored in that 
| Session                              | Token               | JWT                                 |
| ------------------------------------ | ------------------- | ----------------------------------- |
| Server stores session                | Server stores token | No server session needed            |
| Browser stores Session ID cookie     | Client stores token | Client stores JWT                   |
| Best for traditional Django websites | Good for APIs       | Best for modern React + Django apps |

-- the question is where is the jwt stored the jwt is being stored in the react browser itself it is being stored as a result not in the database this is how the flow works 
User Login
      │
      ▼
React
      │
Username + Password
      ▼
Django
      │
Authentication
      ▼
JWT Generated
      │
      ▼
React Stores JWT
      │
Future Requests
      ▼
Authorization: Bearer <JWT>
      │
      ▼
Django

so this is how it stores it really 
React stores it on the client (commonly local storage, session storage, or another secure client-side storage strategy depending on the application).

so here is how it is working 
| Method  | Client Stores | Server Stores              |
| ------- | ------------- | -------------------------- |
| Session | Session ID    | Session                    |
| Token   | Token         | Token                      |
| JWT     | JWT           | Secret Key (to verify JWT) |

-- so the thing with jwt is that if it is being accessed by someone else account then they would be accessing the data and there is no privacy like if someone else get your jwt token they can access your profile and as a result   