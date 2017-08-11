import requests
from bs4 import BeautifulSoup
str0 = ''
str1 = ''
str2 = ''
str3 = 'Found no results for'
doubls = 0
saved = 0
saved1 = 0
all = 0
chek1 = 0
chek2 = 0
no_found = 0
nt_at = 0
openfile1 = open('new СAS_487.txt', "r")
openfile2 = open('result_scbt3.txt', "w")
openfile3 = open('deiterii_scbt3.txt', "w")
openfile4 = open('no_found_scbt3.txt', "w")
Cas_numbers = []
links = []
for line in openfile1:
    Cas_numbers.append(line[:-1])
openfile1.close()
str01 = 'http://www.tcichemicals.com'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }

for ele in Cas_numbers:
    all += 1
    url = 'https://www.scbt.com/scbt/search?Ntt=' + ele
    r = requests.get(url, headers=headers)
    with open('test.html', 'wb') as output_file:
        output_file.write(r.text.encode('UTF-8'))
    output_file.close()
    output_file1 = open('test.html', 'r')
    html = output_file1.read()
    output_file1.close()
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find('meta', {'property': "og:url"})
    if div:
        li2 = div.get('content')
        div = soup.find('meta', {'property': "og:title"})
        titl = div.get('content')
        for ele2 in titl:
            if ele2 != '|':
                str0 += str(ele2)
            else:
                str0 = str0[:-1]
                break
        fin_str = str(ele) + '\t' + str0 + '\t' + str(li2) + '\n'
        str0 = ''
        print(fin_str)
        if str0 in links:
            doubls += 1
        saved += 1
        openfile2.write(fin_str)
    else:
        div = soup.find('h1').next_sibling.next_sibling
        if div:
            str5 = str(div)
            if str3 in str5:
                openfile4.write(ele)
                openfile4.write('\n')
                no_found += 1
                print(ele, " not found\n")
                continue
        div = soup.find('td', {'data-label': "PRODUCT NAME"})
        if div:
            li3 = div.find('a')
            link4 = li3.get('href')
            for ele3 in link4:
                if ele3 != ';':
                    str1 += str(ele3)
                else:
                    break
            li4 = str(li3)
            for ele4 in li4:
                if ele4 == '<':
                    chek2 += 1
                if chek1 == 1 and chek2 == 1:
                    str2 += str(ele4)
                if ele4 == '>':
                    chek1 += 1
            fin_str = str(ele) + '\t' + str2 + '\t' + str1 + '\n'
            str2 = ''
            str1 = ''
            chek1 = 0
            chek2 = 0
            print("insec", fin_str)
            saved1 += 1

            if str1 in links:
                doubls += 1
            openfile3.write(fin_str)
        else:
            print("not at all\n")
            nt_at += 1
openfile2.close()
openfile3.close()
openfile4.close()

def ola():
    print("all: ", all, '\n')
    print("normal saved: ", saved, '\n')
    print("insection: ", saved1, '\n')
    print("dublicats: ", doubls, '\n')
    print("no_found: ", no_found, '\n')
    print("not at all: ", nt_at, '\n')

if __name__ == "__main__":
    ola()
