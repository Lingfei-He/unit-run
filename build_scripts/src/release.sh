work_dir=$(dirname $(dirname $(dirname $0)))
cd $work_dir
py -m twine upload --repository pypi dist/*
sleep 3