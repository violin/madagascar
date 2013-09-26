#!/usr/bin/bash

keytab="/home/qatest/yz/study.keytab"
baseDir="/home/qatest/yz/madagascar"
src1=${baseDir}"/nginx.log"
dest1=${baseDir}"/nginx.json"
cpDest="/home/qatest/webroot-study/access-study.json"
jsonBase="/home/qatest/webroot-study/access-study"

## 0 get log

kinit -kt ${keytab} study/dev@HADOOP.HZ.NETEASE.COM
kinit -R
$HADOOP_HOME/bin/hadoop fs -text /datastream/study/nginx/$(date -d yesterday +%Y_%m_%d)/* > nginx.log

## 1 process
python ${baseDir}/logProcessor.py ${src1} ${dest1}


## 2 merge
## python ${baseDir}/resultMerger.py ${dest1} ${dest2} access-study.json

## 3 post process

python ${baseDir}/renderer.py ${dest1}

## 4 log rotate
if [ -f ${cpDest} ]
then
  cp ${cpDest} ${jsonBase}/access-study-$(date -d ' 2 days ago' +%Y_%m_%d).json
fi

cp ${dest1} ${cpDest}

## 5 clean
rm ${src1}