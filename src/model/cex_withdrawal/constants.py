CEX_WITHDRAWAL_RPCS = {
    "Arbitrum": "https://rpc.ankr.com/arbitrum",
    "Optimism": "https://rpc.ankr.com/optimism",
    "Base": "https://rpc.ankr.com/base",
}

# Network name mappings for different exchanges
NETWORK_MAPPINGS = {
    "okx": {
        "Arbitrum": "ARBONE",
        "Base": "Base",
        "Optimism": "OPTIMISM"
    },
    "bitget": {
        "Arbitrum": "ARBITRUMONE",
        "Base": "BASE",
        "Optimism": "OPTIMISM"
    }
}

# Exchange-specific parameters
EXCHANGE_PARAMS = {
    "okx": {
        "balance": {"type": "funding"},
        "withdraw": {"pwd": "-"}
    },
    "bitget": {
        "balance": {},
        "withdraw": {}
    }
}

# Supported exchanges
SUPPORTED_EXCHANGES = ["okx", "bitget"]