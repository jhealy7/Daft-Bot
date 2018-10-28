from bs4 import BeautifulSoup
import urllib.request

fp = urllib.request.urlopen("https://www.daft.ie/dublin-city/residential-property-for-rent/south-dublin-city/?s%5Bmxp%5D=1650&s%5Badvanced%5D=1&s%5Bignored_agents%5D%5B0%5D=428&s%5Bignored_agents%5D%5B1%5D=1551&s%5Bsort_by%5D=date&s%5Bsort_type%5D=d&searchSource=rental")
soup = BeautifulSoup(fp,'html.parser')

fp.close()

print(soup.prettify())
