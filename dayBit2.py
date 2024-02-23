# tyjkot - 12.23.2024

import requests
import time

# Constants
BITCOIN_API_URL = "https://blockchain.info/q/getblockcount"
GENESIS_BLOCK_HEIGHT = 0
BLOCK_REWARD_HALVING_INTERVAL = 210000
SECONDS_IN_A_DAY = 86400
AVERAGE_BLOCKS_PER_DAY = 144

def get_current_block_height():
    response = requests.get(BITCOIN_API_URL)
    return int(response.text)

def get_reward_halving_timestamp(current_block_height):
    blocks_to_halving = BLOCK_REWARD_HALVING_INTERVAL - (current_block_height % BLOCK_REWARD_HALVING_INTERVAL)
    blocks_to_halving_seconds = blocks_to_halving * SECONDS_IN_A_DAY
    return int(time.time()) + blocks_to_halving_seconds

def get_bitcoin_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    return response.json()['bpi']['USD']['rate_float']

def main():
    current_block_height = get_current_block_height()
    halving_timestamp = get_reward_halving_timestamp(current_block_height)
    blocks_left = BLOCK_REWARD_HALVING_INTERVAL - (current_block_height % BLOCK_REWARD_HALVING_INTERVAL)
    days_left = blocks_left / AVERAGE_BLOCKS_PER_DAY
    bitcoin_price = get_bitcoin_price()

    print(f"Bitcoin price: ${bitcoin_price:.2f}")
    print(f"Blocks left until next halving: {blocks_left}")
    print(f"Estimated days left until next halving: {days_left:.2f}")

if __name__ == "__main__":
    main()
