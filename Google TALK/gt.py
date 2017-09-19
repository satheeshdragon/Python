import sys,xmpp

# Google Talk constants

FROM_GMAIL_ID = "satheeshdragon.satheesh@gmail.com"

GMAIL_PASS = "satheeshprogrammer16"

GTALK_SERVER = "talk.google.com"

TO_GMAIL_ID = "16satheeshkumar@gmail.com"

jid=xmpp.protocol.JID(FROM_GMAIL_ID)

cl=xmpp.Client(jid.getDomain(),debug=[])

if not cl.connect((GTALK_SERVER,5222)):

    raise IOError('Can not connect to server.')

if not cl.auth(jid.getNode(),GMAIL_PASS):

    raise IOError('Can not auth with server.')

cl.send( xmpp.Message( "16satheeshkumar@gmail.com" ,"Hi" ) )

cl.disconnect()