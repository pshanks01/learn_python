#!/bin/python

print "Please enter your shipping address"
addr1 = raw_input("Street address: ")
city = raw_input("City: ")
state = raw_input("State: ")
pcode = raw_input("Postal/Zip code: ")
phone = raw_input("Daytime phone: ")

print """
Confirming address and phone:
Address: %s, %s %s %s
Tel.: %s
""" % (addr1,city,state,pcode,phone)
