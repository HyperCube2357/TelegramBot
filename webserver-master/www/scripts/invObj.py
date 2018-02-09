from time import gmtime, strftime
import rc4
import sys
key = raw_input('Enter your Private key: ')

class invPacket():

    def __init__(self,phone,photo,location,type_weed,amount):
        self.phone = rc4.encrypt(key,phone)
        self.photo = rc4.encrypt(key,photo)
        self.location = rc4.encrypt(key,location)
        self.type_weed = rc4.encrypt(key,type_weed)
        self.amount = rc4.encrypt(key,amount)
        self.time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    def to_log_file(self):
        with open('LogFile.html','a') as f:
         f.write('<br><br>Phone Number: ' + self.phone + '<br> Location: '+ self.location + '<br> Time:' + self.time + '<br> Amount:' + self.amount + '<br> Type:' + self.type_weed)

    def to_Http(self):
        print ('Phone Number: ' + self.phone + '\n Location: '+ self.location + '\n Time:' + self.time + '\n Amount:' + self.amount + '\n Type:' + self.type_weed)


invitation = invPacket('kosomo','ars','mira','zonzonet','gdola')
invitation.to_log_file()
invitation.to_Http()