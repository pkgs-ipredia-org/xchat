%define name xchat
%define prefix /usr

Summary: A GTK+ IRC (chat) client.

Name: %{name}
Version: 1.4.2
Release: 6j1
Epoch: 1
Group: Applications/Internet
Copyright: GPL

Url: http://xchat.org

Source: http://xchat.org/files/source/1.4/xchat-%{version}.tar.gz
Patch: xchat-1.4.2-fixed.patch
Patch1: xchat-1.4.2-nourltoshell.patch
Patch10: xchat-1.4.2-ja.patch
Buildroot: /var/tmp/%{name}-%{version}-%{release}-root

%description
X-Chat is yet another IRC client for the X Window System and
GTK+. X-Chat is fairly easy to use, compared to other GTK+ IRC
clients, and the interface is quite nicely designed.

Install xchat if you need an IRC client for X.

%prep
%setup -q
# fix desktop entry
%patch -p1 -b .fixed
%patch1 -p1 -b .nourltoshell

%patch10 -p1 -b .ja

%build
%configure --disable-panel --disable-textfe \
--enable-japanese-conv --enable-nls
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
%makeinstall

%files
%defattr(-,root,root)
%doc README ChangeLog doc/xchat.sgml doc/*.html
%attr(755,root,root) %{prefix}/bin/xchat
%{prefix}/share/gnome/apps/Internet/xchat.desktop
%{prefix}/share/pixmaps/xchat.png
%{prefix}/share/locale/*/*/*

%clean
rm -r $RPM_BUILD_ROOT

%changelog
* Fri Aug 25 2000 Satoru Sato <ssato@redhat.com>
- apply nls patch(from xchat-ja debian package)

* Sat Aug 19 2000 Havoc Pennington <hp@redhat.com>
- Don't use /bin/sh to interpret URLs from the net

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Updated Epoch

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Havoc Pennington <hp@redhat.com>
- Install HTML docs

* Fri Jun 16 2000 Preston Brown <pbrown@redhat.com>
- fix desktop entry

* Fri May 19 2000 Havoc Pennington <hp@redhat.com>
- rebuild for the Winston tree, update to 1.4.2
