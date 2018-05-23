# IcecastTrackerExpress

To launch the tracker, you have to do the next steps

1. Browse to the folder you have app.js

2. Execute npm start. By default, it starts in port 8080

3. To see servers and the files that contains the servers, you have to open a browser with the address

http://yourdomain:8080

4. To use the tracker, you must enter the address http://yourdomain.com:8080/yourvideo.ext. The tracker loop into the files in the servers and choose the server who has less listeners

5. To add, remove or update the icecast servers, you must edit the file routes/index.js. The array that contains the servers is named 'urls'.
