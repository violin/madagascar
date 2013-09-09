#!/usr/bin/bash

baseDir="/home/study/rsync-production-logs"
src1=${baseDir}"/1/access-study.log.1"
src2=${baseDir}"/2/access-study.log.1"
dest1=${baseDir}"/1/access-study.json"
dest2=${baseDir}"/2/access-study.json"
cpDest="/home/study/webroot-study/log-processed"

## 1 process
python ${baseDir}/scripts/logProcessor.py ${src1} ${dest1} 

python ${baseDir}/scripts/logProcessor.py ${src2} ${dest2}

## 2 merge
python ${baseDir}/scripts/resultMerger.py ${dest1} ${dest2} access-study.json

## 3 post process

python ${baseDir}/scripts/renderer.py access-study.json

cp access-study.json ${cpDest}
