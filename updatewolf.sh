install(){
    echo Installing
    git clone https://www.github.com/Hiyoteam/Little_Wolf
    ./Little_wolf
    chmod 777 *
    nohup python3 main.py &
}
update(){
    echo Updating
    cp config.py /tmp/config.py
    cd ..
    rm -rf ./Little_Wolf
    git clone https://www.github.com/Hiyoteam/Little_Wolf
    cd ./Little_Wolf
    cp /tmp/config.py config.py
    chmod 777 *
    nohup python3 main.py &
}
testifinstall=$(pwd|grep Little_Wolf)
if [[ "$testifinstall" != "" ]]
then 
    echo Installed
    update
else
    echo NotFound
    install
fi
