%define upstream_name Gnome2-Rsvg
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl module for the gnome2-2.x rsvg libraries
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
URL:		http://gtk2-perl.sf.net/
Source0:	http://prdownloads.sourceforge.net/gtk2-perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(Glib)
BuildRequires:	perl(Gtk2) pkgconfig(gtk+-2.0)
BuildRequires:	perl-devel 

%description
This module provides perl access to GNOME-2.x rsvg libraries
(which uses libart and pango to render svg files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os"
export GTK2_PERL_CFLAGS="$RPM_OPT_FLAGS"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
%makeinstall_std

%files
%doc LICENSE 
%{_mandir}/*/*
%{perl_vendorarch}/Gnome2/*
%{perl_vendorarch}/auto/Gnome2/*
