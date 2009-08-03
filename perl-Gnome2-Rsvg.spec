%define upstream_name    Gnome2-Rsvg
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl module for the gnome2-2.x rsvg libraries
License:    GPL+ or Artistic
Group:      Development/GNOME and GTK+
URL:        http://gtk2-perl.sf.net/
Source0:    http://prdownloads.sourceforge.net/gtk2-perl/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: libatk-devel
BuildRequires: librsvg-devel => 2.4.0 
BuildRequires: perl-ExtUtils-PkgConfig 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Glib => 1.00
BuildRequires: perl-Gtk2 gtk+2-devel
BuildRequires: perl-devel 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Conflicts: drakxtools < 9.1-15mdk
Requires: perl-Glib >= 1.00

%description
This module provides perl access to GNOME-2.x rsvg libraries
(which uses libart and pango to render svg files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os -s"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc LICENSE 
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2/*
%{perl_vendorarch}/auto/Gnome2/*
