Icecast tracker
===============

Core
----

As reported in [this
post](https://www.fladi.at/posts/load-balancing-icecast-relays/), it
is a good idea to dispose of a HTTP server which is able to redirect
(using the 'HTTP 302' code reply) to a Icecast server, depending on
the stream and the load of the servers that are transmitting that
stream. Some useful rules that could be followed in order to assign
the most suitable server are:

1. Use a GeoIP datababse such as
   [this](http://dev.maxmind.com/geoip/legacy/downloadable/) to
   determine the closest Icecast server (of the client, of course).

2. Use the 'ping' utility to estimate the load of the link from the tracker to
   the servers. Higher RTT times are correlated with high bandwidth loads.

3. Use the information returned by the servers (specifically, in the file
   'status2.xsl') with information about the number of current connections.

This idea has been implemented
[here](https://pypi.python.org/pypi/django-icecast-balancer/0.1.4) and
[here](https://code.google.com/p/django-icecast-balancer/), but in
this case the load balancer (our tracker) does not use the information
provided by the servers in real time (as our tracker should do). In
other words, while the 'django-icecast-balancer' polls periodically
all the servers in order to estimate the most suitable server when a
client requests it, our 'Icecast tracker' should perform this task
when the request has been received. Obviously, our alternative will
have a higher latency than the previous developed one, but the results
should be more accurate.

Implementation insights
-----------------------

In order to write a HTTP server we have basically two options:

1. Re-invent the wheel, writting the server from scrach. This gives us
   the possibility of using whatever programming language we like, but
   the cost (in terms of time) of this action could be unaffordable.

2. Use some *facility* such as
   [django](https://www.djangoproject.com/start/overview/),
   [Node.js](https://nodejs.org/en/) or [Ruby on
   Rails](http://rubyonrails.org/). In this case our choices are
   smaller than in the previous option but we will build a good HTTP
   server in much less time.

