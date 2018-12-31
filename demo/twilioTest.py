from twilio.rest import Client

account = 'AC6e8050c5a63ba6ec813a9a6d1132d4f3'
token = 'd76deccc334126c93869c14e067b79ca'
myNumber = '+8618688900954'
twilioNumber = '+19033001537'
client = Client(account, token)

def textmyself(message):
    message = client.messages.create(to=myNumber, from_=twilioNumber,
                                     body=message)

if __name__ == '__main__':
    textmyself("打开支付宝首页搜“575441631”领红包，领到大红包的小伙伴赶紧使用哦111！")