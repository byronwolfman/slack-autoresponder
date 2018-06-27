#!/usr/bin/env python

import os
from slackclient import SlackClient
import time

# Globally important
cooldown = 28800  # 28800 seconds = 8 hours
last_message_from = {}
slack_token = os.environ["SLACK_TOKEN"]

autoresponder_message = "Your polite message goes here"

# Execution starts here
client = SlackClient(slack_token)
if client.rtm_connect(auto_reconnect=True):
    myself = client.api_call("auth.test")["user_id"]

    while client.server.connected is True:
        events = client.rtm_read()

        # Process events from rtm; event format is an array of events
        for event in events:
            event_type = event.get("type")

            # Handle messages
            if event_type == "message":
                msg_sender = event.get("user")
                msg_channel = event.get("channel", "N/A")

                # Ignore messages from ourselves
                if msg_sender == myself:
                    continue

                # Message is a DM if the "channel" begins with D
                try:
                    if msg_channel[0] == "D" and msg_sender is not None:
                        now = int(time.time())
                        time_of_last_message_from_sender = \
                            last_message_from.get(msg_sender, 0)

                        # Send a polite reminder that we're not here if it's
                        # been $cooldown seconds since the last one
                        if now - time_of_last_message_from_sender > cooldown:
                            client.api_call("chat.postMessage",
                                            as_user=True,
                                            channel=msg_channel,
                                            text=autoresponder_message)
                            last_message_from[msg_sender] = now
                except:
                    pass

                # Sleep a bit so we don't DoS Slack
                time.sleep(2)
else:
    print ":("
