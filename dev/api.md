# API

An **API**, *Application Programming Interface* is an interface through which different software
applications can communicate with each other. **API** have become a standard: it enables to 
centralize information, thus a single backend with an API can be shared by multiple frontend
applications.

An **API** uses **endpoints**. Each **endpoint** enables a specficic action (sending an email,
authenticating the user, etc.). This is useful because the API's user, the one who "calls" these
endpoints, doesn't have to understand how they work: they just need to know what the endpoint is
and what it does (similarly to using a third party library).

In more concrete terms, an **endpoint** is an URL. Depending on which HTTP method is used to call
it (GET, POST, PATCH, DELETE), soome code will be executed and a **result** will be returned. This
result is made of a *status code* (200, 201, 400, etc.) which indicates whether the call has been
successful or not and a **response**, usually in JSON format (sometimes in XML) which contains 
**data** (either success or error data depending on whether the call was successful).

These calls to the endpoints can also be sent with URL parameters or paramaters in the body request.

```aln
API : Application Programming Interface
```