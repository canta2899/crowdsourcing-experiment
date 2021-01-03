#!/bin/sh

echo "Creating folder: tasks/${1}/${2}/deploy";
mkdir -p "tasks/${1}/${2}/deploy";
echo "Creating folder: tasks/${1}/${2}/mturk";
mkdir -p "tasks/${1}/${2}/mturk";
# shellcheck disable=SC2039
if [ "${5}" == "allow-config" ]
then
echo "Creating folder: tasks/${1}/${2}/task";
mkdir -p "tasks/${1}/${2}/task";
fi
echo "Building task ${1}/${2}";
ng build --prod --output-hashing=none \
&& cat ../dist/CrowdsourcingSkeleton/polyfills-es2015.js ../dist/CrowdsourcingSkeleton/runtime-es2015.js ../dist/CrowdsourcingSkeleton/main-es2015.js > build/deploy/scripts.js  \
&& cat ../dist/CrowdsourcingSkeleton/styles.css > build/deploy/styles.css \
&& cat build/deploy/scripts.js > "tasks/${1}/${2}/deploy/scripts.js" \
&& cat build/deploy/styles.css > "tasks/${1}/${2}/deploy/styles.css" \
&& cat build/deploy/index.html > "tasks/${1}/${2}/deploy/index.html" \
&& cat build/admin.json > "tasks/admin.json" \
&& cat build/task/workers.json > "tasks/${1}/${2}/task/workers.json" \
&& cat build/mturk/tokens.csv > "tasks/${1}/${2}/mturk/tokens.csv" \
&& cat build/mturk/index.html > "tasks/${1}/${2}/mturk/index.html";
# shellcheck disable=SC2039
if [ "${5}" == "allow-config" ]
then
cat build/task/dimensions.json > "tasks/${1}/${2}/task/dimensions.json";
cat build/task/hits.json > "tasks/${1}/${2}/task/hits.json";
cat build/task/instructions_main.json > "tasks/${1}/${2}/task/instructions_main.json";
cat build/task/instructions_dimensions.json > "tasks/${1}/${2}/task/instructions_dimensions.json";
cat build/task/questionnaires.json > "tasks/${1}/${2}/task/questionnaires.json";
cat build/task/search_engine.json > "tasks/${1}/${2}/task/search_engine.json";
cat build/task/task.json > "tasks/${1}/${2}/task/task.json";
cat build/task/workers.json > "tasks/${1}/${2}/task/workers.json";
fi
echo "Build completed";
echo "Deploying task ${1}/${2}";
aws s3api put-object     --bucket "${3}" --key "admin.json"                                   --body "tasks/admin.json"                                    --content-type application/json       ;
if [ "${5}" == "allow-config" ]
then
echo "Uploading configuration to folder: ${3}/Task/";
aws s3api put-object     --bucket "${3}" --key "${1}/${2}/Task/dimensions.json"               --body "tasks/${1}/${2}/task/dimensions.json"                --content-type application/json       ;
aws s3api put-object     --bucket "${3}" --key "${1}/${2}/Task/hits.json"                     --body "tasks/${1}/${2}/task/hits.json"                      --content-type application/json       ;
aws s3api put-object     --bucket "${3}" --key "${1}/${2}/Task/instructions_main.json"        --body "tasks/${1}/${2}/task/instructions_main.json"         --content-type application/json       ;
aws s3api put-object     --bucket "${3}" --key "${1}/${2}/Task/instructions_dimensions.json"  --body "tasks/${1}/${2}/task/instructions_dimensions.json"   --content-type application/json       ;
aws s3api put-object     --bucket "${3}" --key "${1}/${2}/Task/questionnaires.json"           --body "tasks/${1}/${2}/task/questionnaires.json"            --content-type application/json       ;
aws s3api put-object     --bucket "${3}" --key "${1}/${2}/Task/search_engine.json"            --body "tasks/${1}/${2}/task/search_engine.json"             --content-type application/json       ;
aws s3api put-object     --bucket "${3}" --key "${1}/${2}/Task/task.json"                     --body "tasks/${1}/${2}/task/task.json"                      --content-type application/json       ;
aws s3api put-object     --bucket "${3}" --key "${1}/${2}/Task/workers.json"                  --body "tasks/${1}/${2}/task/workers.json"                   --content-type application/json       ;
fi
echo "Uploading task source files to folder: ${4}/";
aws s3api put-object     --bucket "${4}" --key "${1}/${2}/styles.css"                         --body "tasks/${1}/${2}/deploy/styles.css"                   --content-type text/css               &&
aws s3api put-object-acl --bucket "${4}" --key "${1}/${2}/styles.css"                         --acl public-read                                                                                  ;
aws s3api put-object     --bucket "${4}" --key "${1}/${2}/scripts.js"                         --body "tasks/${1}/${2}/deploy/scripts.js"                   --content-type application/javascript &&
aws s3api put-object-acl --bucket "${4}" --key "${1}/${2}/scripts.js"                         --acl public-read                                                                                  ;
aws s3api put-object     --bucket "${4}" --key "${1}/${2}/index.html"                         --body "tasks/${1}/${2}/deploy/index.html"                   --content-type text/html              &&
aws s3api put-object-acl --bucket "${4}" --key "${1}/${2}/index.html"                         --acl public-read                                                                                  ;
echo "Upload completed";
python -m webbrowser https://sc-cs-deploy.s3.eu-south-1.amazonaws.com/ProgettoSocialComputing2/Batch1/index.html
