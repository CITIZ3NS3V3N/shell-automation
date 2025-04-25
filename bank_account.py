import requests
from torpy import TorClient
from randomuser import RandomUser
import os

user = RandomUser()
with TorClient() as tor:
    session = tor.create_session()
    response = session.get("https://www.cayebank.bz/open-an-account")
    # Generate fake ID
    fake_id = session.post("https://idmaker.pw/generate", data={"name": user.get_full_name()}).json()
    session.post("https://www.cayebank.bz/submit-kyc", files={"id": fake_id})

# Setup Monero wallet
os.system("cakewallet --generate-wallet --currency xmr")
# Simulate crypto transfer
kraken = requests.post("https://api.kraken.com/0/public/sandbox", json={"pair": "XMRUSD"}).json()