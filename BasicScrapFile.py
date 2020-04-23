# Trying www.cricbuzz.com scrapping

import ScrappingUtility as su

def PlayerTable (mainpage):
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
