object = 24
if (isinstance(object, int)):
    if (object >= 100):
        print "That's a big number!"
    elif (object < 100):
        print "That's a small number."

if (isinstance(object, str)):
    if (len(object) >= 50):
        print "Long sentence."
    else:
        print "Short sentence."

if (isinstance(object, list)):
    if (len(object) >= 10):
        print "Big list!"
    else:
        print "Small list."
