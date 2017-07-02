#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Constant
%define		pnam	Generate
%include	/usr/lib/rpm/macros.perl
Summary:	Constant::Generate - Common tasks for symbolic constants
Summary(pl.UTF-8):	Constant::Generate - wspólne zadania dla stałych symbolicznych
Name:		perl-Constant-Generate
Version:	0.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MN/MNUNBERG/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	61636afc1c0be17bc8a26ec4031eae13
URL:		http://search.cpan.org/dist/Constant-Generate/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(constant) >= 1.17
BuildRequires:	perl-Scalar-List-Utils >= 1.20
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Constant::Generate provides useful utilities for handling, debugging,
and generating opaque, 'magic-cookie' type constants as well as
value-significant constants.

%description -l pl.UTF-8
Constant::Generate udostępnia proste narzędzia do obsługi, diagnostyki
i generowania nieprzejrzystych stałych typu "magic cookie" oraz
stałych o znaczeniu zmiennych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Constant
%{perl_vendorlib}/Constant/Generate.pm
%{perl_vendorlib}/Constant/Generate
%{_mandir}/man3/Constant::Generate.3pm*
