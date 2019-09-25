%define git_owner       tista500
%define git_url         https://gitlab.com/%{git_owner}/%{name}
Name:           plata-theme
Summary:        Plata Gtk Theme
License:        GPL 2.0 and SA 4.0
URL:            %{git_url}

Version:        0.9.0
Release:        1%{?dist}
Source0:        %{git_url}/-/archive/%{version}/%{name}-%{version}.tar.gz       

BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  inkscape >= 0.91
BuildRequires:  parallel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  sassc    >= 3.3
BuildRequires:  zip
BuildRequires:  marco-devel >= 1.22.2


%description
Plata-theme
A Gtk+ theme based on Material Design Refresh.

%package        Plata
Summary:        A Gtk+ theme based on Material Design Refresh.
%description    Plata

%package        Plata-Lumine
Summary:        A Gtk+ theme based on Material Design Refresh.
%description    Plata-Lumine

%package        Plata-Noir
Summary:        A Gtk+ theme based on Material Design Refresh.
%description    Plata-Noir

%prep
%autosetup
%{_bindir}/autoreconf -fiv

%build
%configure \
--prefix=%{_prefix} \
--enable-parallel \
--enable-plank \
--enable-telegram \
--enable-tweetdeck \
--enable-gtk_next
%make_build

%install
%make_install

%files Plata
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%{_datadir}/themes/Plata/*
%{_datadir}/themes/Plata-Compact/*

%files Plata-Lumine
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%{_datadir}/themes/Plata-Lumine/*
%{_datadir}/themes/Plata-Lumine-Compact/*

%files Plata-Noir
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%{_datadir}/themes/Plata-Noir/*
%{_datadir}/themes/Plata-Noir-Compact/*

%files
%license COPYING LICENSE_CC_BY_SA4
%doc README.md
%{_datadir}/*

%changelog
* Tue Sep 24 2019 Peter Ceiley <peter@ceiley.net> 0.9.0
- Initial RPM release. Adapted from https://github.com/Ceeox/copr-repos.
