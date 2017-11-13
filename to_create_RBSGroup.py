#  #!/usr/bin/env python
__AUTHOR__='Danevych V.'
__COPYRIGHT__='Danevych V. 2017 Kiev, Ukraine'
#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import csv

    
def main():
    try:
        f = open('to_create_RBSGroup.xml', 'w+')
    except ValueError as msg:
        print msg
    try:    
        f3 = open('error_RBSGroup.log', 'w+')
    except ValueError as msg:
        print msg
    with open('rnc_list_of_sites.txt', 'rb') as csvfile:
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
            if rnc not in ('KITR1','KIER1','KIER2','KIER3','KIER4','KIER5','KIER6','KIER7'):
                print "First correct argument was not found, (KIERX) I'll miss that line, line_num is " + str(line_num)
                f3.write('The quantuty of arguments at the line number ' + str(line_num) + ' is not enouph (3)' + '\n')
                #continue
            ## Header
            if line_num == 1:
                f.write('<!DOCTYPE Model SYSTEM "/opt/ericsson/arne/etc/arne17_0.dtd">'+ '\n') 
                #f.write('<!DOCTYPE Model SYSTEM "/opt/ericsson/arne/etc/arne16_2.dtd">'+ '\n') 
                #f.write('<Model version="1" importVersion="16.2">'+ '\n')
                f.write('<Model version="1" importVersion="17.0">'+ '\n')
                f.write('  '+ '<Create>'+ '\n')
                ## Subnetwork start here
                f.write('	  '+ '<SubNetwork userLabel="'+ rnc +'" networkType="IPRAN">'+ '\n')
                f.write('	  '+ '<Group userLabel="RBSGroup" groupType="RBSGroup" networkType="WCDMA"></Group>'+ '\n')
            #print row
            if len(site_name) <> 6:
                print "Correct site was not found, I'll miss that line, line_num is " + str(line_num)
                f3.write('Correct site was not found: ' + site_name + ', I will miss that line, line_num is ' + str(line_num) + '\n')
                continue
            ## Manage Element starts create
            f.write('	  '+ '<ManagedElement sourceType="CELLO">'+ '\n')
            f.write('            '+ '<ManagedElementId string="' + site_name + '"/>'+ '\n')
            f.write('            '+ '<primaryType type="RBS"/>'+ '\n')
            f.write('            '+ '<managedElementType types=""/>'+ '\n')
            f.write('            '+ '<associatedSite string="Site=' + site_name + '"/>'+ '\n')
            f.write('            '+ '<nodeVersion string=""/>'+ '\n')
            f.write('            '+ '<platformVersion string=""/>'+ '\n')
            f.write('            '+ '<swVersion string=""/>'+ '\n')
            f.write('            '+ '<vendorName string="Ericsson"/>'+ '\n')
            f.write('            '+ '<userDefinedState string=""/>'+ '\n')
            f.write('            '+ '<managedServiceAvailability int="1"/>'+ '\n')
            f.write('            '+ '<isManaged boolean="true"/>'+ '\n')
            f.write('            '+ '<neMIMVersion string="U.3.1"/>'+ '\n')
            f.write('            '+ '<connectionStatus string="ON"/>'+ '\n')
            f.write('            '+ '<ManagedFunction>'+ '\n')
            f.write('               '+ '<functionType string="NodeB"/>'+ '\n')
            f.write('               '+ '<supportSystemControl boolean="true"/>'+ '\n')
            f.write('            '+ '</ManagedFunction>'+ '\n')
            ## Connectivity
            f.write('            '+ '<Connectivity>'+ '\n') 
            ## Default start
            f.write('               '+ '<DEFAULT>'+ '\n')
            f.write('                  '+ '<emUrl url="http://' + ip +':80/em/index.html"/>'+ '\n')
            f.write('                  '+ '<ipAddress string="' + ip + '"/>' + '\n')
            f.write('                  '+ '<oldIpAddress string=""/>' + '\n')
            f.write('                  '+ '<hostname string="' + site_name + '"/>' + '\n')
            f.write('                  '+ '<nodeSecurityState state="ON"/>' + '\n')
            f.write('                  '+ '<boardId string=""/>' + '\n')
            ## Protocol 0
            f.write('                  '+ '<Protocol number="0">' + '\n')
            f.write('                     '+ '<protocolType string="CORBA"/>' + '\n')
            f.write('                     '+ '<port int="0"/>' + '\n')
            f.write('                     '+ '<protocolVersion string="v3.2"/>' + '\n')
            f.write('                     '+ '<securityName string=""/>' + '\n')
            f.write('                     '+ '<authenticationMethod string=""/>' + '\n')
            f.write('                     '+ '<encryptionMethod string=""/>' + '\n')
            f.write('                     '+ '<communityString string=""/>' + '\n')
            f.write('                     '+ '<context string=""/>' + '\n')
            f.write('                     '+ '<namingUrl string="http://' + ip + ':80/cello/ior_files/nameroot.ior"/>' + '\n')
            f.write('                     '+ '<namingPort int="0"/>' + '\n')
            f.write('                     '+ '<notificationIRPAgentVersion string="3.2"/>' + '\n')
            f.write('                     '+ '<alarmIRPAgentVersion string="3.2"/>' + '\n')
            f.write('                     '+ '<notificationIRPNamingContext context="NOTIFICATION_IRP_VERSION_1_1"/>' + '\n')
            f.write('                     '+ '<alarmIRPNamingContext context="ALARM_IRP_VERSION_1_1"/>' + '\n')
            f.write('                  '+ '</Protocol>' + '\n')
            ## Protocol 1
            f.write('                  '+ '<Protocol number="1">' + '\n')
            f.write('                     '+ '<protocolType string="TELNET"/>' + '\n')
            f.write('                     '+ '<port int="23"/>' + '\n')
            f.write('                     '+ '<protocolVersion string="v2"/>' + '\n')
            f.write('                     '+ '<securityName string=""/>' + '\n')
            f.write('                     '+ '<authenticationMethod string=""/>' + '\n')
            f.write('                     '+ '<encryptionMethod string=""/>' + '\n')
            f.write('                     '+ '<communityString string=""/>' + '\n')
            f.write('                     '+ '<context string=""/>' + '\n')
            f.write('                     '+ '<namingUrl string=""/>' + '\n')
            f.write('                     '+ '<namingPort int=""/>' + '\n')
            f.write('                     '+ '<notificationIRPAgentVersion string=""/>' + '\n')
            f.write('                     '+ '<alarmIRPAgentVersion string=""/>' + '\n')
            f.write('                     '+ '<notificationIRPNamingContext context=""/>' + '\n')
            f.write('                     '+ '<alarmIRPNamingContext context=""/>' + '\n')
            f.write('                  '+ '</Protocol>' + '\n')
            ## Browser
            f.write('                  '+ '<Browser>' + '\n')
            f.write('                     '+ '<browser string=""/>' + '\n')
            f.write('                     '+ '<browserURL string=""/>' + '\n')
            f.write('                     '+ '<bookname string=""/>' + '\n')
            f.write('                  '+ '</Browser>' + '\n')
            ## Default end
            f.write('               '+ '</DEFAULT>' + '\n')
            ## Connectivity end
            f.write('            '+ '</Connectivity>'+ '\n')
            # TSS start
            f.write('            '+ '<Tss>'+ '\n') 
            ## Entry NORMAL
            f.write('               '+ '<Entry>' + '\n')
            f.write('                  '+ '<System string="' + site_name + '"/>' + '\n')
            f.write('                  '+ '<Type string="NORMAL"/>' + '\n')
            f.write('                  '+ '<User string="rbs"/>' + '\n')
            f.write('                  '+ '<Password string="rbs"/>' + '\n')
            f.write('               '+ '</Entry>' + '\n')
            ## Entry SECURE
            f.write('               '+ '<Entry>' + '\n')
            f.write('                  '+ '<System string="' + site_name + '"/>' + '\n')
            f.write('                  '+ '<Type string="SECURE"/>' + '\n')
            f.write('                  '+ '<User string="rbs"/>' + '\n')
            f.write('                  '+ '<Password string="rbs"/>' + '\n')
            f.write('               '+ '</Entry>' + '\n')
            # TSS end
            f.write('            '+ '</Tss>'+ '\n')
            ## Relationship start
            f.write('            '+ '<Relationship>'+ '\n')
            #f.write('               '+ '<AssociableNode TO_FDN="FtpServer=SMRSSLAVE-WRAN-ki2nedss,FtpService=w-back-ki2nedss" AssociationType="ManagedElement_to_ftpBackupStore"/>'+ '\n')
            f.write('               '+ '<AssociableNode TO_FDN="FtpServer=SMRSSLAVE-WRAN-dn2nedss,FtpService=w-back-dn2nedss" AssociationType="ManagedElement_to_ftpBackupStore"/>'+ '\n')
            #f.write('               '+ '<AssociableNode TO_FDN="FtpServer=SMRSSLAVE-WRAN-ki2nedss,FtpService=w-key-ki2nedss" AssociationType="ManagedElement_to_ftpLicenseKeyStore"/>'+ '\n') 
            f.write('               '+ '<AssociableNode TO_FDN="FtpServer=SMRSSLAVE-WRAN-dn2nedss,FtpService=w-key-dn2nedss" AssociationType="ManagedElement_to_ftpLicenseKeyStore"/>'+ '\n') 
            #f.write('               '+ '<AssociableNode TO_FDN="FtpServer=SMRSSLAVE-WRAN-ki2nedss,FtpService=w-sws-ki2nedss" AssociationType="ManagedElement_to_ftpSwStore"/>'+ '\n')
            f.write('               '+ '<AssociableNode TO_FDN="FtpServer=SMRSSLAVE-WRAN-dn2nedss,FtpService=w-sws-dn2nedss" AssociationType="ManagedElement_to_ftpSwStore"/>'+ '\n')
            f.write('               '+ '<AssociableNode TO_FDN="ManagementNode=ONRM" AssociationType="MgmtAssociation"/>'+ '\n')
            f.write('               '+ '<AssociableNode TO_FDN="SubNetwork=' + rnc + ',Group=RBSGroup" AssociationType="Group_to_MeContext"/>'+ '\n')
            ## Relationship end
            f.write('            '+ '/<Relationship>'+ '\n')
            ## Manage Element ends here
            f.write('	  '+ '</ManagedElement>'+ '\n')
  
  
    ## Stop create
    ## Subnetwork ends here
    f.write('	 '+ '</SubNetwork>'+ '\n')
    f.write('  '+ '</Create>'+ '\n')
    f.write('</Model>'+ '\n')     
    f.close()
    f#2.close()
    f3.close()

    print "to_create_RBSGroup.xml file was created."
    print 'For check xml file use: ' + '/opt/ericsson/arne/bin/import.sh -f /home/fmuser2/scripts/oss_migration/to_create_RBSGroup.xml -val:rall' + '\n'
    print 'For start xml file use: ' + '/opt/ericsson/arne/bin/import.sh -import -f /home/fmuser2/scripts/oss_migration/to_create_RBSGroup.xml' + '\n'
    print 'Check error at error log: error_RBSGroup.log' + '\n'


if __name__ == '__main__':
  main()


