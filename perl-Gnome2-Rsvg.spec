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
Conflicts:	drakxtools < 9.1-15mdk

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


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.110.0-3
+ Revision: 773558
- clean out spec
- don't pass '-s' to %%optflags
- drop redundant perl-Glib dependency
- update buildrequires to use perl() & pkgconfig() dependencies
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 555878
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 552313
- update to 0.11

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 408409
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2009.0
+ Revision: 257119
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.10-2mdv2008.1
+ Revision: 152093
- rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 0.10-1mdv2008.1
+ Revision: 135846
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Jan 04 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.10-1mdv2007.1
+ Revision: 104210
- new release

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Gnome2-Rsvg

* Thu Mar 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.06-2mdk
- fix buildrequires

* Tue Jan 31 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.06-1mdk
- new releaase

* Mon Jan 23 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.05-2mdk
- Add BuildRequires : libatk-devel

* Thu Oct 13 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.05-1mdk
- new release

* Fri Feb 25 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-1mdk
- new release

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.03-2mdk
- rebuild for new perl

* Tue Jul 27 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.03-1mdk
- new release

* Mon Jun 07 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.02-1mdk
- new release

* Sat Apr 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.01-2mdk
- relink with new libcroco

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.01-1mdk
- initial release

