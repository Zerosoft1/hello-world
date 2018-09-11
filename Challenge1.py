#!/usr/bin/env python

def devices():
	routers = ['router1','router2','router3']
	return routers 
	

def security(creds):
	credentials = {x: 'passw0rd1' for x in (devs)}
	return credentials


def combined():
	print devices()
	print security(devs)


if __name__ == "__main__":

	devs = devices()

	print 'The routers are:\n', devices()

	print 'The credentials are:\n', security(devs)

	print 'All data is\n', combined()


#THIS IS CURTIS'S MACHINE


