script_dir=$(dirname $0)
work_dir=$(dirname $(dirname $script_dir))
cd $work_dir
cd doc
rm -rf source/api
sphinx-apidoc -o source/api ../src/ -f -e 