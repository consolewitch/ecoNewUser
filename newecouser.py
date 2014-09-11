"""
This code hacked together by Alex Speaks : @logicalmethods : alex@sneaksneak.org
It's my first python script.. be gentle.

new user creation script for Ecotrust
-------------------------------------

does:
*creates users in AD 

to do:
* read CSV of user names and attributes
* add ad user to appropriate groups
* create social cast user
* create mediawiki user
* create resource space user
* create basecamp user?
* create user in GLPI
* assign user to computer in GLPI
* option : create mailbox?
* option : create linux dev boxen user?
"""


from pyad import *	#for interacting with AD
import json			#for reading and writing json
import urllib2		#for parsing URLs
#from httplib2 import Http

def readWorkFile(fileName): #opens the to-do file and returns a json object of the things we should be doing
	f = open(fileName, "r")
	work = json.load(f)
	return(work)


def mkAD(username):
	ou = pyad.adcontainer.ADContainer.from_dn("OU=folder redirection,OU=employees,OU=ecotrust,DC=ecotrust,DC=org")
	c = pyad.aduser.ADUser.create(name = username, container_object=ou, password=pwgen(), upn_suffix=None, enable=False, optional_attributes=dict(description = "new user"))
	addToGrp("everybody", username)
	return(c.displayName)

def addToGrp(groupName, userName):


# returns a 10 character human readable password
def pwgen():
	return("Password!")

"""
def mkBasecamp()


def mkSocialcast(userName):
	httpCall = Http()
	data = dict(name="Joe", comment="A test comment")
	resp, content = h.request("http://bitworking.org/news/223/Meet-Ares", "POST", urlencode(data))
	resp
"""

print mkAD("aaron")