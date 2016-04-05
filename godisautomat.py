# -*- coding: utf-8 -*-

print "1 choklad 10 kr"
print "2 festis 8 kr"
print "Tryck nummer för onskad vara"

nr = int(raw_input(">>> "))

if nr == 1:
    print "mata in 10 kr"
if nr == 2:
    print "mata in 8 kr"


kr = int(raw_input(">>> "))

if nr == 1 and kr >= 10:
    print "choklad"
    print "Du får tillbaka %s kr." % (kr - 10)

if nr == 2 and kr >= 8:
    print "choklad"
    print "Du får tillbaka %s kr." % (kr - 8)

if nr == 1 and kr < 10:
    print "För lite pengar för din önskad vara"

if nr == 2 and kr < 8:
    print "För lite pengar för din önskad vara"