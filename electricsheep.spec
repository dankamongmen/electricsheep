Summary: collaborative screen-saver
Name: electricsheep
Version: 2.7b12
Release: 1
License: GPL
Group: Graphics
Source: http://electricsheep.org/electricsheep-2.7b12.tar.gz
Url: http://electricsheep.org
Packager: Scott Draves <rpm@electricsheep.org>
Requires: xscreensaver, expat, curl
%description

Electric Sheep is a screen-saver that realizes the collective dream of
sleeping computers from all over the internet.

%prep
%setup
./configure

%build
make

%install
make install

%undefine	__check_files

%files
/usr/local/bin/electricsheep
/usr/local/bin/electricsheep-voter
/usr/local/bin/flam3-animate
/usr/local/bin/mpeg2dec_onroot 
/usr/local/share/electricsheep/electricsheep-smile.png
/usr/local/share/electricsheep/electricsheep-frown.png
/usr/share/control-center/screensavers/electricsheep.xml
/usr/local/man/man1/electricsheep.1
