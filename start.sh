#!/usr/bin/bash

echo "start!"
wdir=/home/fmuser2/scripts/oss_migration

if [ $# -eq 0 ]; then
        echo "The script run without parameters! Put RNC_NAME (KIERX) as a parameter!"
        exit 1
fi

print $1 

echo "removing old files"
rm ${wdir}/rnc_list_of_sites.txt
rm ${wdir}/to_create_site.txt
cd ${wdir}
rm *.xml

echo "The to_create_RBSGroup.py needed the file rnc_list_of_sites.txt"
echo "The to_create_sites.py needed the file to_create_site.txt"

echo "generating that files..."
/opt/ericsson/ddc/util/bin/listme | grep RBS_NODE_MODEL | sed -e 's/[@=,]/ /g' | grep $1  | awk '{print $4 ";" $6 ";" $7 }' | sort| uniq > ${wdir}/rnc_list_of_sites.txt
cp -p ${wdir}/rnc_list_of_sites.txt ${wdir}/to_create_site.txt
echo "Done"

echo "script has been started to work at" `date` > ${wdir}/script.log

echo "starting first python module"
echo "start creation a sites file"
python ${wdir}/to_create_sites.py 

echo "starting second python module"
echo "start creation RBSGroup file"
python ${wdir}/to_create_RBSGroup.py 

#echo "starting third python module"
#start parsing e_tilt data for Atoll
#python ${wdir}/3.py 

echo "finish!!!" 
echo "script has been finished to work at" `date` >> ${wdir}/script.log