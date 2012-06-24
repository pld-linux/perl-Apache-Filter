#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Filter
Summary:	Apache::Filter Perl module
Summary(cs):	Modul Apache::Filter pro Perl
Summary(da):	Perlmodul Apache::Filter
Summary(de):	Apache::Filter Perl Modul
Summary(es):	M�dulo de Perl Apache::Filter
Summary(fr):	Module Perl Apache::Filter
Summary(it):	Modulo di Perl Apache::Filter
Summary(ja):	Apache::Filter Perl �⥸�塼��
Summary(ko):	Apache::Filter �� ����
Summary(no):	Perlmodul Apache::Filter
Summary(pl):	Modu� Perla Apache::Filter
Summary(pt):	M�dulo de Perl Apache::Filter
Summary(pt_BR):	M�dulo Perl Apache::Filter
Summary(ru):	������ ��� Perl Apache::Filter
Summary(sv):	Apache::Filter Perlmodul
Summary(uk):	������ ��� Perl Apache::Filter
Summary(zh_CN):	Apache::Filter Perl ģ��
Name:		perl-Apache-Filter
Version:	1.022
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%%define		_noautoreq	"perl(Apache)"

%description
Apache::Filter Perl module alters the output of previous handlers in
a chain of "filter-aware" Apache modules.

%description -l pl
Modu� Perla Apache::Filter obrabia dane na wyj�ciu poprzedniego modu�u
w ramach listy "filtrowalnych" modu��w z klasy Apache.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "!" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Apache/*.pm
%{_mandir}/man3/*
