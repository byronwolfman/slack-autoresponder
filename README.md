# Slack Autoresponder

A quick and dirty out-of-office autoresponder for Slack. For everyone who has had the "Slack isn't e-mail, but..." conversation.

# Setup

Optionally set a different away message in responder.py.

You'll need a [Slack Legacy Token](https://api.slack.com/custom-integrations/legacy-tokens).

Build the container:

    docker build -t slack-autoresponder:latest .

Run the container:

    docker run \
      -e SLACK_TOKEN=$YOUR_LEGACY_TOKEN \
      --restart=always \
      --name autoresponder \
      -d slack-autoresponder:latest

# Caveats

It's a quick and dirty python script with hardly any error handling. Probably don't commit your legacy token to any repos. Be aware of what you leave behind in your bash history. Definitely run at your own risk.
