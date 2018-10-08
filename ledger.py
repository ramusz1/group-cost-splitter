import sys

# const
group_delimiter = 'group '
comment_delimiter = '#'
even_split = 'even'

class Account:
    def __init__(self, owner, value):
        self.owner = owner
        self.value = value

    def __gt__( self, other ):
        return self.value > other.value

    def __ge__( self, other ):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= self.other

class Ledger:

    def __init__(self):
        self.minDifference = 0.5
        self.accounts = {}

    def setGroup(self, group ):
        self.group = group
        for member in group:
            if member not in self.accounts:
                self.accounts[ member ] = 0
        
    def evenSplit(self,  retard, loanValue):
        assert retard in self.group
        splitValue = loanValue / len( self.group )
        self.accounts[ retard ] += loanValue - splitValue
        debtors = [ x for x in self.group if x != retard ] 
        for debtor in debtors:
            self.accounts[ debtor ] -= splitValue

    def put( self, retard, loanValue ):
        assert retard in self.group
        self.accounts[ retard ] += loanValue

    def getTransactions(self): 
        currentValue = list( self.accounts.items() )
        currentValue = list ( map( lambda p: Account(p[0], p[1]),
                                self.accounts.items() )) 
        output = []

        biggestLoan = max( currentValue )
        biggestDebt = min( currentValue )

        while biggestLoan.value > self.minDifference or \
                abs( biggestDebt.value ) > self.minDifference:

            # try to get with one of these values to zero
            transactionValue = 0
            if biggestLoan.value > abs( biggestDebt.value ):
                transactionValue = abs( biggestDebt.value )
                biggestLoan.value -= transactionValue
                biggestDebt.value = 0
            else :
                transactionValue = abs( biggestLoan.value )
                biggestDebt.value += transactionValue
                biggestLoan.value = 0

            # save to output
            output.append(( biggestDebt.owner,
                            biggestLoan.owner,
                            transactionValue ))

            # update
            biggestLoan = max( currentValue )
            biggestDebt = min( currentValue )

        return output

    def dumpTransactions(self):
        print('transactions')
        for t in self.getTransactions():
            print( t[0], '->', t[1], ':', t[2])

    def dump(self):
        print('bank balance')
        for member, balance in self.accounts.items():
            print( member, balance )

def main( ledgerFile ):

    ledger = Ledger()

    with open( ledgerFile ) as file:
        goup = []
        for line in file.readlines():
            # remove \n from line end
            if line[-1] == '\n':
                line = line[:-1]
            print( line ) 
            if line.startswith( group_delimiter ):
                group = line.split(' ')[1:] # group a b c d -> [a, b, c, d]
                ledger.setGroup( group )
            elif line.startswith( comment_delimiter ):
                pass
            else :
                transaction = line.split(' ')
                if  len(transaction) < 2:
                    pass
                groupMember = transaction[0]
                transactionValue = int( transaction[1] )
                if len(transaction) == 3:
                    ledger.evenSplit( groupMember,transactionValue)
                else :
                    ledger.put( groupMember, transactionValue)

    ledger.dump()
    ledger.dumpTransactions()

     
if len( sys.argv ) <= 1 : 
    print('gib file to process')
    exit(1)

main(sys.argv[1])
            

