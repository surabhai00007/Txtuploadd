import os

API_ID = API_ID = 28328736

API_HASH = os.environ.get("API_HASH", "802254a44896baa87f3083b7af36b2e5")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7836714507:AAE0uMDhthtcFEPoO96xxUxXmeyW6Obz5tU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 2052075731))

LOG = ,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6762899804").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


