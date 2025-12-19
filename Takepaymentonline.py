import qrcode

# taking UPI id in input
upi_id = input ("Enter your UPI ID = ")

# upi://pay?pa=upi_id&pn=Name&am=amount&cu=Currency&tn=massage

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name'

# Create the QRcode for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)


# save the QRcode to image file

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

