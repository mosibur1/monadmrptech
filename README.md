# Monad Testnet Automation

This tool automates interactions with the Monad testnet, including various DeFi operations and token interactions.

# All features are available in config:
# FAUCETS
"faucet" - get tokens from faucet

"farm_faucet" - get tokens from faucet ON FARM ACCOUNTS (data/keys_for_faucet.txt)

"disperse_farm_accounts" - disperse tokens from farm accounts to main accounts | keys_for_faucet.txt -> private_keys.txt

"disperse_from_one_wallet" - disperse tokens from one wallet to all other wallets | keys_for_faucet.txt (first wallet) -> private_keys.txt

# SWAPS
"collect_all_to_monad" - swap all tokens to native token (MON)

"swaps" - testnet.monad.xyz/ page token swaps

"bean" - swap tokens on Bean DEX

"ambient" - swap tokens on Ambient DEX

"izumi" - swap tokens on Izumi DEX

# STAKES
"apriori" - stake MON token

"magma" - stake MON token on Magma

"shmonad" - buy and stake shmon on shmonad.xyz | LOOK SETTINGS BELOW

"kintsu" - stake MON token on kintsu.xyz/

# MINT
"magiceden" - mint NFT on magiceden.io

"accountable" - mint accountable nft

"owlto" - deploy contract on Owlto

"lilchogstars" - mint NFT on testnet.lilchogstars.com/

"demask" - mint NFT on app.demask.finance/launchpad/0x2cdd146aa75ffa605ff7c5cc5f62d3b52c140f9c/0

"monadking" - mint NFT on nerzo.xyz/monadking

"monadking_unlocked" - mint NFT on www.nerzo.xyz/unlocked

# REFUEL
"gaszip" - gaszip refuel from arbitrum, optimism, base to monad

"orbiter" - bridge ETH from Sepolia to Monad via Orbiter

"memebridge" - memebridge refuel from arbitrum, optimism, base to monad

# OTHER
"logs" - show logs: MON balance | number of transactions | avarage balance | avarage number of transactions

"nad_domains" - register random domain on nad.domains

"aircraft" - mint NFT on aircraft.fun

## Requirements
- Python 3.11 or higher

## Installation

1. Clone the repository
```bash
git clone https://github.com/mosibur1/monadmrptech.git
cd monadmrptech
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure the bot by starting it (py main.py) and choosing the edit config option`

```

4. Add your data to the following files:
- `data/private_keys.txt` - One private key per line
- `data/proxies.txt` - One proxy per line (format: `user:pass@ip:port`)


5. Run the bot
```bash
python main.py
```

## Support
- Telegram: https://t.me/mrptechofficial
