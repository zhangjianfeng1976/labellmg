# ex: set ts=8 noet:

all: qt5

test:
	pytest

qt4: qt4py2

qt5: qt5py3

qt4py2:
	pyrcc4 -py2 -o src/labelImg/resources.py resources.qrc

qt4py3:
	pyrcc4 -py3 -o src/labelImg/resources.py resources.qrc

qt5py3:
	pyrcc5 -o src/labelImg/resources.py resources.qrc

clean:
	rm -f ~/.labelImgSettings.pkl resources.pyc

.PHONY: test
