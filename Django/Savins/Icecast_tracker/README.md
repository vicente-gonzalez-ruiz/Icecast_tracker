#Introduction
This project is a Icecast load-balancer. When a user wants to watch a channel, the server searches in the database the server less loaded in real time (getting status2.xsl) and it sent the url to the user.

#Adding new channel
Users can add their servers very easily with the database webclient of Django.

![Login](https://github.com/Sistemas-Multimedia/Icecast-tracker/blob/master/Django/Savins/public/images/admin.png)

![Dashboard](https://github.com/Sistemas-Multimedia/Icecast-tracker/blob/master/Django/Savins/public/images/adminDashboard.png)

#How to work

The main page of the application would be:
![Channel list](https://github.com/Sistemas-Multimedia/Icecast-tracker/blob/master/Django/Savins/public/images/channelList.png)

And when clicking on the video link would be.
![Playing the video](https://github.com/Sistemas-Multimedia/Icecast-tracker/blob/master/Django/Savins/public/images/streaming.png)

Copying the URL in VLC could play the video in the player.
![Configure the VLC](https://github.com/Sistemas-Multimedia/Icecast-tracker/blob/master/Django/Savins/public/images/configureVLC.png)
![Playing channel in VLC](https://github.com/Sistemas-Multimedia/Icecast-tracker/blob/master/Django/Savins/public/images/playingVLC.png)
