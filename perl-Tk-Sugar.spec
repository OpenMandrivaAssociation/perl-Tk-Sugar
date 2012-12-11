%define upstream_name    Tk-Sugar
%define upstream_version 1.093190

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Sugar syntax for Tk
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
the Tk manpage is a great graphical toolkit to write desktop applications.
However, one can get bothered with the constant typing of quotes and
options. the Tk::Sugar manpage provides handy subs for common options used
when programming Tk.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.93.190-2mdv2011.0
+ Revision: 655240
- rebuild for updated spec-helper

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.93.190-1mdv2011.0
+ Revision: 466431
- update to 1.093190

* Sun Nov 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.93.180-1mdv2010.1
+ Revision: 466153
- import perl-Tk-Sugar


* Sun Nov 15 2009 cpan2dist 1.093180-1mdv
- initial mdv release, generated with cpan2dist
