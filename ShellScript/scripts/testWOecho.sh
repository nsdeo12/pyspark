###############.
###############
#
#!/bin/bash
echo "////////////////////////////////////////////////////////////////////////////////
////////////////STARTING DUMP COLLECTION SCRIPT/////////////////////////////////
////////////////////////////////////////////////////////////////////////////////"
echo "-------------------------------------------------------------------------------\r"

#Find current dire and today
echo "Current Directory>>"$(pwd)
nowDate=$(date +"%Y%m%d")
echo "Today is >>" $nowDate
echo "Modified Date >>" 
parentDir=$(dirname $(pwd))
echo "parentDir>>" $parentDir
destinationFilename="Tallyman_SANUK_Dump_Driving"
dumpFilePath="$parentDir/Tallyman/dumps/driving"
echo "dump path>>"$dumpFilePath
#List files in folder starts

for fileunit in "$dumpFilePath"/*
	do
	if [[ -d $fileunit ]]; then
		echo "$fileunit is a directory"
	elif [[ -f $fileunit ]]; then
		echo "$fileunit is a file"
	else
		echo "$fileunit is not valid"
    exit 1
fi
	done
if [ 20200719 -eq 20200719 ];
then
	echo "Equal"
fi
	
echo ">>>>O-V-E-R>>>>"