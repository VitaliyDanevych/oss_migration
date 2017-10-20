#!/usr/bin/bash

echo "start!"
wdir=/home/fmuser2/scripts/oss_migration

if [ $# -eq 0 ]; then
        echo "The script run without parameters! Put RNC_NAME (KIERX) as a parameter!"
        exit 1
fi


echo "removing old files"
#rm -f ${wdir}/rnc_list_of_sites.txt
#rm -f ${wdir}/to_create_site.txt
cd ${wdir}
rm -f *.txt
rm -f *.xml
rm -f *.log

echo "script has been started to work at" `date` > ${wdir}/script.log

echo "The to_create_RBSGroup.py needed the file rnc_list_of_sites.txt"
echo "The to_create_sites.py needed the file to_create_site.txt"

echo "generating that files..."
/opt/ericsson/ddc/util/bin/listme | grep RBS_NODE_MODEL | sed -e 's/[@=,]/ /g' | grep $1  | awk '{print $4 ";" $6 ";" $7 }' | sort| uniq > ${wdir}/rnc_list_of_sites.txt
cp -p ${wdir}/rnc_list_of_sites.txt ${wdir}/to_create_site.txt
echo "Done"


echo "starting first python module"
echo "start creation a sites file"
python ${wdir}/to_create_sites.py 


echo "starting second python module"
echo "start creation RBSGroup file"
python ${wdir}/to_create_RBSGroup.py 


echo "exporting of whole network to xml file...".
echo "it takes a few minutes. you could drink a cup of cofee while it is proccessing :) ...."
cd ${wdir}/
/opt/ericsson/arne/bin/export.sh -f whole_network_exported.xml -o -noTss > /dev/null 2>&1
echo "extract only $1 RNC to $1.xml file..."
/opt/ericsson/arne/modeltrans/bin/searchManagedElementById.sh whole_network_exported.xml $1 to_create_RNC_$1.xml
echo "to_create_RNC_$1.xml file was created."
echo "For check xml file use: /opt/ericsson/arne/bin/import.sh -f ${wdir}/to_create_RNC_${1}.xml -val:rall"
echo "For start xml file use: /opt/ericsson/arne/bin/import.sh -import -f ${wdir}/to_create_RNC_${1}.xml"
	

echo "finish!!!" 
echo "script has been finished to work at" `date` >> ${wdir}/script.log
