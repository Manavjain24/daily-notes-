OAUTH2 with password (and hashing), bearer with jwt tokens 
-- jwt -- json web tokens these are the tokens in json form in these the tokens 
are being enerated these are the json lines without spaces in which the tokes are being generated in such a way that they are not encrypted information could be leaked out from them but they are also signed so in this we get the same user that signed it could be used and also the expiration date is fixed 

--hashing -- it means converting a string into a gibbrish or a text which makes no sense 

--password hashing -- in this th epasswords is being hashed in such a way that if u enter that password it would be converted into gibberish but the gibberish would not be converted onto password 
this is the user workflow 
User logs in with username & password.
Server verifies the password (bcrypt/Argon2).
If correct, server creates a JWT token.
Frontend stores the token.
Every protected request sends Bearer <token>.
Server verifies the token.
If valid → allow access; otherwise → return 401 Unauthorized.
