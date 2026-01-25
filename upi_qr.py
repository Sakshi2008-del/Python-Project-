import upi_qr

#taking upi id as input
upi_id = input("enter your upi id = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#qr code gnrating

phonepay_qr = upi_qr.make(phonepay_url)
paytm_qr = upi_qr.make(paytm_url)
google_pay_qr = upi_qr.make(google_pay_url)

#save the qr code to image file

phonepay_qr.save('phonepay_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#dispay the qr code 

phonepay_qr.show()
paytm_qr.show()
google_pay_qr.show()


