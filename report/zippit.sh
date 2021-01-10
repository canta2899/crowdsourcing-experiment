#/bin/bash

# This script build the zip file containing the whole assignment

DIR_NAME="cantarutti_bombasseidebona_zanatta_fase_1"

if [ -d "$DIR_NAME" ]; then
        rm -r $DIR_NAME
fi

mkdir $DIR_NAME

cp ../framework $DIR_NAME -r 
cp ../pyDistribution $DIR_NAME -r 
cp ../pyHITS $DIR_NAME -r
cp report.pdf $DIR_NAME -r
 
zip "$DIR_NAME.zip" $DIR_NAME -x "*node_modules*" -r 
