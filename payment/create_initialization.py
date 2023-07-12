from paycomuz import Paycom

paycom = Paycom()
url = paycom.create_initialization(amount=1000, order_id='197', return_url='https://www.youtube.com')
print(url)