#/bin/bash

# This script build the zip file containing the whole assignment

DIR_NAME="cantarutti_bombasseidebona_zanatta_fase_1"

if [ -d "$DIR_NAME" ]; then
        rm -r $DIR_NAME
fi

mkdir $DIR_NAME

cp -r ../framework $DIR_NAME 
cp -r ../pyDistribution $DIR_NAME
cp -r ../pyHITS $DIR_NAME
cp -r report.pdf $DIR_NAME/RelazioneFase1.pdf
echo "node_modules folder not included.\nLaunch yarn install to download all the modules needed" > $DIR_NAME/framework/readme.txt
 
zip "$DIR_NAME.zip" $DIR_NAME -x "*node_modules*" -r 
