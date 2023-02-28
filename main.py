import telebot
import requests
import json
import pickle
from web3 import Web3
from mnemonic import Mnemonic
from moralis import evm_api
from abi import abiLp
from abi import abiPinksale
import datetime
from telebot import types
from abi import abiPcs

moralis_key = "GFe9A3lNYWFSv1jO5NmC14bUHeW4oedryp1BPUHxAnAMZUL7C3Nd0Ppjaru3003R"
Api_key = "5964876840:AAHe5gbeYg9e1BtPIX2WJauspGbwWd1i1Ao"
infura = "https://mainnet.infura.io/v3/c1f653384020470d942fdd4d8eb97795"
bscApi = "JIW519CDP82K5S9QU9JFN8CPP8TRFSWXT7"
w3 = Web3(Web3.HTTPProvider(infura))
bnb = "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"
bnb = bnb.lower()
usdt = "0x55d398326f99059ff775485246999027b3197955"
usdt = usdt.lower()

w4 = Web3(
  Web3.HTTPProvider(
    "https://sparkling-fluent-flower.bsc.discover.quiknode.pro/0a6645304944afc91f4056ae41b6e666a4c68f87/"
  ))
bot = telebot.TeleBot(Api_key)
ourTokenCa = "0xBdD120C5fc6CD22a9E75148Fd9a81850D9c12C5b"
allowed = []
addy_cache = 'addy.pickle'
file_name = 'cached_array.pickle'
addys_cache = 'addys.pickle'
addyVerified = []
verifiedAddyCache = {}
devid = [795341146]
wallets = []
game = []
mainData = {}
mainDataCache = 'mainData.pickle'
gameCache = 'game.pickle'


def cache_data(data, file_name):
  with open(file_name, 'wb') as f:
    pickle.dump(data, f)


def load_cached_data(file_name):
  try:
    with open(file_name, 'rb') as f:
      return pickle.load(f)
  except FileNotFoundError:
    return None


#cache_data(allowed, file_name)
#cache_data(verifiedAddyCache, addy_cache)
#cache_data(wallets, addys_cache)
cache_data(game, gameCache)
cache_data(mainData, mainDataCache)

def fromPairGetToken(pair):
  api_key = "GFe9A3lNYWFSv1jO5NmC14bUHeW4oedryp1BPUHxAnAMZUL7C3Nd0Ppjaru3003R"
  params = {
    "addresses": [pair],
    "chain": "bsc",
  }

  result = evm_api.token.get_token_metadata(
    api_key=api_key,
    params=params,
  )

  #print(result, pair)
  name = result[0]['name']
  link = f"<a href='https://poocoin.app/tokens/{pair}'>Poocoin</a>"
  buy = f"https://t.me/MaestroSniperBot?start={pair}"
  addy = f"<a href='bscscan.com/token/{pair}'>Contract</a>"
  buyM = f"<a href='{buy}'>Maestro</a>"
  honeypot = f"<a href='https://honeypot.is/?address={pair}'>Honeypot Checker</a>"
  str = f"{name} <pre>{pair}</pre>  \n {buyM}   {link}  {addy}  {honeypot}\n\n"
  return str





@bot.message_handler(commands=['recent'])
def whalecheck(message):
  pancakeswap = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"
  abi = abiPcs
  factory_contract = w4.eth.contract(address=pancakeswap, abi=abi)
  block = w4.eth.block_number
  events = factory_contract.events.PairCreated().createFilter(
    fromBlock=block - 10000, toBlock=block).get_all_entries()[-1:-15:-1]
  str = "<b><u>Latest Tokens Launched On Binance smart chain</u></b>\n\n"
  for event in events:
    a = event.transactionHash.hex()
    api_key = "GFe9A3lNYWFSv1jO5NmC14bUHeW4oedryp1BPUHxAnAMZUL7C3Nd0Ppjaru3003R"
    params = {
      "transaction_hash": a,
      "chain": "bsc",
    }

    result = evm_api.transaction.get_transaction(
      api_key=api_key,
      params=params,
    )

    hex = result['input'][:3]

    #print(hex)
    if hex == "0x6":
      token0_address = event['args']['token0']
      if token0_address.lower() == usdt or token0_address.lower() == bnb:
        print("w")
      else:
        text = fromPairGetToken(token0_address)
        #text = "halooooo"
        str = F"{str} {text}"

  bot.send_message(message.chat.id,
                   f"<b><i>{str}</i></b>",
                   parse_mode="html",
                   disable_web_page_preview=True)

verifiedAddyCache = load_cached_data(addy_cache)
print(verifiedAddyCache)
allowed = load_cached_data(file_name)
wallets = load_cached_data(addys_cache)
print(allowed, wallets)
game = load_cached_data(gameCache)
mainData = load_cached_data(mainDataCache)


@bot.message_handler(commands=['check'])
def checkDev(message):
  global verifiedAddyCache
  global wallets
  text = f"<b><u>List of Address Who Sold</u></b>\n\n"
  if message.chat.id not in devid:
    bot.send_message(
      message.chat.id,
      f"<b><i>This command can only used by dev.\nUse /verify to get verified and get acess to whale chat</i></b>",
      parse_mode="html")
  else:
    addy = verifiedAddyCache.keys()
    for addy in verifiedAddyCache:
      api = ("https://api.bscscan.com/api"
             "?module=account"
             "&action=tokenbalance"
             f"&contractaddress={ourTokenCa}"
             f"&address={addy}"
             "&tag=latest"
             "&apikey=JIW519CDP82K5S9QU9JFN8CPP8TRFSWXT7")
      response = requests.get(api)
      username = verifiedAddyCache[addy]
      datac = response.text
      balance = int(json.loads(datac)['result'])
      balanceR = balance / 10**18
      if balanceR < 9000:
        wallets.remove(addy)
        text = f"{text} {addy}\nUsername:-@{username}\n\n"
    bot.send_message(message.chat.id, f"{text}", parse_mode="html")


@bot.message_handler(commands=["start"])
def start(message):
  bot.send_photo(
    message.chat.id,
    "https://ibb.co/X83hkfn",
    caption=
    f"<i><b>Hey Welcome To Whale 🐋 Chat Bot</b>.\n\nuse /verify to verify you're a whale 🐋 and get acess to the private whale chat\n\nuse /ca to scan a contract and get detailed info</i>",
    parse_mode="html")


def getAddressInfo(masala):
  address = []
  for maja in masala:
    address.append(maja['address'])
  return address


def getFast(addy):
  txs = []
  tx0 = 0
  tx1 = 0
  tx2 = 0
  tx3 = 0
  tx4 = 0
  for ads in addy:
    checksummed_addr = Web3.toChecksumAddress(ads)
    tx_count = w4.eth.get_transaction_count(checksummed_addr)
    txs.append(tx_count)
  for tx in txs:
    if tx > 0 and tx < 4:
      tx0 = tx0 + 1
    if tx > 0 and tx < 6:
      tx1 = tx1 + 1
    if tx > 0 and tx < 11:
      tx2 = tx2 + 1
    if tx > 0 and tx < 21:
      tx3 = tx3 + 1
    if tx > 0 and tx < 50:
      tx4 = tx4 + 1

  n = len(addy)
  subarrays = []
  allArray = []
  count = 0
  count2 = 0
  count3 = 0
  count4 = 0
  count5 = 0
  count6 = 0
  for i in range(0, n, 19):
    subarray_start = i
    subarray_end = min(i + 19, n)
    subarray = addy[subarray_start:subarray_end]
    subarrays.append(subarray)
  #print(subarrays)
  for array in subarrays:
    #print(array)
    url = "https://api.bscscan.com/api"
    params = {
      "module": "account",
      "action": "balancemulti",
      "address": ",".join(array),
      "tag": "latest",
      "apikey": bscApi
    }
    response = requests.get(url, params=params)
    data = response.json()['result']
    allArray.extend(data)
  for acc in allArray:
    balance = float(acc['balance']) / 10**18
    if balance <= .1:
      count = count + 1
    elif balance <= .5:
      count2 = count2 + 1
    elif balance <= 1:
      count3 = count3 + 1
    elif balance <= 5:
      count4 = count4 + 1
    elif balance <= 10:
      count5 = count5 + 1
    elif balance > 10:
      count6 = count6 + 1
  return [
    count, count2, count3, count4, count5, count6, tx0, tx1, tx2, tx3, tx4
  ]


@bot.message_handler(commands=['ca'])
def caChecker(message):
  if message.text.split(" ")[1].startswith("0x"):
    ca = message.text.split(" ")[1]
    chainName = "bsc-mainnet"
    try:
      url = f"https://api.covalenthq.com/v1/{chainName}/tokens/{ca}/token_holders/?key=ckey_a4afa01c9791458a9a222c44612"
      res = requests.get(url)
      data = res.text
      realD = json.loads(data)
      masala = realD['data']['items']
      #print(masala[0])
      decimal = int(masala[0]['contract_decimals'])
      name = masala[0]['contract_name']
      symbol = masala[0]['contract_ticker_symbol']
      supply = int(masala[0]['total_supply']) / 10**decimal
      #topBuyer = round(topBuyer,3)
      addy = getAddressInfo(masala)
      poocoin = f"<a href='https://poocoin.app/tokens/{ca}'>Poocoin</a>"
      maestro = f"<a href='https://t.me/MaestroSniperBot/?start={ca}'>Maestro</a>"
      contract = f"<a href='https://bscscan.com/token/{ca}'>Contract</a>"
      honeypot = f"<a href='https://honeypot.is/?address={ca}'>Hp Checker</a>"
      info = getFast(addy)
      print(info[8], len(addy))
      freshper = (info[8] / len(addy)) * 100
      freshper = round(freshper, 2)
      infoFormat = f"0-30$: {info[0]}          30$-150$: {info[1]}\n150$-300$: {info[2]}       300$-1500$: {info[3]}\n1500$-3000$: {info[4]}       3000$ and more: {info[5]}"

    except:
      bot.send_message(
        message.chat.id,
        f"<b><i>Please Enter A Valid Binance Smart Chain Address</i></b>",
        parse_mode="html")

    bot.send_message(
      message.chat.id,
      f"<b><i><u>Basic Info</u>\n\nName:- {name}\nSymbol:-{symbol}\nTotalSupply:- <pre>{supply}</pre>\nContract:- <pre>{ca}</pre>\n\n<u>Wallets Balances Analysis 👀🔍</u>\n\n{infoFormat}\n\n<u>Fresh Wallets Analysis 👁🔍</u>\n\nFresh wallets percentage:- {freshper}%\nLess than 50 transactions:- {info[10]}\nLess Than 20 transactions:-{info[9]}\nLess Than 10 transactions:- {info[8]}\nLess Than 5 transactions:- {info[7]}\nOnly holds this token:- {info[6]}\n\n<u>Important Links</u>\n\n{poocoin}                 {maestro} \n{contract}                 {honeypot}</i></b>",
      parse_mode="html",
      disable_web_page_preview=True)


def time_diff_to_dhm(timestamp):
  """
    Calculates the time difference between the current time and a timestamp, and returns the result in days, hours, and minutes format.
    """
  # Get current time in Unix format
  current_time = datetime.datetime.now().timestamp()

  # Calculate time difference in seconds
  diff_seconds = int(current_time - timestamp)

  # Calculate number of days, hours, and minutes
  days, remaining_seconds = divmod(diff_seconds, 86400)
  hours, remaining_seconds = divmod(remaining_seconds, 3600)
  minutes, remaining_seconds = divmod(remaining_seconds, 60)

  # Return formatted string
  return f"{days} days, {hours} hours, {minutes} minutes"


@bot.message_handler(commands=["verify"])
def verify(message):
  if message.chat.id in allowed:
    bot.send_animation(
      message.chat.id,
      animation="https://media.giphy.com/media/Y07F3fs9Is5byj4zK8/giphy.gif",
      caption=f"<b>You're Already Verified :) </b>\n",
      parse_mode="html")
  else:
    #chat_id = latest_message["message"]["chat"]["id"]
    #print(chat_id)
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=256)
    seed = mnemo.to_seed(words, passphrase="")
    account = w3.eth.account.privateKeyToAccount(seed[:32])
    private_key = account.privateKey
    public_key = account.address
    private_key = private_key.hex()
    #public_key = int(public_key)
    bot.send_message(message.chat.id,
                     f"<b><i><pre>{public_key}</pre></i></b>",
                     parse_mode="html")
    sent_msg = bot.send_message(
      message.chat.id,
      f"<b><i>To Get Verified And Access To The bot Make Sure You Have more than 1% of supply.\n\nIf you have then copy the above wallet address and send 0.001 bnb  to that address. \n\nThen reply to this msg  with your transaction hash </i></b> ",
      parse_mode="html",
    )
    bot.register_next_step_handler(message,
                                   process_name_step,
                                   data={'publicKey': public_key})


def process_name_step(message, data):
  hash = message.text
  public_key = data["publicKey"]
  if hash.startswith("0x"):
    #print("hi", hash)
    checkTxHash(hash, message, public_key)
  if hash.startswith("http"):
    #print("hlo", hash)
    newTx = hash.split("/")[4]
    checkTxHash(newTx, message, public_key)


def checkTxHash(tx, message, public_key):
  global wallets
  global verifiedAddyCache
  global allowed
  global ourTokenCa
  poocoin = f"<a href='https://poocoin.app/tokens/{ourTokenCa}'> Poocoin </a>"
  maestro = f"<a href='https://t.me/maestrosniperbot/?start={ourTokenCa}'>Maestro</a>"
  public_key = public_key.lower()
  params = {
    "transaction_hash": tx,
    "chain": "bsc",
  }
  try:
    result = evm_api.transaction.get_transaction(
      api_key=moralis_key,
      params=params,
    )
    print(result)
    fromAddy = result['from_address']
    toAddy = result['to_address']
    toAddy = toAddy.lower()
    if toAddy == public_key:
      print("true")
    if fromAddy not in wallets:
      print("true")
  except:
    bot.send_message(
      message.chat.id,
      f"<b><i> This dosent seem like a valid transaction hash</i></b>",
      parse_mode="html")
    return

  if toAddy == public_key and fromAddy not in wallets:
    urlCheck = ("https://api.bscscan.com/api"
                "?module=account"
                "&action=tokenbalance"
                f"&contractaddress={ourTokenCa}"
                f"&address={fromAddy}"
                "&tag=latest"
                "&apikey=JIW519CDP82K5S9QU9JFN8CPP8TRFSWXT7")
    response = requests.get(urlCheck)
    datac = response.text
    balance = int(json.loads(datac)['result'])
    balanceR = balance / 10**18
    if balanceR >= 9000:
      id = int(message.chat.id)
      username = message.chat.username
      bot.send_animation(
        message.chat.id,
        animation="https://media.giphy.com/media/veHIwhDRl780wT2XfC/giphy.gif",
        caption=f"<b>Verification SuccessFul.✅ </b>",
        parse_mode="html")
      allowed.append(id)
      wallets.append(fromAddy)
      verifiedAddyCache[fromAddy] = username
      bot_id = -1001550693632
      print(bot_id)
      bot.send_message(
        bot_id,
        f"User Verified\n id = {message.chat.id},\nAddy = {fromAddy}\nUsername:- @{username}"
      )
      cache_data(allowed, file_name)
      cache_data(verifiedAddyCache, addy_cache)
      cache_data(wallets, addys_cache)
      url = f"https://api.telegram.org/bot{Api_key}/createChatInviteLink"
      params = {'chat_id': -1001784003144, 'member_limit': 1}
      res = requests.get(url, params)
      link = res.json()
      linki = link['result']['invite_link']
      bot.send_message(
        message.chat.id,
        f"{linki}\n\n<b><i>Use this Link To Join The Whale 🐋Chat\nThis link will expire after 1 member join so dont share else you wont be able to join the chat.</i></b>",
        parse_mode="html")
    else:
      bot.send_message(
        message.chat.id,
        f"You dont have sufficent tokens. Use The link below to buy\n{poocoin}  {maestro}",
        parse_mode="html")
  else:
    bot.send_message(
      message.chat.id,
      "<b>Either You are already Verified or sent bnb to a wrong address</b>",
      parse_mode="html")


def getWalletAddys(addy, check):
  n = len(addy)
  subarrays = []
  allArray = []
  count = 0
  filterAddy = []
  for i in range(0, n, 19):
    subarray_start = i
    subarray_end = min(i + 19, n)
    subarray = addy[subarray_start:subarray_end]
    subarrays.append(subarray)
  #print(subarrays)
  for array in subarrays:
    #print(array)
    url = "https://api.bscscan.com/api"
    params = {
      "module": "account",
      "action": "balancemulti",
      "address": ",".join(array),
      "tag": "latest",
      "apikey": bscApi
    }
    response = requests.get(url, params=params)
    data = response.json()['result']
    allArray.extend(data)
  for acc in allArray:
    walet = acc['account']
    balance = float(acc['balance']) / 10**18
    if balance >= check:
      count = count + 1
      filterAddy.append(walet)
  return [count, filterAddy]


@bot.message_handler(commands=['order'])
def order(message):
  bot.send_message(
    message.chat.id,
    f"<b><u>Buy and burn .5 bnb worth of our tokens and then send a dm to @The_MightyGod</u></b>",
    parse_mode="html")


@bot.message_handler(commands=["detect"])
def detect(message):
  text = ""
  if message.chat.id not in allowed:
    bot.send_message(
      message.chat.id,
      f"<b><i>This is a premium feature. to use this make sure you hold more than 1% of supply and then press /verify</i></b>",
      parse_mode="html")
  else:
    if len(message.text.split(" ")) > 1:

      if message.text.split(" ")[1].startswith("0x"):
        if len(message.text.split(" ")) == 3:
          ca = message.text.split(" ")[1]
          check = (message.text.split(" ")[2])
          if check.replace(".", "", 1).isdigit():
            check = float((message.text.split(" ")[2]))
            chainName = "bsc-mainnet"
            try:
              url = f"https://api.covalenthq.com/v1/{chainName}/tokens/{ca}/token_holders/?key=ckey_a4afa01c9791458a9a222c44612"
              res = requests.get(url)
              data = res.text
              realD = json.loads(data)
              masala = realD['data']['items']
              #print(masala[0])
              decimal = int(masala[0]['contract_decimals'])
              name = masala[0]['contract_name']
              symbol = masala[0]['contract_ticker_symbol']
              supply = int(masala[0]['total_supply']) / 10**decimal
              #topBuyer = round(topBuyer,3)
              addy = getAddressInfo(masala)
              poocoin = f"<a href='https://poocoin.app/tokens/{ca}'>Poocoin</a>"
              maestro = f"<a href='https://t.me/MaestroSniperBot/?start={ca}'>Maestro</a>"
              contract = f"<a href='https://bscscan.com/token/{ca}'>Contract</a>"

            except:
              bot.send_message(
                message.chat.id,
                f"<b><i>Please Enter A Valid Binance Smart Chain Address</i></b>",
                parse_mode="html")
              return
            info = getWalletAddys(addy, check)
            count = info[0]
            filterAddy = info[1]
            if count == 0:
              bot.send_message(
                message.chat.id,
                f"<b><i>asic Info\n\nName:- {name}\nSymbol:-{symbol}\nTotalSupply:- {supply}\n\nNo Wallets Found with more than {check}bnb\n\n{poocoin}  {maestro} {contract}",
                parse_mode="html",
                disable_web_page_preview=True)
            else:
              for i, value in enumerate(filterAddy):
                values = f"<a href='https://bscscan.com/address/{value}'>Wallet {i+1}</a>"
                text = f"{text} {values}"
              bot.send_message(
                message.chat.id,
                f"<b><i>Basic Info\n\nName:- {name}\nSymbol:-{symbol}\nTotalSupply:- <pre>{supply}</pre>\nContract:- <pre>{ca}</pre>\n\nThere are {count} wallets with more than {check}bnb\n\n{poocoin}    {maestro}    {contract}\n--------------------------------------------------\nList of wallets {text}</i></b>",
                parse_mode="html",
                disable_web_page_preview=True)
          else:
            bot.send_message(
              message.chat.id,
              f"<b><i>Youre not using the correct input format ❌\n\n<u>/detect then wallet adress and the bnb amount you want to check</u>\n\nExample:- /detect 0xDead 2</i></b>",
              parse_mode="html")
        else:
          bot.send_message(
            message.chat.id,
            f"<b><i>Youre not using the correct input format ❌\n\n<u>/detect then wallet adress and the bnb amount you want to check</u>\n\nExample:- /detect 0xDead 2</i></b>",
            parse_mode="html")
      else:
        bot.send_message(message.chat.id,
                         f"Thats not a contract Address You dumb Bitch ❌❌")


bot.polling()
