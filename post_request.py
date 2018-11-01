import requests

URL="https://www.daft.ie/dublin/apartments-for-rent/ballsbridge/100-merrion-road-ballsbridge-dublin-1878359/"

##test data on random property url
payload = {
    'name': 'Tom',
    'email': 'tom@gmail.com',
    'contact_number': '0852021111',
    'your_message': 'blank',
    'terms': '1'
}

session = requests.session()
r = requests.post(URL, data=payload)
print('done')  #Testing to see if script makes it here ****currently doesn't
print (r.cookies)
