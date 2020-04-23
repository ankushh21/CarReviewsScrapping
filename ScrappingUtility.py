# Scrappinf related functions
def getplayerdetails(cntr, block):
    playerlist = list()
    playerlist.append(str(cntr))
    for playername in block.find_all('div'):
        print(playername.text, end='\t')
        playerlist.append(playername.text)
    print()
    return playerlist
