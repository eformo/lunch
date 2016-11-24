#!/usr/bin/python
import random,sys,os

if __name__ == "__main__":

	mail_list = open('list.in','r').readlines()

	order_organizer = random.choice(mail_list)
	mail_list.remove(order_organizer)
	order_caller = random.choice(mail_list)

	organizer_text = "Good morning %s, you are the chosen food order organizer. " \
				"Please do what you must to provide a document to %s to call in and order" \
				% (order_organizer.split(' ')[0], order_caller.split(' ')[0])
	print organizer_text

	order_text = "Good morning %s, you are the chosen food order caller. " \
			"Please wait for a document from %s to call in and order" \
			% (order_caller.split(' ')[0], order_organizer.split(' ')[0])
	print order_text

	cmd = """echo "%s"|timeout 10m mutt -e 'set realname=\'Lunch_Boss\'' -a lunch.jpg -s \'LUNCH TODAY\' -- %s""" % (organizer_text,order_organizer.split(' ')[1])
	print cmd
	#os.system(cmd)
	cmd = """echo "%s"|timeout 10m mutt -e 'set realname=\'Lunch_Boss\'' -a lunch.jpg -s \'LUNCH TODAY\' -- %s""" % (order_text,order_organizer.split(' ')[1])
	print cmd
	#os.system(cmd)

