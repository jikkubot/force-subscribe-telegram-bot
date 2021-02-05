import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(658905997)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1511657790:AAGft0IIajOMhrg7MIC7-ugQcoPcJaMvZM8"
    DATABASE_URL = "postgres://dstwfnibkctjoo:4898c1502985cf1d346554d35170c1eef4af2fe8ef62d88f8b1fe51acc3f35b8@ec2-52-6-178-202.compute-1.amazonaws.com:5432/dej4l44tb6gf37"
    APP_ID = "2629442"
    API_HASH = "01b1a378f9c961cffcb022dfda679b0b"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(658905997)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @JikkuBarca**"
      ]

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
