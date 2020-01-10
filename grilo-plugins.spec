# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global grilo_version 0.2.11

Name:		grilo-plugins
Version:	0.2.14
Release:	8%{?dist}
Summary:	Plugins for the Grilo framework

Group:		Applications/Multimedia
License:	LGPLv2+
Url:		https://live.gnome.org/Grilo
Source0:	http://ftp.gnome.org/pub/GNOME/sources/grilo-plugins/%{release_version}/grilo-plugins-%{version}.tar.xz

BuildRequires:	avahi-gobject-devel
BuildRequires:	grilo-devel >= %{grilo_version}
BuildRequires:	glib2-devel
BuildRequires:	gom-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libxml2-devel
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libarchive-devel
BuildRequires:	libmediaart-devel
BuildRequires:	libsoup-devel
%if 0%{?fedora}
BuildRequires:	lua-devel
%endif
BuildRequires:	rest-devel
BuildRequires:	sqlite-devel
BuildRequires:	libgdata-devel
BuildRequires:	totem-pl-parser-devel
BuildRequires:	tracker-devel
BuildRequires:	libdmapsharing-devel
BuildRequires:	json-glib-devel

Requires:	grilo >= %{grilo_version}
Requires:	dleyna-server

Patch0:		grilo-plugins-0.2.14-bug-fixes.patch
BuildRequires: autoconf automake intltool libtool gnome-common yelp-tools
Patch1:		0001-Use-copy-paste-instead-of-gmime.patch
Patch2:		0001-Only-require-gom-0.2.1.patch
Patch3:		0001-Port-back-to-libmediaart-1.0-API.patch
Patch4:		0001-youtube-Fix-an-unpaired-unref-of-a-GCancellable-when.patch

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains plugins to get information from theses sources:
- Apple Trailers
- Bookmarks
- Euronews
- Filesystem
- Flickr
- Freebox
- Gravatar
- iTunes Music Sharing
- Jamendo
- Last.fm (for album arts)
- Local metadata (album arts and thumbnails)
- Metadata Store
- Pocket
- Podcasts
- Radio France
- Shoutcast
- The Guardian Videos
- Tracker
- Vimeo
- Youtube

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoreconf -i -f

%configure				\
	--disable-static		\
	--disable-shoutcast		\
	--enable-apple-trailers		\
	--disable-bliptv		\
	--enable-bookmarks		\
	--enable-dleyna			\
	--enable-dmap			\
	--enable-filesystem		\
	--enable-flickr			\
	--enable-freebox		\
	--enable-gravatar		\
	--enable-goa			\
	--enable-jamendo		\
	--enable-lastfm-albumart	\
	--enable-localmetadata		\
%if 0%{?fedora}
	--enable-lua-factory		\
%else
	--disable-lua-factory		\
%endif
	--enable-metadata-store		\
	--enable-magnatune		\
	--enable-optical-media		\
	--enable-opensubtitles		\
	--enable-pocket			\
	--enable-podcasts		\
	--enable-shoutcast		\
	--enable-raitv			\
	--enable-tmdb			\
	--enable-tracker		\
	--enable-thetvdb		\
	--enable-vimeo			\
	--enable-youtube		\
	--enable-tracker

# Silence unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove files that will not be packaged
rm -f $RPM_BUILD_ROOT%{_libdir}/grilo-%{release_version}/*.la
rm -f $RPM_BUILD_ROOT%{_bindir}/*

%find_lang grilo-plugins --with-gnome

%files -f grilo-plugins.lang
%doc AUTHORS COPYING NEWS README
%doc %{_datadir}/help/C/examples/example-tmdb.c
%if 0%{?fedora}
%{_datadir}/grilo-plugins/
%endif
%{_libdir}/grilo-%{release_version}/*.so*
%{_libdir}/grilo-%{release_version}/*.xml

%changelog
* Mon Sep 07 2015 Bastien Nocera <bnocera@redhat.com> 0.2.14-8
- Fix crash in YouTube plugin
Resolves: #1258811

* Fri Sep 04 2015 Bastien Nocera <bnocera@redhat.com> 0.2.14-7
- Enable the libdmapsharing plugin
Related: #1221283

* Thu Sep 03 2015 Bastien Nocera <bnocera@redhat.com> 0.2.14-6
- Enable a number of missing plugins
Related: #1184200
- Disable blip.tv plugin as service has now closed
- Add patch to downgrade the gom requirements
- Port back local-metadata plugin to libmediaart-1.0

* Thu Sep 03 2015 Bastien Nocera <bnocera@redhat.com> 0.2.14-5
- Rebuild
Related: #1184200

* Wed Jul 01 2015 Debarshi Ray <rishi@fedoraproject.org> 0.2.14-4
- Un-conditionalize dleyna-server requirement
Related: #1174536

* Thu May 14 2015 Ray Strode <rstrode@redhat.com> 0.2.14-3
- Rebuild against new totem-pl-parser
Related: #1174536

* Fri May 08 2015 Ray Strode <rstrode@redhat.com> 0.2.14-2
- Conditionalize out dleyna-server for now
Related: #1174536

* Mon May 04 2015 Bastien Nocera <bnocera@redhat.com> 0.2.14-1
- Update to 0.2.14
Resolves: #1174536

* Thu Mar 19 2015 Richard Hughes <rhughes@redhat.com> - 0.2.13-1
- Update to 0.2.13
- Resolves: #1174536

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.2.6-4
- Mass rebuild 2014-01-24

* Mon Jan 06 2014 Bastien Nocera <bnocera@redhat.com> 0.2.6-3
- Add gcrypt BR for autoconf macros
Resolves: #1048862

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.2.6-2
- Mass rebuild 2013-12-27

* Mon Apr 29 2013 Bastien Nocera <bnocera@redhat.com> 0.2.6-1
- Remove gmime BR

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.6-1
- Update to 0.2.6

* Mon Jan 28 2013 Matthias Clasen <mclasen@redhat.com> - 0.2.5-3
- Fix build against newer tracker

* Sun Jan 27 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.5-2
- Rebuild for tracker

* Thu Dec 20 2012 Bastien Nocera <bnocera@redhat.com> 0.2.5-1
- Update to 0.2.5

* Tue Dec 04 2012 Bastien Nocera <bnocera@redhat.com> 0.2.4-1
- Update to 0.2.4

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> 0.2.3-1
- Update to 0.2.3

* Fri Oct 05 2012 Bastien Nocera <bnocera@redhat.com> 0.2.2-1
- Update to 0.2.2

* Wed Oct 03 2012 Bastien Nocera <bnocera@redhat.com> 0.2.1-1
- Update to 0.2.1

* Fri Aug 31 2012 Debarshi Ray <rishi@fedoraproject.org> 0.2.0-1
- update to 0.2.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 25 2012 Bastien Nocera <bnocera@redhat.com> 0.1.19-1
- Update to 0.1.19

* Fri Mar 16 2012 Adam Williamson <awilliam@redhat.com> - 0.1.18-4
- Rebuild for new tracker again

* Tue Feb 28 2012 Matthias Clasen <mclasen@redhat.com> - 0.1.18-3
- Rebuild for new tracker

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Bastien Nocera <bnocera@redhat.com> 0.1.18-1
- Update to 0.1.18

* Thu Nov 17 2011 Daniel Drake <dsd@laptop.org> 0.1.17-2
- rebuild for libquvi.so.7

* Mon Oct 17 2011 Bastien Nocera <bnocera@redhat.com> 0.1.17-1
- Update to 0.1.17

* Mon Jul 04 2011 Bastien Nocera <bnocera@redhat.com> 0.1.16-1
- Update to 0.1.16

* Fri Jun 17 2011 Peter Robinson <pbrobinson@gmail.com> 0.1.15-5
- rebuild for new gupnp/gssdp

* Fri May 20 2011 Bastien Nocera <bnocera@redhat.com> 0.1.15-4
- Update with more comments from Kalev Lember <kalev@smartlink.ee>

* Fri May 20 2011 Bastien Nocera <bnocera@redhat.com> 0.1.15-3
- Update with comments from Kalev Lember <kalev@smartlink.ee>

* Fri May 20 2011 Bastien Nocera <bnocera@redhat.com> 0.1.15-2
- Fix a few rpmlint warnings

* Thu Apr 21 2011 Bastien Nocera <bnocera@redhat.com> 0.1.15-1
- Fist package, based on upstream work by Juan A.
  Suarez Romero <jasuarez@igalia.com>

