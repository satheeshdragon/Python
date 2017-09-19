import xmpp
GMAIL_ID = 'satheeshdragon.satheesh@gmail.com'
PASS = 'satheeshprogrammer' # if you have app specific pass, you'll need to generate one for this
jid = xmpp.protocol.JID(GMAIL_ID)
C = xmpp.Client(jid.getDomain(), debug=['always'])
if not C.connect(("talk.google.com",5223)):
    raise IOError('Can not connect')
if not C.auth(jid.getNode(),PASS):
    raise IOError('Can not auth with server')

# use following to get list of contacts
C.sendInitPresence(requestRoster=1)
#rosterobject =  C.getRoster() 
# I used the following loop just to check my contacts, it's not need if you know the ID
#for i in rosterobject.getItems():
#    print i

C.send( xmpp.Message('your.online.buddy@gmail.com', "hello") )