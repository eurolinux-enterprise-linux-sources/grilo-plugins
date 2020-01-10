# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global grilo_version 0.3.1
%global goa_version 3.17.91

Name:		grilo-plugins
Version:	0.3.4
Release:	3%{?dist}
Summary:	Plugins for the Grilo framework

License:	LGPLv2+
URL:		https://wiki.gnome.org/Projects/Grilo
Source0:	https://download.gnome.org/sources/grilo-plugins/%{release_version}/grilo-plugins-%{version}.tar.xz

# https://bugzilla.redhat.com/show_bug.cgi?id=1477129
Patch0:		0001-lua-factory-Downgrade-requirement-to-lua-5.1.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=788557
Patch1:		0002-lua-factory-Fix-warning-in-Apple-trailers-source.patch

BuildRequires:	avahi-gobject-devel
BuildRequires:	grilo-devel >= %{grilo_version}
BuildRequires:	glib2-devel
BuildRequires:	gom-devel
BuildRequires:	gnome-online-accounts-devel >= %{goa_version}
BuildRequires:	gperf
BuildRequires:	libgcrypt-devel
BuildRequires:	libxml2-devel
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libarchive-devel
BuildRequires:	libmediaart-devel
BuildRequires:	libsoup-devel
BuildRequires:	lua-devel
BuildRequires:	rest-devel
BuildRequires:	sqlite-devel
BuildRequires:	libgdata-devel
BuildRequires:	totem-pl-parser-devel
BuildRequires:	tracker-devel
%if 0%{?fedora}
BuildRequires:	gmime-devel
%endif
BuildRequires:	libdmapsharing-devel
BuildRequires:	json-glib-devel
BuildRequires:	libtool autoconf automake gnome-common

Requires:	dleyna-server
Requires:	gnome-online-accounts%{_isa} >= %{goa_version}
Requires:	grilo%{_isa} >= %{grilo_version}

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

%build
autoreconf -f

%configure				\
	--disable-static		\
	--disable-shoutcast		\
	--enable-bookmarks		\
	--enable-dleyna			\
	--enable-dmap			\
	--enable-filesystem		\
	--enable-flickr			\
	--enable-freebox		\
	--enable-gravatar		\
	--enable-jamendo		\
	--enable-lua-factory		\
	--enable-metadata-store		\
%if 0%{?fedora}
	--enable-podcasts		\
%endif
	--enable-tmdb			\
	--enable-tracker		\
	--enable-vimeo			\
	--enable-youtube		\
	--enable-tracker

# Silence unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}


%install
%make_install

# Remove files that will not be packaged
rm -f $RPM_BUILD_ROOT%{_libdir}/grilo-%{release_version}/*.la
rm -f $RPM_BUILD_ROOT%{_bindir}/*

%find_lang grilo-plugins --with-gnome

%files -f grilo-plugins.lang
%license COPYING
%doc AUTHORS NEWS README
%doc %{_datadir}/help/C/examples/example-tmdb.c
%{_datadir}/grilo-plugins/
%{_libdir}/grilo-%{release_version}/*.so*

%changelog
* Thu Oct 05 2017 Bastien Nocera <bnocera@redhat.com> - 0.3.4-3
- Fix size reporting in Apple Trailers source
- Add compatibility layer to allow building with lua 5.1
Resolves: #1477129

* Wed Oct 04 2017 Bastien Nocera <bnocera@redhat.com> - 0.3.4-2
- Enable lua plugins
Resolves: #1477129

* Tue Feb 14 2017 Kalev Lember <klember@redhat.com> - 0.3.4-1
- Update to 0.3.4
- Resolves: #1386975

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

