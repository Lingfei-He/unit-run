doc_dir=$(dirname $(dirname $(dirname $0)))/doc
# echo $doc_dir
cd $doc_dir
jb build . --all
sleep 3