""" fauxmo_minimal.py - Fabricate.IO

    This is a demo python file showing what can be done with the debounce_handler.
    The handler prints True when you say "Alexa, device on" and False when you say
    "Alexa, device off".

    If you have two or more Echos, it only handles the one that hears you more clearly.
    You can have an Echo per room and not worry about your handlers triggering for
    those other rooms.

    The IP of the triggering Echo is also passed into the act() function, so you can
    do different things based on which Echo triggered the handler.
"""

import fauxmo
import logging
import time
import gpio_handler
import outlet_handler
import time

from debounce_handler import debounce_handler

logging.basicConfig(level=logging.DEBUG)

o_handler = outlet_handler.OutletHandler()

class device_handler(debounce_handler):
    """Publishes the on/off state requested,
       and the IP address of the Echo making the request.
    """
    TRIGGERS = {"gooseberg": 52000,
                "two": 52001,
                "the fan": 52003,
                "christmas": 52004,
                #"flash": 52002,
                "circle": 52005}



    def act(self, client_address, state, name):
        #print name
        #print "State", state, "on ", name, "from client @", client_address
        if name == "gooseberg":
                if state:
                   o_handler.turn_on(1)
                else:
                   o_handler.turn_off(1)

        elif name == "two":
            if state:
                o_handler.turn_on(2)
            else:
                o_handler.turn_off(2)

        elif name == "the fan":
            if state:
                o_handler.turn_on(4)
            else:
                o_handler.turn_off(4)

        elif name == "christmas":
            if state:
                o_handler.turn_on(5)
            else:
                o_handler.turn_off(5)

        elif name == "circle":

            for i in range(4):
                o_handler.turn_on(1)
                time.sleep(.1)
                o_handler.turn_off(1)
                time.sleep(.05)
                o_handler.turn_on(2)
                time.sleep(.1)
                o_handler.turn_off(2)
                time.sleep(.05)
                o_handler.turn_on(4)
                time.sleep(.1)
                o_handler.turn_off(4)
                time.sleep(.05)



        return True



if __name__ == "__main__":
    # Startup the fauxmo server
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    u.init_socket()
    p.add(u)

    # Register the device callback as a fauxmo handler
    d = device_handler()
    for trig, port in d.TRIGGERS.items():
        fauxmo.fauxmo(trig, u, p, None, port, d)

    # Loop and poll for incoming Echo requests
    logging.debug("Entering fauxmo polling loop")
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
            p.poll(100)
            time.sleep(0.1)
        except Exception, e:
            logging.critical("Critical exception: " + str(e))
            break
