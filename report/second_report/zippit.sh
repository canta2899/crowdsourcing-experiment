#/bin/bash

# This script build the zip file containing the whole assignment

DIR_NAME="cantarutti_bombasseidebona_zanatta_fase_2"

if [ -d "$DIR_NAME" ]; then
        rm -r $DIR_NAME
fi

mkdir $DIR_NAME

cp -r ../../pyAnalysis $DIR_NAME
cp -r ../../Data $DIR_NAME
cp -r report.pdf $DIR_NAME/RelazioneFase2.pdf
 
zip "$DIR_NAME.zip" $DIR_NAME -r 
