CWD=$(pwd)
GIT_RESTORE_MTIME="../git-restore-mtime"

curl "https://raw.githubusercontent.com/MestreLion/git-tools/main/git-restore-mtime" > $GIT_RESTORE_MTIME
chmod +x $GIT_RESTORE_MTIME
$GIT_RESTORE_MTIME

pip3 install -r requirements.txt

cd plugins

for plugin in $(ls)
do
    pip3 install -Ue ./$plugin
done

cd $CWD

python3 -m mkdocs build