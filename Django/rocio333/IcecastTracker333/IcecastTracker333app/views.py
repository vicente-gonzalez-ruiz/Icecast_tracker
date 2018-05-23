from django.shortcuts import render
from models import Channel, Route, Server
import urllib2
#import libxml2
import re

#Gets a list with all the channels
def channel_list(request):
	#Looking for all the channels
	allChannels = Route.objects.order_by('path')
	#DISTINCT ON MANUAL =)
	channels = []
	seen_path = []
	for channel in allChannels:
		if channel.path not in seen_path:
			seen_path.append(channel.path)
			channels.append(channel)

	    #The channels are sended
	return render(request, 'IcecastTracker333app/channel_list.html', {'channels':channels})

#This method select the server that the channel selected is less seen.
def play_channel(request):
#The variables are initialized
	sourcerListening = 1000000000
	finalAddress = ""
	finalPort = 0
	finalPath = ""
	#Regex
	p = re.compile("/")
	p2 = re.compile(",")

	#it gets the path of the source that the user wants to see/listen
	path = request.GET.get('c', '')
	#it gets all the routes that they gets this path
	routes = Route.objects.filter(path=path)
	for route in routes:
		icecastServer = "http://"+route.server.ip+":"+str(route.server.port)
		try:
			if urllib2.urlopen(icecastServer+"/status2.xsl").getcode() == 200:
				# getting the status2.xsl file from the server
				xslString = str(libxml2.parseDoc(urllib2.urlopen(icecastServer+"/status2.xsl").read()).xpathEval('pre')[0])
				# splitting all the channel in the file
				channels = p.split(xslString)
				for channel in channels:
					# We split the information of each channel
					channelInformation = p2.split(channel)
					if len(channelInformation)>4:
						#channelInformation[0] = namePath, channelInformation[3] = sourcesActivesInThisMoment
						if path == channelInformation[0] and sourcerListening > int(channelInformation[3]) :
								sourcerListening = channelInformation[3]
								finalAddress = route.server.ip
								finalPort = route.server.port
								finalPath = route.path
		except Exception as e:
			print "source not found"
	if finalAddress == "":
		return render(request, 'IcecastTracker333app/error_channel.html')
	else:
		url = "http://"+finalAddress + ":" + str(finalPort) +"/"+finalPath
		return render(request, 'IcecastTracker333app/play_channel.html', {'url':url})
		
	
def hello(request):
	nombre = "Roci"
	context = {
		'saludo':'Hello, how are you? From Koding',
		'nombre':nombre
	}
	return render(request, 'IcecastTracker333app/helloWorld.html', context)
		#Looking for all the channels
	