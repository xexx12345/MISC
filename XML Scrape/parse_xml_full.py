import xml.etree.ElementTree as ET
import codecs

fileBase = 'FULINS_S_20180303_02of02'
inFinInstrm_tag = False
inFinInstrmGnlAttrbts = False
inTradgVnRltdAttrbts = False
inTechAttrbts = False

outRcrd = ''
AdmssnApprvlDtByIssrVal = ''
ReqForAdmssnDtVal = ''
FrstTradDtVal = ''
TechAttrbtsVal = ''
RlvntCmptntAuthrtyVal = ''

csvOutput  = codecs.open(fileBase + '.csv', mode="w", encoding='utf-8')
csvOutput.write('FinInstrmGnlAttrbts.Id, FinInstrmGnlAttrbts.FullNm, FinInstrmGnlAttrbts.ShrtNm, TradgVnRltdAttrbts.Id ,TradgVnRltdAttrbts.AdmssnApprvlDtByIssr, TradgVnRltdAttrbts.ReqForAdmssnDt, TradgVnRltdAttrbts.FrstTradDt, TechAttrbts.RlvntCmptntAuthrty\n')
for event, elem in ET.iterparse(fileBase + ".xml", events=("start", "end")):
    # process your person data
    tag = elem.tag.split('}', 1)[1]
    value = elem.text

    try :
        value = value.decode()
    except AttributeError:
        pass

    if value is None:
        value = ''

    value = value.replace(',', ' ')

    if event == 'start' :

        if tag == 'FinInstrmGnlAttrbts' :
            inFinInstrmGnlAttrbts = True
        elif tag == 'TradgVnRltdAttrbts' :
            inTradgVnRltdAttrbts = True
        elif tag == 'TechAttrbts' :
            inTechAttrbts = True

    if tag == 'Id' and inFinInstrmGnlAttrbts == True and value != '':
        outRcrd = outRcrd + value
    elif tag == 'FullNm' and inFinInstrmGnlAttrbts == True and value != '':
        outRcrd = outRcrd + ',' + value
    elif tag == 'ShrtNm' and inFinInstrmGnlAttrbts == True  and value != '':
        outRcrd = outRcrd + ',' + value
    elif tag == 'Id' and inTradgVnRltdAttrbts == True and value != '':
        outRcrd = outRcrd + ',' + value
    elif tag == 'AdmssnApprvlDtByIssr' and inTradgVnRltdAttrbts == True  and value != '':
        AdmssnApprvlDtByIssrVal = value
    elif tag == 'ReqForAdmssnDt'  and inTradgVnRltdAttrbts == True  and value != '':
        ReqForAdmssnDtVal = value
    elif tag == 'FrstTradDt'  and inTradgVnRltdAttrbts == True  and value != '':
        FrstTradDtVal = value
    elif tag == 'RlvntCmptntAuthrty' and inTechAttrbts == True and value !='':
        RlvntCmptntAuthrtyVal = value

    if event == 'end' :

        #if tag == 'Id' and inFinInstrmGnlAttrbts == True and value != '':
        #    outRcrd = outRcrd + ',' + value

        if tag == 'FinInstrmGnlAttrbts' :
            inFinInstrmGnlAttrbts = False

        elif tag == 'TechAttrbts' :
            outRcrd = outRcrd + ',' + RlvntCmptntAuthrtyVal
            RlvntCmptntAuthrtyVal = ''
            inTechAttrbts = False

        elif tag == 'TradgVnRltdAttrbts' :
            outRcrd = outRcrd + ',' + AdmssnApprvlDtByIssrVal
            outRcrd = outRcrd + ',' + ReqForAdmssnDtVal
            outRcrd = outRcrd + ',' + FrstTradDtVal

            AdmssnApprvlDtByIssrVal = ''
            ReqForAdmssnDtVal = ''
            FrstTradDtVal = ''

            inTradgVnRltdAttrbts = False

        elif tag == 'RefData' :
            #print(outRcrd)
            csvOutput.write(outRcrd + '\n')
            outRcrd = ''



    elem.clear()

csvOutput.close()