helga-stfu
==========

A helga command and preprocessor to prevent any plugins from processing messages. This is useful if the bot
is being noisy on a channel and you wish to silence it. Usage::

    helga (stfu [for <minutes>]|speak)

Without any arguments, ``stfu`` will silence helga indefinitely. Otherwise, you can specify a number
of minutes for helga to be silent::

    <sduncan> !stfu for 5
    <helga> Ok I'll be back in 5 minutes

If the bot is currently silenced, you can unsilence it::

    <sduncan> !speak
    <helga> speaking again


License
-------

Copyright (c) 2015 Shaun Duncan

Licensed under an `MIT`_ license.

.. _`MIT`: https://github.com/shaunduncan/helga-stfu/blob/master/LICENSE
