#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Filter
Summary:	Apache::Filter - alter the output of previous handlers
Summary(pl):	Apache::Filter - obrabianie danych na wyj¶ciu poprzedniego modu³u
Name:		perl-Apache-Filter
Version:	1.022
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f2aa0a85081c28d6d86a14773149ebc5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%%define		_noautoreq	'perl(Apache)'

%description
Apache::Filter Perl module alters the output of previous handlers in
a chain of "filter-aware" Apache modules.

%description -l pl
Modu³ Perla Apache::Filter obrabia dane na wyj¶ciu poprzedniego modu³u
w ramach listy "filtrowalnych" modu³ów z klasy Apache.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "!" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Apache/*.pm
%{_mandir}/man3/*
