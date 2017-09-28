#  #!/usr/bin/env python
__AUTHOR__='Danevych V.'
__COPYRIGHT__='Danevych V. 2016 Kiev, Ukraine'
#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import csv

  
"""
/opt/ericsson/ddc/util/bin/listme | grep RBS_NODE_MODEL | sed -e 's/[@=,]/ /g' | grep KIER  | awk '{print $4 ";" $6 ";" $7 }' | sort| uniq > ${wdir}/ipdatabase.txt
KIER2;KI0026;10.82.39.177
KIER2;KI0027;10.82.45.164

/opt/ericsson/ddc/util/bin/listme | grep RBS_NODE_MODEL | sed -e 's/[@=,]/ /g' | grep KIER  | awk '{print $6 "   " $7 "   "	"rbs"}' | sort| uniq > ${wdir}/ipdatabase.txt
CH0017   10.83.40.195   rbs
CH0018   10.83.40.17   rbs

/opt/ericsson/ddc/util/bin/listme | grep RBS_NODE_MODEL | sed -e 's/[@=,]/ /g' | grep KIER6  | awk '{print $6 }' | sort| uniq >  to_create_site.txt  # only sites
"""    

def main():
    try:
        f = open('to_create_site.xml', 'w')
    except ValueError as msg:
        print msg
    try:    
        f3 = open('error_creating_sites.log', 'w+')
    except ValueError as msg:
        print msg
    with open('to_create_site.txt', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        line_num = 0
        for row in reader:
            line_num += 1
            #print 'str(len(row))= ' + str(len(row))
            #print row
            if (not len(row) == 3):
                print 'The quantuty of arguments at the line number ' + str(line_num) + ' is not enouph (3)'
                f3.write('The quantuty of arguments at the line number ' + str(line_num) + ' is not enouph (3)' + '\n')
                continue
            rnc = row[0].strip().upper() # upper case and remove all spaces
            site_name= row[1].strip().upper()
            ip = row[2].strip()
            if rnc not in ('KIER1','KIER2','KIER3','KIER4','KIER5','KIER6','KIER7'):
                print "First correct argument was not found, (KIERX) I'll miss that line, line_num is " + str(line_num)
                f3.write('The quantuty of arguments at the line number ' + str(line_num) + ' is not enouph (3)' + '\n')
                #continue
            ## Header
            if line_num == 1:    
                f.write('<!DOCTYPE Model SYSTEM "/opt/ericsson/arne/etc/arne16_2.dtd">'+ '\n') 
                f.write('<Model version="1" importVersion="16.2">'+ '\n')
                f.write('  '+ '<Create>'+ '\n')
                
            #print str(line_num) + '\n '
            #print row
            if len(site_name) <> 6:
                print "Correct site was not found, I'll miss that line, line_num is " + str(line_num)
                f3.write('Correct site was not found: ' + site_name + ', I will miss that line, line_num is ' + str(line_num) + '\n')
                continue
            ## Manage Element starts create
            f.write('         ' + '<Site userLabel="' + site_name + '"/>'+ '\n') 
            f.write('            ' + '<altitude string="0"/>' + '\n')
            f.write('            ' + '<location string="All Ukraine"/>' + '\n')
            f.write('            ' + '<longitude string="0"/>' + '\n')
            f.write('            ' + '<latitude string="0"/>' + '\n')
            f.write('            ' + '<worldTimeZoneId string="Europe/Kiev"/>'+ '\n')
            f.write('            ' + '<freeText string=""/>'+ '\n')
            f.write('            ' + '<datum string="wgs84"/'+ '\n')
            f.write('         ' + '</Site>' + '\n')
    ## Stop create     
    f.write('  '+ '</Create>'+ '\n')
    f.write('</Model>'+ '\n')     
    f.close()
    f3.close()

print "to_create_site.xml file was created."
print 'For check xml file use: ' + '/opt/ericsson/arne/bin/import.sh -f /tmp/siu/to_create_site.xml -val:rall' + '\n'
print 'For start xml file use: ' + '/opt/ericsson/arne/bin/import.sh -import -f /tmp/siu/to_create_site.xml' + '\n'
print 'Check error at error log: error_creating_sites.log' + '\n'


if __name__ == '__main__':
  main()

