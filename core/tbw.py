#!/usr/bin/env python
from config.configure import Configure
from network.network import Network
from modules.allocate import Allocate
from modules.blocks import Blocks
from modules.initialize import Initialize
from modules.payments import Payments
from modules.stage import Stage
from modules.voters import Voters
from utility.database import Database
#from utility.sql import Sql
#from utility.utility import Utility


if __name__ == '__main__':
    print("Start Processing")

    # get configuration
    config = Configure()
    
    #load network
    network = Network(config.network)
    
    # check if initialized
    
    
    # connect to database
    database = Database(config, network)
    database.open_connection()
    database.get_publickey()
    print(database.publickey)
    database.get_current_nonce()
    print(database.nonce)
    database.close_connection()
    
    
    # process blocks
    
    
    
    # allocate block rewards
    
    
    
    # process payments
    print("End Processing")
