#!/bin/sh

pip install --upgrade virtualenv

# clone labelimg source
rm -rf /tmp/labelImgSetup
mkdir /tmp/labelImgSetup
cd /tmp/labelImgSetup
curl https://codeload.github.com/tzutalin/labelImg/zip/master --output labelImg.zip
unzip labelImg.zip
rm labelImg.zip

# setup python3 space
virtualenv --system-site-packages  -p python3 /tmp/labelImgSetup/labelImg-py3
source /tmp/labelImgSetup/labelImg-py3/bin/activate
cd labelImg-master

# build labelImg app
pip3 install py2app
pip3 install PyQt5 lxml
make qt5py3
rm -rf build dist
python3 setup.py py2app -A
mv "/tmp/labelImgSetup/labelImg-master/dist/labelImg.app" /Applications
# deactivate python3
deactivate
cd ../
rm -rf /tmp/labelImgSetup
echo 'DONE'
