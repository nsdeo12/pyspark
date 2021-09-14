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
		#echo "${fileunit##*/}"
		#echo "$fileunit"
		currentFolder=$fileunit
		
		#echo $currentFolder  
		#lastModOfFolder=$(stat -c %y $currentFolder |cut -d' ' -f1)
		lastModOfFolder=$(stat -c %y $currentFolder | sed -r 's/[" ",-]//g' | cut -c1-8)
		echo "Time of last modification : $lastModOfFolder"
		#echo "Time of last access : $(stat -c %x $currentFolder )"
		#echo "Time of last modification : $(stat -c %y $currentFolder |cut -d' ' -f2)"
		#echo "Time of last change : $(stat -c %z $currentFolder)"
		#Check modified date == current date starts
			if [ $lastModOfFolder == $nowDate ]
				then
					echo "EQUAL"
					echo "inside $currentFolder  "
					#Check for .dmp file extensions starts
					#findFile= $(find $currentFolder  -iname "*dmp" -exec echo {} \);
					targetFile=$(find $currentFolder -type f -name "*dmp")
					echo "targetFile name : $targetFile"
					bname=$(basename "$targetFile")
					echo "Base Name of the target file: $bname"
					extension="${bname##*.}"
					echo "Extension of the target file: $extension"
					filenamewoext="${bname%.*}"
					echo "filename without extension : $filenamewoext"
					#newfilename="${filenamewoext}${date}.${extension}
					newfilename="$destinationFilename".${extension}
					echo "newfilename is : $newfilename"
										
						#COPY TO OUTER Directory STARTS
						cp $targetFile $dumpFilePath/${newfilename}
				
						#COPY TO OUTER Directory ENDS

					#Check for .dmp file extensions ends					
			else
				echo "NOT EQUAL"
			fi
			

		#Check modified date == current date ends
	done
	
	
#List files in folder ends

#/d/pySpark/ShellScript/Tallyman/dumps/driving/2020-07-12_14-00-01

#access						 2020-07-16 19:50:10.456663100 +0530
 #Time of last modification : 2020-07-16 19:50:10.456663100 +0530
#Time of last change : 		 2020-07-17 09:18:29.706258100 +0530

#/d/pySpark/ShellScript/Tallyman/dumps/driving/2020-07-13_14-00-00
#Time of last access :       2020-07-16 19:50:10.475675700 +0530
#Time of last modification : 2020-07-16 19:50:10.475675700 +0530
#Time of last change :       2020-07-16 19:50:10.475675700 +0530


echo "----------------------------------------------------------------------------------"
echo"////////////////////////////////////////////////////////////////////////////////
////////////////STARTING DUMP COLLECTION SCRIPT/////////////////////////////////
////////////////////////////////////////////////////////////////////////////////"