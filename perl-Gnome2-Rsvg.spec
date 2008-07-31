%define module Gnome2-Rsvg
%define fmodule Gnome2/Rsvg

Summary: Perl module for the gnome2-2.x rsvg libraries
Name:    perl-%module
Version: 0.10
Release: %mkrel 4
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  http://prdownloads.sourceforge.net/gtk2-perl/%module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRequires: librsvg-devel => 2.4.0 
BuildRequires: perl-devel 
BuildRequires: perl-ExtUtils-PkgConfig 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Glib => 1.00
BuildRequires: perl-Gtk2 gtk+2-devel
BuildRequires: libatk-devel
Requires: perl-Glib >= 1.00
Conflicts: drakxtools < 9.1-15mdk
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides perl access to GNOME-2.x rsvg libraries
(which uses libart and pango to render svg files.

%prep
%setup -q -n %module-%version
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
%{perl_vendorarch}/%fmodule
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule


