work_dir=$(dirname $(dirname $(dirname $0)))
cd $work_dir
rm ./dist/*
python -m build