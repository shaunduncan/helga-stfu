import random
import re

from twisted.internet import reactor

from helga.plugins import command, preprocessor


silence_acks = (
    u'silence is golden',
    u'shutting up',
    u'biting my tongue',
    u'fine, whatever',
)

unsilence_acks = (
    u'speaking once again',
    u'did you miss me?',
    u'FINALLY',
    u'thanks {nick}, i was getting bored'
)

snarks = (
    u'why would you want to do that {nick}?',
    u'do you really despise me that much {nick}?',
    u'whatever i do what i want',
    u'no can do, i love the sound of my own voice',
)

# Set of silenced channels
silenced = set()


def auto_unsilence(client, channel, length):
    global silenced

    if channel in silenced:
        silenced.discard(channel)
        client.msg(channel, u"Speaking again after waiting {0} minutes".format(length//60))


@preprocessor
@command('stfu', aliases=['speak'],
         help="Tell the bot to be quiet or not. Usage: helga (speak|stfu [for <time_in_minutes>])")
def stfu(client, channel, nick, message, *args):
    global silenced

    # Handle the message preprocesor
    if len(args) == 0:
        # Duh, don't silence the speak command
        is_speak = bool(re.findall(ur'^{0}\W*\s(speak)$'.format(client.nickname), message))

        if channel in silenced and not is_speak:
            message = u''

        return channel, nick, message

    elif len(args) == 2:
        resp = u''

        if channel == nick:  # Private message
            resp = random.choice(snarks)
        elif args[0] == 'stfu':
            silenced.add(channel)
            cmdargs = args[1]
            resp = random.choice(silence_acks)

            if len(cmdargs) > 0 and cmdargs[0] == 'for':
                try:
                    length = int(cmdargs[1]) * 60
                except (TypeError, ValueError, IndexError):
                    pass
                else:
                    reactor.callLater(length, auto_unsilence, client, channel, length)
                    resp = u"OK {0}, I'll be back in {1} min".format(nick, cmdargs[1])
        elif args[0] == 'speak':
            if channel not in silenced:
                return None

            resp = random.choice(unsilence_acks)
            silenced.discard(channel)

        return resp.format(nick=nick)
