import requests
from bs4 import BeautifulSoup


def ola():
    doubls = 0
    saved = 0
    all = 0
    alert = 0
    openfile1 = open('new СAS_487.txt', "r")
    openfile2 = open('result_topric2.txt', "w")
    openfile3 = open('topric_out2.txt', "w")
    Cas_numbers = []
    links = []
    for line in openfile1:
        Cas_numbers.append(line[:-1])
    openfile1.close()
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }
    for ele in Cas_numbers:
        str0 = ''
        all += 1
        url = 'https://www.tocris.com/search.php?Value=' + ele + '&Type=QuickSearch&SrchdFrom=Header'
        r = requests.get(url, headers=headers)
        with open('test.html', 'wb') as output_file:
            output_file.write(r.text.encode('UTF-8'))
        output_file.close()
        output_file1 = open('test.html', 'r')
        html = output_file1.read()
        output_file1.close()
        soup = BeautifulSoup(html, 'lxml')
        div = soup.find('meta', {'name': "twitter:title"})
        if div:
            name = div.get('content')
            if name[0:5] == "Searc":
                openfile3.write(ele)
                openfile3.write('\n')
                continue
            for ele2 in name:
                if ele2 != '|':
                    str0 += str(ele2)
                else:
                    str0 = str0[:-10]
                    break
            div1 = soup.find('link', {'rel': "canonical"})
            link = div1.get('href')
            fin_str = str(ele) + '\t' + str0 + '\t' + str(link) + '\n'
            openfile2.write(fin_str)
            print(fin_str)
            saved += 1
            if link in links:
                doubls += 1
                openfile3.write(link)
            else:
                links.append(link)
        else:
            openfile3.write(ele)
            openfile3.write('???')
            openfile3.write('\n')
            alert += 1
    openfile2.close()
    openfile3.close()

    print(len(links))
    print(saved)
    print(doubls)
    print(alert)

if __name__ == "__main__":
    ola()
