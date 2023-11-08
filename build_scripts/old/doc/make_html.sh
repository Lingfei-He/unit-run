script_dir=$(dirname $0)
work_dir=$(dirname $(dirname $script_dir))
cd $work_dir
cd doc
jupyter-book build --all ./ # all 
read