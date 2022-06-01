apt update && apt install -y git vim python3 python3-pip

wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz

tar zxf Downloads/geckodriver-v0.31.0-linux64.tar.gz -C /usr/local/bin
pip3 install requests selenium lxml