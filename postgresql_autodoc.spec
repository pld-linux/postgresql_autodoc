# $Revision: 1.1 $ $Date: 2004-05-29 18:46:05 $

%include	/usr/lib/rpm/macros.perl

Summary:	postgresql_autodoc - Perl script for creating documentaion for PostgreSQL databases
Summary(pl):	postgresql_autodoc - skrypt Perla umo¿liwiaj±cy tworzenie dokumentacji baz PostgreSQL
Name:		postgresql_autodoc
Version:	1.22
Release:	1
License:	BSD-like
Group:		Applications/Databases
Source0:	http://www.rbt.ca/autodoc/binaries/%{name}-%{version}.tar.gz
# Source0-md5:	c3e8ed8f31dbd8f4712364478efab9bf
URL:		http://www.rbt.ca/autodoc/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-DBI
BuildRequires:	perl-DBD-Pg
BuildRequires:	perl-HTML-Template
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
postgresql_autodoc is a utility which will run through PostgreSQL
system tables and returns HTML, Dot, Dia and DocBook XML which
describes the database.

The default output may be changed or new types may be created by
altering the Templates which control the text file formatting.

%description -l pl
postgresql_autodoc jest narzêdziem potrafi±cym przeanalizowaæ tabele
systemowe PostgreSQL w celu utworzenia plików HTML, Dot, Dia i DocBook
XML opisuj±cych analizowan± bazê danych.

Domy¶lna postaæ wyników mo¿e byæ zmieniana, a nowe typy plików
wynikowych mog± byæ tworzone poprzez zmiany w szablonach
kontroluj±cych proces formatowania plików wynikowych.

%prep
%setup -q -n %{name}

%build
%configure --datadir=%{_datadir}/postgresql_autodoc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/postgresql_autodoc}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	datadir=$RPM_BUILD_ROOT%{_datadir}/postgresql_autodoc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/postgresql_autodoc
%dir %{_datadir}/postgresql_autodoc
%{_datadir}/postgresql_autodoc
