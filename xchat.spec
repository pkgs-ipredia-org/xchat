%define name xchat
%define version 1.6.1
%define release 2tc1
%define prefix /usr

Summary: A GTK+ IRC (chat) client

Name: %{name}
Version: %{version}
Release: %{release}
Epoch: 1
Group: Applications/Internet
Copyright: GPL
Packager: Red Hat, Inc. <http://bugzilla.redhat.com/bugzilla>
Vendor: Red Hat, Inc.

Url: http://xchat.org

Source: http://xchat.org/files/source/1.6/xchat-%{version}.tar.gz
Source1: xchat-zh_TW.po
Source2: xchat-zh_CN.po
Patch: xchat-1.6.1-mb.diff
Buildroot: /var/tmp/%{name}-%{version}-%{release}-root

%description
X-Chat is yet another IRC client for the X Window System and
GTK+. X-Chat is fairly easy to use, compared to other GTK+ IRC
clients, and the interface is quite nicely designed.

%prep

%setup
%patch -p0 -b .mb

%build
#%configure --disable-panel --disable-textfe --enable-openssl
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix} \
	--disable-panel --disable-textfe --enable-openssl
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT%{prefix}
make prefix=$RPM_BUILD_ROOT%{prefix} install-strip

# install languages by hand
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/zh_TW/LC_MESSAGES
msgfmt -o $RPM_BUILD_ROOT/usr/share/locale/zh_TW/LC_MESSAGES/xchat.mo %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT/usr/share/locale/zh_CN/LC_MESSAGES
msgfmt -o $RPM_BUILD_ROOT/usr/share/locale/zh_CN/LC_MESSAGES/xchat.mo %{SOURCE2}

%files
%defattr(-,root,root)
%doc README ChangeLog doc/xchat.sgml
%attr(755,root,root) %{prefix}/bin/xchat
%{prefix}/share/gnome/apps/Internet/xchat.desktop
%{prefix}/share/pixmaps/xchat.png
%{prefix}/share/locale/*/LC_MESSAGES/*

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Dec 8 2000 Chih-Wei Huang <cwhuang@linux.org.tw>
- add Epoch to ensure upgrade safely from RH7
- change zh_TW.Big5.po to zh_TW.po
- add --enable-openssl

* Tue Dec 5 2000 Andrew Lee <andrew@linux.org.tw>
- update to 1.6.1
- new xchat-zh_TW.Big5.po

* Sat Sep 2 2000 Anthony Fok <foka@debian.org>
- added zh_CN po file

* Thu Mar 16 2000 Chih-Wei Huang <cwhuang@linux.org.tw>
- update 1.4.1

* Sat Feb 26 2000 Andrew Lee <andrew@cle.linux.org.tw>
- add zh_TW.po
