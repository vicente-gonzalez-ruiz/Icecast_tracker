Manual
======

	# 1. Install "pip"
	sudo easy_install pip			# Provided by Python

	# 2. Install "virtualenv"
	sudo pip install virtualenv

	# 3. Create a new (user's) python environment for using Fask 
	virtualenv venv
	
	# 4. Acrivate the environment
	. venv/bin/activate
	
	# 5. Install Flask:
	pip install Flask
	
	# 6. Install queuelib (provides "queue")
	pip install queuelib

	# 7. Run the tracker (the environment must be activated)
	python3 tracker.py

	# 8. Run the player
	firefox localhost:5001/BBB-134.ogv
	vlc http://localhost:5001/BBB-134.ogv
