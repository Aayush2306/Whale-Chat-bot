abiLp = [{
  "inputs": [{
    "internalType": "contract IUniFactory",
    "name": "_uniswapFactory",
    "type": "address"
  }],
  "stateMutability":
  "nonpayable",
  "type":
  "constructor"
}, {
  "anonymous":
  False,
  "inputs": [{
    "indexed": True,
    "internalType": "address",
    "name": "previousOwner",
    "type": "address"
  }, {
    "indexed": True,
    "internalType": "address",
    "name": "newOwner",
    "type": "address"
  }],
  "name":
  "OwnershipTransferred",
  "type":
  "event"
}, {
  "anonymous":
  False,
  "inputs": [{
    "indexed": False,
    "internalType": "address",
    "name": "lpToken",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "user",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "amount",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "lockDate",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "unlockDate",
    "type": "uint256"
  }],
  "name":
  "onDeposit",
  "type":
  "event"
}, {
  "anonymous":
  False,
  "inputs": [{
    "indexed": False,
    "internalType": "address",
    "name": "lpToken",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "amount",
    "type": "uint256"
  }],
  "name":
  "onWithdraw",
  "type":
  "event"
}, {
  "inputs": [],
  "name":
  "MIGRATION_IN",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [],
  "name":
  "gFees",
  "outputs": [{
    "internalType": "uint256",
    "name": "ethFee",
    "type": "uint256"
  }, {
    "internalType": "contract IERCBurn",
    "name": "secondaryFeeToken",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "secondaryTokenFee",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "secondaryTokenDiscount",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "liquidityFee",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "referralPercent",
    "type": "uint256"
  }, {
    "internalType": "contract IERCBurn",
    "name": "referralToken",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "referralHold",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "referralDiscount",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "_index",
    "type": "uint256"
  }],
  "name":
  "getLockedTokenAtIndex",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [],
  "name":
  "getNumLockedTokens",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_lpToken",
    "type": "address"
  }],
  "name":
  "getNumLocksForToken",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_user",
    "type": "address"
  }, {
    "internalType": "address",
    "name": "_lpToken",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "_index",
    "type": "uint256"
  }],
  "name":
  "getUserLockForTokenAtIndex",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }, {
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_user",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "_index",
    "type": "uint256"
  }],
  "name":
  "getUserLockedTokenAtIndex",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_user",
    "type": "address"
  }],
  "name":
  "getUserNumLockedTokens",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_user",
    "type": "address"
  }, {
    "internalType": "address",
    "name": "_lpToken",
    "type": "address"
  }],
  "name":
  "getUserNumLocksForToken",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_user",
    "type": "address"
  }],
  "name":
  "getUserWhitelistStatus",
  "outputs": [{
    "internalType": "bool",
    "name": "",
    "type": "bool"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "_index",
    "type": "uint256"
  }],
  "name":
  "getWhitelistedUserAtIndex",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [],
  "name":
  "getWhitelistedUsersLength",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_lpToken",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "_index",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_lockID",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_amount",
    "type": "uint256"
  }],
  "name":
  "incrementLock",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_lpToken",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "_amount",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_unlock_date",
    "type": "uint256"
  }, {
    "internalType": "address payable",
    "name": "_referral",
    "type": "address"
  }, {
    "internalType": "bool",
    "name": "_fee_in_eth",
    "type": "bool"
  }, {
    "internalType": "address payable",
    "name": "_withdrawer",
    "type": "address"
  }],
  "name":
  "lockLPToken",
  "outputs": [],
  "stateMutability":
  "payable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_lpToken",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "_index",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_lockID",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_amount",
    "type": "uint256"
  }],
  "name":
  "migrate",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [],
  "name":
  "owner",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_lpToken",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "_index",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_lockID",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_unlock_date",
    "type": "uint256"
  }],
  "name":
  "relock",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [],
  "name": "renounceOwnership",
  "outputs": [],
  "stateMutability": "nonpayable",
  "type": "function"
}, {
  "inputs": [{
    "internalType": "address payable",
    "name": "_devaddr",
    "type": "address"
  }],
  "name":
  "setDev",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "_referralPercent",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_referralDiscount",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_ethFee",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_secondaryTokenFee",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_secondaryTokenDiscount",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_liquidityFee",
    "type": "uint256"
  }],
  "name":
  "setFees",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_migrationIn",
    "type": "address"
  }],
  "name":
  "setMigrationIn",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "contract IMigrator",
    "name": "_migrator",
    "type": "address"
  }],
  "name":
  "setMigrator",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "contract IERCBurn",
    "name": "_referralToken",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "_hold",
    "type": "uint256"
  }],
  "name":
  "setReferralTokenAndHold",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_secondaryFeeToken",
    "type": "address"
  }],
  "name":
  "setSecondaryFeeToken",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_lpToken",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "_index",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_lockID",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_amount",
    "type": "uint256"
  }],
  "name":
  "splitLock",
  "outputs": [],
  "stateMutability":
  "payable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "name":
  "tokenLocks",
  "outputs": [{
    "internalType": "uint256",
    "name": "lockDate",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "amount",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "initialAmount",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "unlockDate",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "lockID",
    "type": "uint256"
  }, {
    "internalType": "address",
    "name": "owner",
    "type": "address"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_lpToken",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "_index",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_lockID",
    "type": "uint256"
  }, {
    "internalType": "address payable",
    "name": "_newOwner",
    "type": "address"
  }],
  "name":
  "transferLockOwnership",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "newOwner",
    "type": "address"
  }],
  "name":
  "transferOwnership",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [],
  "name":
  "uniswapFactory",
  "outputs": [{
    "internalType": "contract IUniFactory",
    "name": "",
    "type": "address"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_user",
    "type": "address"
  }, {
    "internalType": "bool",
    "name": "_add",
    "type": "bool"
  }],
  "name":
  "whitelistFeeAccount",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "_lpToken",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "_index",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_lockID",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "_amount",
    "type": "uint256"
  }],
  "name":
  "withdraw",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}]

abiPinksale = [{
  "anonymous":
  False,
  "inputs": [{
    "indexed": True,
    "internalType": "uint256",
    "name": "id",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "token",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "owner",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "amount",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "unlockDate",
    "type": "uint256"
  }],
  "name":
  "LockAdded",
  "type":
  "event"
}, {
  "anonymous":
  False,
  "inputs": [{
    "indexed": False,
    "internalType": "uint256",
    "name": "lockId",
    "type": "uint256"
  }],
  "name":
  "LockDescriptionChanged",
  "type":
  "event"
}, {
  "anonymous":
  False,
  "inputs": [{
    "indexed": False,
    "internalType": "uint256",
    "name": "lockId",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "owner",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "newOwner",
    "type": "address"
  }],
  "name":
  "LockOwnerChanged",
  "type":
  "event"
}, {
  "anonymous":
  False,
  "inputs": [{
    "indexed": True,
    "internalType": "uint256",
    "name": "id",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "token",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "owner",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "amount",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "unlockedAt",
    "type": "uint256"
  }],
  "name":
  "LockRemoved",
  "type":
  "event"
}, {
  "anonymous":
  False,
  "inputs": [{
    "indexed": True,
    "internalType": "uint256",
    "name": "id",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "token",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "owner",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "newAmount",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "newUnlockDate",
    "type": "uint256"
  }],
  "name":
  "LockUpdated",
  "type":
  "event"
}, {
  "anonymous":
  False,
  "inputs": [{
    "indexed": True,
    "internalType": "uint256",
    "name": "id",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "token",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "owner",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "amount",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "remaining",
    "type": "uint256"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "timestamp",
    "type": "uint256"
  }],
  "name":
  "LockVested",
  "type":
  "event"
}, {
  "inputs": [],
  "name":
  "allLpTokenLockedCount",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [],
  "name":
  "allNormalTokenLockedCount",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "name":
  "cumulativeLockInfo",
  "outputs": [{
    "internalType": "address",
    "name": "token",
    "type": "address"
  }, {
    "internalType": "address",
    "name": "factory",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "amount",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "lockId",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "newAmount",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "newUnlockDate",
    "type": "uint256"
  }],
  "name":
  "editLock",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "lockId",
    "type": "uint256"
  }, {
    "internalType": "string",
    "name": "description",
    "type": "string"
  }],
  "name":
  "editLockDescription",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "start",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "end",
    "type": "uint256"
  }],
  "name":
  "getCumulativeLpTokenLockInfo",
  "outputs": [{
    "components": [{
      "internalType": "address",
      "name": "token",
      "type": "address"
    }, {
      "internalType": "address",
      "name": "factory",
      "type": "address"
    }, {
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    }],
    "internalType":
    "struct PinkLock02.CumulativeLockInfo[]",
    "name":
    "",
    "type":
    "tuple[]"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "index",
    "type": "uint256"
  }],
  "name":
  "getCumulativeLpTokenLockInfoAt",
  "outputs": [{
    "components": [{
      "internalType": "address",
      "name": "token",
      "type": "address"
    }, {
      "internalType": "address",
      "name": "factory",
      "type": "address"
    }, {
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    }],
    "internalType":
    "struct PinkLock02.CumulativeLockInfo",
    "name":
    "",
    "type":
    "tuple"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "start",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "end",
    "type": "uint256"
  }],
  "name":
  "getCumulativeNormalTokenLockInfo",
  "outputs": [{
    "components": [{
      "internalType": "address",
      "name": "token",
      "type": "address"
    }, {
      "internalType": "address",
      "name": "factory",
      "type": "address"
    }, {
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    }],
    "internalType":
    "struct PinkLock02.CumulativeLockInfo[]",
    "name":
    "",
    "type":
    "tuple[]"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "index",
    "type": "uint256"
  }],
  "name":
  "getCumulativeNormalTokenLockInfoAt",
  "outputs": [{
    "components": [{
      "internalType": "address",
      "name": "token",
      "type": "address"
    }, {
      "internalType": "address",
      "name": "factory",
      "type": "address"
    }, {
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    }],
    "internalType":
    "struct PinkLock02.CumulativeLockInfo",
    "name":
    "",
    "type":
    "tuple"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "index",
    "type": "uint256"
  }],
  "name":
  "getLockAt",
  "outputs": [{
    "components": [{
      "internalType": "uint256",
      "name": "id",
      "type": "uint256"
    }, {
      "internalType": "address",
      "name": "token",
      "type": "address"
    }, {
      "internalType": "address",
      "name": "owner",
      "type": "address"
    }, {
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "lockDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycle",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycleBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "unlockedAmount",
      "type": "uint256"
    }, {
      "internalType": "string",
      "name": "description",
      "type": "string"
    }],
    "internalType":
    "struct PinkLock02.Lock",
    "name":
    "",
    "type":
    "tuple"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "lockId",
    "type": "uint256"
  }],
  "name":
  "getLockById",
  "outputs": [{
    "components": [{
      "internalType": "uint256",
      "name": "id",
      "type": "uint256"
    }, {
      "internalType": "address",
      "name": "token",
      "type": "address"
    }, {
      "internalType": "address",
      "name": "owner",
      "type": "address"
    }, {
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "lockDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycle",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycleBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "unlockedAmount",
      "type": "uint256"
    }, {
      "internalType": "string",
      "name": "description",
      "type": "string"
    }],
    "internalType":
    "struct PinkLock02.Lock",
    "name":
    "",
    "type":
    "tuple"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "token",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "start",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "end",
    "type": "uint256"
  }],
  "name":
  "getLocksForToken",
  "outputs": [{
    "components": [{
      "internalType": "uint256",
      "name": "id",
      "type": "uint256"
    }, {
      "internalType": "address",
      "name": "token",
      "type": "address"
    }, {
      "internalType": "address",
      "name": "owner",
      "type": "address"
    }, {
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "lockDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycle",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycleBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "unlockedAmount",
      "type": "uint256"
    }, {
      "internalType": "string",
      "name": "description",
      "type": "string"
    }],
    "internalType":
    "struct PinkLock02.Lock[]",
    "name":
    "",
    "type":
    "tuple[]"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [],
  "name":
  "getTotalLockCount",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "owner",
    "type": "address"
  }, {
    "internalType": "address",
    "name": "token",
    "type": "address"
  }, {
    "internalType": "bool",
    "name": "isLpToken",
    "type": "bool"
  }, {
    "internalType": "uint256",
    "name": "amount",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "unlockDate",
    "type": "uint256"
  }, {
    "internalType": "string",
    "name": "description",
    "type": "string"
  }],
  "name":
  "lock",
  "outputs": [{
    "internalType": "uint256",
    "name": "id",
    "type": "uint256"
  }],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "user",
    "type": "address"
  }],
  "name":
  "lpLockCountForUser",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "user",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "index",
    "type": "uint256"
  }],
  "name":
  "lpLockForUserAtIndex",
  "outputs": [{
    "components": [{
      "internalType": "uint256",
      "name": "id",
      "type": "uint256"
    }, {
      "internalType": "address",
      "name": "token",
      "type": "address"
    }, {
      "internalType": "address",
      "name": "owner",
      "type": "address"
    }, {
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "lockDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycle",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycleBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "unlockedAmount",
      "type": "uint256"
    }, {
      "internalType": "string",
      "name": "description",
      "type": "string"
    }],
    "internalType":
    "struct PinkLock02.Lock",
    "name":
    "",
    "type":
    "tuple"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "user",
    "type": "address"
  }],
  "name":
  "lpLocksForUser",
  "outputs": [{
    "components": [{
      "internalType": "uint256",
      "name": "id",
      "type": "uint256"
    }, {
      "internalType": "address",
      "name": "token",
      "type": "address"
    }, {
      "internalType": "address",
      "name": "owner",
      "type": "address"
    }, {
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "lockDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycle",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycleBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "unlockedAmount",
      "type": "uint256"
    }, {
      "internalType": "string",
      "name": "description",
      "type": "string"
    }],
    "internalType":
    "struct PinkLock02.Lock[]",
    "name":
    "",
    "type":
    "tuple[]"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address[]",
    "name": "owners",
    "type": "address[]"
  }, {
    "internalType": "uint256[]",
    "name": "amounts",
    "type": "uint256[]"
  }, {
    "internalType": "address",
    "name": "token",
    "type": "address"
  }, {
    "internalType": "bool",
    "name": "isLpToken",
    "type": "bool"
  }, {
    "internalType": "uint256",
    "name": "tgeDate",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "tgeBps",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "cycle",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "cycleBps",
    "type": "uint256"
  }, {
    "internalType": "string",
    "name": "description",
    "type": "string"
  }],
  "name":
  "multipleVestingLock",
  "outputs": [{
    "internalType": "uint256[]",
    "name": "",
    "type": "uint256[]"
  }],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "user",
    "type": "address"
  }],
  "name":
  "normalLockCountForUser",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "user",
    "type": "address"
  }, {
    "internalType": "uint256",
    "name": "index",
    "type": "uint256"
  }],
  "name":
  "normalLockForUserAtIndex",
  "outputs": [{
    "components": [{
      "internalType": "uint256",
      "name": "id",
      "type": "uint256"
    }, {
      "internalType": "address",
      "name": "token",
      "type": "address"
    }, {
      "internalType": "address",
      "name": "owner",
      "type": "address"
    }, {
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "lockDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycle",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycleBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "unlockedAmount",
      "type": "uint256"
    }, {
      "internalType": "string",
      "name": "description",
      "type": "string"
    }],
    "internalType":
    "struct PinkLock02.Lock",
    "name":
    "",
    "type":
    "tuple"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "user",
    "type": "address"
  }],
  "name":
  "normalLocksForUser",
  "outputs": [{
    "components": [{
      "internalType": "uint256",
      "name": "id",
      "type": "uint256"
    }, {
      "internalType": "address",
      "name": "token",
      "type": "address"
    }, {
      "internalType": "address",
      "name": "owner",
      "type": "address"
    }, {
      "internalType": "uint256",
      "name": "amount",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "lockDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeDate",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "tgeBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycle",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "cycleBps",
      "type": "uint256"
    }, {
      "internalType": "uint256",
      "name": "unlockedAmount",
      "type": "uint256"
    }, {
      "internalType": "string",
      "name": "description",
      "type": "string"
    }],
    "internalType":
    "struct PinkLock02.Lock[]",
    "name":
    "",
    "type":
    "tuple[]"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "lockId",
    "type": "uint256"
  }],
  "name":
  "renounceLockOwnership",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "token",
    "type": "address"
  }],
  "name":
  "totalLockCountForToken",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "user",
    "type": "address"
  }],
  "name":
  "totalLockCountForUser",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [],
  "name":
  "totalTokenLockedCount",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "lockId",
    "type": "uint256"
  }, {
    "internalType": "address",
    "name": "newOwner",
    "type": "address"
  }],
  "name":
  "transferLockOwnership",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "lockId",
    "type": "uint256"
  }],
  "name":
  "unlock",
  "outputs": [],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "address",
    "name": "owner",
    "type": "address"
  }, {
    "internalType": "address",
    "name": "token",
    "type": "address"
  }, {
    "internalType": "bool",
    "name": "isLpToken",
    "type": "bool"
  }, {
    "internalType": "uint256",
    "name": "amount",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "tgeDate",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "tgeBps",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "cycle",
    "type": "uint256"
  }, {
    "internalType": "uint256",
    "name": "cycleBps",
    "type": "uint256"
  }, {
    "internalType": "string",
    "name": "description",
    "type": "string"
  }],
  "name":
  "vestingLock",
  "outputs": [{
    "internalType": "uint256",
    "name": "id",
    "type": "uint256"
  }],
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "inputs": [{
    "internalType": "uint256",
    "name": "lockId",
    "type": "uint256"
  }],
  "name":
  "withdrawableTokens",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "stateMutability":
  "view",
  "type":
  "function"
}]

abiPcs = [{
  "inputs": [{
    "internalType": "address",
    "name": "_feeToSetter",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "nonpayable",
  "type":
  "constructor"
}, {
  "anonymous":
  False,
  "inputs": [{
    "indexed": True,
    "internalType": "address",
    "name": "token0",
    "type": "address"
  }, {
    "indexed": True,
    "internalType": "address",
    "name": "token1",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "pair",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "name":
  "PairCreated",
  "type":
  "event"
}, {
  "constant":
  True,
  "inputs": [],
  "name":
  "INIT_CODE_PAIR_HASH",
  "outputs": [{
    "internalType": "bytes32",
    "name": "",
    "type": "bytes32"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  True,
  "inputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "name":
  "allPairs",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  True,
  "inputs": [],
  "name":
  "allPairsLength",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  False,
  "inputs": [{
    "internalType": "address",
    "name": "tokenA",
    "type": "address"
  }, {
    "internalType": "address",
    "name": "tokenB",
    "type": "address"
  }],
  "name":
  "createPair",
  "outputs": [{
    "internalType": "address",
    "name": "pair",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "constant":
  True,
  "inputs": [],
  "name":
  "feeTo",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  True,
  "inputs": [],
  "name":
  "feeToSetter",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  True,
  "inputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }, {
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "name":
  "getPair",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  False,
  "inputs": [{
    "internalType": "address",
    "name": "_feeTo",
    "type": "address"
  }],
  "name":
  "setFeeTo",
  "outputs": [],
  "payable":
  False,
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "constant":
  False,
  "inputs": [{
    "internalType": "address",
    "name": "_feeToSetter",
    "type": "address"
  }],
  "name":
  "setFeeToSetter",
  "outputs": [],
  "payable":
  False,
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}]

abiPcs = [{
  "inputs": [{
    "internalType": "address",
    "name": "_feeToSetter",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "nonpayable",
  "type":
  "constructor"
}, {
  "anonymous":
  False,
  "inputs": [{
    "indexed": True,
    "internalType": "address",
    "name": "token0",
    "type": "address"
  }, {
    "indexed": True,
    "internalType": "address",
    "name": "token1",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "address",
    "name": "pair",
    "type": "address"
  }, {
    "indexed": False,
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "name":
  "PairCreated",
  "type":
  "event"
}, {
  "constant":
  True,
  "inputs": [],
  "name":
  "INIT_CODE_PAIR_HASH",
  "outputs": [{
    "internalType": "bytes32",
    "name": "",
    "type": "bytes32"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  True,
  "inputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "name":
  "allPairs",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  True,
  "inputs": [],
  "name":
  "allPairsLength",
  "outputs": [{
    "internalType": "uint256",
    "name": "",
    "type": "uint256"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  False,
  "inputs": [{
    "internalType": "address",
    "name": "tokenA",
    "type": "address"
  }, {
    "internalType": "address",
    "name": "tokenB",
    "type": "address"
  }],
  "name":
  "createPair",
  "outputs": [{
    "internalType": "address",
    "name": "pair",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "constant":
  True,
  "inputs": [],
  "name":
  "feeTo",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  True,
  "inputs": [],
  "name":
  "feeToSetter",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  True,
  "inputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }, {
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "name":
  "getPair",
  "outputs": [{
    "internalType": "address",
    "name": "",
    "type": "address"
  }],
  "payable":
  False,
  "stateMutability":
  "view",
  "type":
  "function"
}, {
  "constant":
  False,
  "inputs": [{
    "internalType": "address",
    "name": "_feeTo",
    "type": "address"
  }],
  "name":
  "setFeeTo",
  "outputs": [],
  "payable":
  False,
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}, {
  "constant":
  False,
  "inputs": [{
    "internalType": "address",
    "name": "_feeToSetter",
    "type": "address"
  }],
  "name":
  "setFeeToSetter",
  "outputs": [],
  "payable":
  False,
  "stateMutability":
  "nonpayable",
  "type":
  "function"
}]
