# Trying www.cricbuzz.com scrapping
import requests
from bs4 import BeautifulSoup
import csv
import ScrappingUtility as su

with open('MatchDetails.csv', 'w', newline='') as myfile:
    csv_Writer = csv.writer(myfile, delimiter=',')
    siteurl = 'https://www.cricbuzz.com/live-cricket-scorecard/22396/csk-vs-rcb-1st-match-indian-premier-league-2019'
    htmlcontent = requests.get(siteurl).content
    sitesoup = BeautifulSoup(htmlcontent, 'html.parser')

    sitetab = sitesoup.title.text
    print('Tab Name: ', sitetab)

    mainpage = sitesoup.find('div', class_='page').find('div', class_='container').find('div', class_='cb-col cb-col-100 cb-bg-white')

    matchdetails = mainpage.find('div', class_='cb-nav-main cb-col-100 cb-col cb-bg-white')
    matchname = matchdetails.find('h1').text.split('-')[0]
    print('Match name : ', matchname)
    matchsubdetails = matchdetails.find('div', class_='cb-nav-subhdr cb-font-12')
    seriesname = matchsubdetails.find('span', class_='text-hvr-underline text-gray').text
    print('Series name : ', seriesname)
    stadiumname = matchsubdetails.find('span', itemprop='name').text
    print('Stadium name : ', stadiumname)
    Stadiumlocation = matchsubdetails.find('span', itemprop='addressLocality').text
    print('Stadium Location : ', Stadiumlocation)
    matchdatetime = matchsubdetails.find('span', itemprop='startDate').text
    print('Match Date : ', matchdatetime)

    csv_Writer.writerow(['Match name : ', matchname])
    csv_Writer.writerow(['Series name : ', seriesname])
    csv_Writer.writerow(['Stadium name : ', stadiumname])
    csv_Writer.writerow(['Stadium Location : ', Stadiumlocation])
    csv_Writer.writerow(['Match Date : ', matchdatetime])
    csv_Writer.writerow(['\n'])

    matchinningdtl = mainpage.find('div', class_='cb-col cb-col-67 cb-scrd-lft-col html-refresh')
    matchresult = matchinningdtl.find('div').text
    print('Match result:', matchresult)

    for Playertable in mainpage.find_all('div', class_='cb-col cb-col-100 cb-ltst-wgt-hdr'):
        # print(Playertable.prettify())
        try:
            Inningname = Playertable.find('span').text
            print('Team : ', Inningname)
            Inningscore = Playertable.find('span', class_='pull-right').text
            print('Team Score: ', Inningscore)
        except AttributeError as myerror:
            print('Bowling...')
            csv_Writer.writerow(['\n'])
            pass
        finally:
            Plyertblheading = Playertable.find('div', class_='cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray')
            tblheading = list()
            tblheading.append('Sr. No.')
            for playerheading in Plyertblheading.find_all('div'):
                if playerheading.text == '':
                    tblheading.append('Out to bowler')
                else:
                    tblheading.append(playerheading.text)
            print('Table Heading ::', tblheading)
            csv_Writer.writerow(tblheading)

            srnum = 0
            for playerdtl in Playertable.find_all('div', 'cb-col cb-col-100 cb-scrd-itms'):
                srnum += 1
                csv_Writer.writerow(su.getplayerdetails(srnum, playerdtl))
