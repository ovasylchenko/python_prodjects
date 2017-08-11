import requests
from bs4 import BeautifulSoup

doubls = 0
saved = 0
all = 0
ins = 0
notf = 0
str2 = ''
str4 = 'Product (1)'
openfile1 = open('new СAS_487.txt', "r")
openfile2 = open('result_tcichem2.txt', "w")
openfile3 = open('tcichem_out2.txt', "w")
openfile4 = open('tcichem_out5.txt', "w")
Cas_numbers = []
links = []
for line in openfile1:
    Cas_numbers.append(line[:-1])
openfile1.close()
str1 = 'http://www.tcichemicals.com'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }

for ele in Cas_numbers:
    all += 1
    url = 'http://www.tcichemicals.com/eshop/en/eu/catalog/list/search?searchWord=' + ele + '&client=default_frontend&output=xml_no_dtd&proxystylesheet=default_frontend&sort=date%3AD%3AL%3Ad1&oe=UTF-8&ie=UTF-8&ud=1&exclude_apps=1&site=en_eu&mode=0'
    r = requests.get(url, headers=headers)
    with open('test.html', 'wb') as output_file:
        output_file.write(r.text.encode('UTF-8'))
    output_file.close()
    output_file1 = open('test.html', 'r')
    html = output_file1.read()
    output_file1.close()
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('td', {'class': "comp-td", 'colspan': "2"})
    if div:
        div3 = soup.find('div', {'class': "search-category"})
        strx = str(div3)
        if str4 in strx:
            chek1 = 0
            chek2 = 0
            li = div.find('a')
            li2 = li.get('href')
            link = str1 + str(li2)
            name2 = div.find('a')
            li4 = str(name2)
            for ele4 in li4:
                if ele4 == '<':
                    chek2 += 1
                if chek1 == 2 and chek2 == 2:
                    str2 += str(ele4)
                if ele4 == '>':
                    chek1 += 1
            fin_str = str(ele) + '\t' + str(str2) + '\t' + str(link) + '\n'
            openfile2.write(fin_str)
            saved += 1
            if link in links:
                doubls += 1
            str2 = ''
            print(fin_str)
        else:
            openfile4.write(ele)
            openfile4.write('\n')
            ins += 1
            print("ins found\n")
    else:
        openfile3.write(ele)
        openfile3.write('\n')
        print("not found\n")
        notf += 1
openfile2.close()
openfile3.close()
openfile4.close()
def ola():
    print(all)
    print(saved)
    print(doubls)
    print(ins)

if __name__ == "__main__":
    ola()
