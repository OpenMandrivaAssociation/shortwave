%undefine _debugsource_packages
%define oname Shortwave

Name:       shortwave
Version:    5.0.0
Release:    1
Summary:    Find and listen to internet radio stations

Group:      Applications/Internet
License:    GPLv3
URL:        https://gitlab.gnome.org/World/Shortwave
Source0:    https://gitlab.gnome.org/World/Shortwave/-/archive/%{version}/%{oname}-%{version}.tar.bz2
#Patch0:     cargo-lock.patch

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  intltool
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:	gettext
BuildRequires:	git
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(shumate-1.0)
BuildRequires:	rust 
BuildRequires:	cargo
BuildRequires:	pkgconfig(libdazzle-1.0)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(openssl)

Requires:       dconf

%description
A GTK3 app for finding and listening to internet radio stations.

%prep 
%autosetup -n %{oname}-%{version} -p1 

%build

%meson
%meson_build

%install
%meson_install

%find_lang shortwave

%post
%{_bindir}/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ]
then
    %{_bindir}/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    %{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%license COPYING.md
%{_bindir}/%{name}
%{_datadir}/shortwave/
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/de.haeckerfelix.Shortwave.desktop
%{_datadir}/icons/hicolor/*/apps/de.haeckerfelix.*
%{_datadir}/metainfo/*.xml
%{_datadir}/dbus-1/services/*.service
