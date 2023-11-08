script_dir=$(dirname $0)
work_dir=$(dirname $(dirname $(dirname $0)))
cd $work_dir
sh $script_dir/build.sh
whl_path=$(ls dist/*.whl)
pip install --no-index $whl_path --force-reinstall
sleep 10