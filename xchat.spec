Summary: A GTK+ IRC (chat) client.
Name: xchat
Version: 1.8.8
Release: 5
Epoch: 1
Group: Applications/Internet
License: GPL
URL: http://www.xchat.org
Source: http://www.xchat.org/files/source/1.8/xchat-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-root

Patch4: xchat-1.8.1-konqueror.patch
Patch5: xchat-1.8.4-fix-USE_GNOME.patch
Patch6: xchat-1.8.7-use-sysconf-to-detect-cpus.patch

BuildRequires: gnome-libs

%description
X-Chat is an IRC client for the X Window System and GTK+. X-Chat is
fairly easy to use and includes a nice interface.

%prep
%setup -q

%patch5 -p0 -b .fix-USE_GNOME
%patch6 -p0 -b .use-sysconf-to-detect-cpus

%build
%configure --disable-panel --disable-textfe --enable-japanese-conv \
           --enable-openssl --enable-ipv6

make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
#%if %{WithoutGNOME}
#mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Internet $RPM_BUILD_ROOT%{_datadir}/pixmaps
#install -m 644 xchat.desktop $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Internet
#install -m 644 xchat.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
#%endif

%find_lang %name

%files -f %{name}.lang
%defattr(-,root,root)
%doc README ChangeLog doc/xchat.sgml doc/*.html scripts-python scripts-perl
%{_bindir}/xchat
#%if %{WithoutGNOME}
#%{_sysconfdir}/X11/applnk/Internet/xchat.desktop
#%else
%{_datadir}/gnome/apps/Internet/xchat.desktop
#%endif
%{_datadir}/pixmaps/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Apr  8 2002 Mike A. Harris <mharris@redhat.com> 1.8.8-5
- Re-enabled GNOME support due to user complaints of pixmaps missing, key
  bindings, and other fairly important features no longer working.

* Tue Mar 27 2002 Mike A. Harris <mharris@redhat.com> 1.8.8-4
- Disabled GNOME support since it doesn't seem too useful anyways, and forces
  all xchat users to install GNOME libs even if they use KDE. (#59626)
- Updated URL and source lines in spec.

* Wed Mar  6 2002 Mike A. Harris <mharris@redhat.com> 1.8.8-1
- Updated to xchat 1.8.8

* Tue Feb 26 2002 Mike A. Harris <mharris@redhat.com> 1.8.7-6
- Built in new buildroot

* Tue Feb  5 2002 Mike A. Harris <mharris@redhat.com> 1.8.7-5
- Added xchat-1.8.7-use-sysconf-to-detect-cpus.patch to use glibc's sysconf()
  to detect the number of processors available.

* Mon Feb  4 2002 Mike A. Harris <mharris@redhat.com> 1.8.7-4
- Enabled IPv6 support as per the request for enhancement (#52124)

* Thu Jan 24 2002 Mike A. Harris <mharris@redhat.com> 1.8.7-3
- Rebuilt in new build environment

* Thu Jan 10 2002 Mike A. Harris <mharris@redhat.com> 1.8.7-2
- Updated to xchat 1.8.7
- New release fixes security vulnerability in CTCP reply
- Built erratum for all supported releases (1.8.7-1.62.0, 1.8.7-1.70.0,
  1.8.7-1.71.0, 1.8.7-1.72.0)
- Removed konqueror patch as it is integrated now.

* Sat Jan  5 2002 Mike A. Harris <mharris@redhat.com> 1.8.6-2
- Enabled ssl support with --enable-openssl
- Also built releases 1.72.0, 1.71.0, 1.70.0, 1.62.0 for erratum release

* Mon Dec 10 2001 Mike A. Harris <mharris@redhat.com> 1.8.6-1
- Updated to xchat 1.8.6

* Tue Nov 13 2001 Mike A. Harris <mharris@redhat.com> 1.8.5-1
- Updated to xchat 1.8.5
- Added f to rm -r in install and clean sections

* Sun Oct  7 2001 Mike A. Harris <mharris@redhat.com> 1.8.4-1
- Updated to 1.8.4, now using tar.bz2
- Removed kanjiconv-fix patch as it is integrated now
- Added xchat-1.8.4-fix-USE_GNOME.patch to fix simple ifdef USE_GNOME typo

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
