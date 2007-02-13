#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Filter
Summary:	Apache::Filter - alter the output of previous handlers
Summary(pl.UTF-8):	Apache::Filter - obrabianie danych na wyjściu poprzedniego modułu
Name:		perl-Apache-Filter
Version:	1.024
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22fdc595d61fbfac8c25c9529fcf6551
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%%define		_noautoreq	'perl(Apache)'

%description
Apache::Filter Perl module alters the output of previous handlers in a
chain of "filter-aware" Apache modules.

%description -l pl.UTF-8
Moduł Perla Apache::Filter obrabia dane na wyjściu poprzedniego modułu
w ramach listy "filtrowalnych" modułów z klasy Apache.

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
