Summary: A GTK+ IRC (chat) client.
Name: xchat
Version: 1.8.1
Release: 2
Epoch: 1
Group: Applications/Internet
License: GPL
Url: http://xchat.org
Source: http://xchat.org/files/source/1.4/xchat-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-root

Patch4: xchat-1.8.1-konqueror.patch
Patch5: xchat-1.8.1-kanjiconv-fix.patch

BuildRequires: gnome-libs

%description
X-Chat is yet another IRC client for the X Window System and
GTK+. X-Chat is fairly easy to use, compared to other GTK+ IRC
clients, and the interface is quite nicely designed.

Install xchat if you need an IRC client for X.

%prep
%setup -q

%patch4 -p1 -b .konqueror
%patch5 -p1 -b .kanjiconv

%build
%configure --disable-panel --disable-textfe --enable-japanese-conv
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
%makeinstall

%find_lang %name

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog doc/xchat.sgml doc/*.html scripts-python scripts-perl
%{_bindir}/xchat
%{_datadir}/gnome/apps/Internet/xchat.desktop
%{_datadir}/pixmaps/*

%clean
rm -r $RPM_BUILD_ROOT

%changelog
* Fri Jul 13 2001 Akira TAGOH <tagoh@redhat.com> 1.8.1-2
- fixed check locale.
- don't save kanji_conv.
  always check locale. however anyone can change the option from
  the settings menu.

* Thu Jul 12 2001 Havoc Pennington <hp@redhat.com>
- upgrade to 1.8.1
- remove autoconnect patch since it's upstream
- remove japanese patch, upstream seems to have applied
  parts of it and changelog says there's upstream support.
  (this patch was pretty huge to maintain in an SRPM anyway...)
- put scripts-python scripts-perl in docs bug #28521
- remove patch to include locale.h, gone upstream
- upgrade konqueror patch

* Thu Jul 12 2001 Havoc Pennington <hp@redhat.com>
- nevermind, BuildRequires gnome-libs, that should 
  close #48923

* Thu Jul 12 2001 Havoc Pennington <hp@redhat.com>
- fix file list to not include absolute path "/usr/share/..."
  no idea how that ever worked at all. closes #48923

* Mon Jun 25 2001 Karsten Hopp <karsten@redhat.de>
- use konqueror, not kfmclient on URLs

* Fri Feb 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- langify
- use %%{_tmppath}
- make it compile

* Tue Feb 13 2001 Akira TAGOH <tagoh@redhat.com>
- Added Japanese patch.

* Tue Feb 13 2001 Havoc Pennington <hp@redhat.com>
- patch that may fix autoconnections (bug 27093)

* Mon Jan 22 2001 Havoc Pennington <hp@redhat.com>
- 1.6.3
- remove patch to desktop file (Internet->Application), seems to 
  have gone upstream

* Sat Dec 9 2000 Havoc Pennington <hp@redhat.com>
- Remove security fix which has been merged upstream
- upgrade to 1.6.1

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
