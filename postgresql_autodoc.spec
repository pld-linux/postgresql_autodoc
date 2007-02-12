# $Revision: 1.6 $ $Date: 2007-02-12 01:06:27 $

%include	/usr/lib/rpm/macros.perl

Summary:	postgresql_autodoc - Perl script for creating documentaion for PostgreSQL databases
Summary(pl.UTF-8):   postgresql_autodoc - skrypt Perla umożliwiający tworzenie dokumentacji baz PostgreSQL
Name:		postgresql_autodoc
Version:	1.25
Release:	1
License:	BSD-like
Group:		Applications/Databases
Source0:	http://www.rbt.ca/autodoc/binaries/%{name}-%{version}.tar.gz
# Source0-md5:	f61071a23f6b34f948bbf799de91e8e4
URL:		http://www.rbt.ca/autodoc/
BuildRequires:	perl-DBI
BuildRequires:	perl-DBD-Pg
BuildRequires:	perl-HTML-Template
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
postgresql_autodoc is a utility which will run through PostgreSQL
system tables and returns HTML, Dot, Dia and DocBook XML which
describes the database.

The default output may be changed or new types may be created by
altering the Templates which control the text file formatting.

%description -l pl.UTF-8
postgresql_autodoc jest narzędziem potrafiącym przeanalizować tabele
systemowe PostgreSQL w celu utworzenia plików HTML, Dot, Dia i DocBook
XML opisujących analizowaną bazę danych.

Domyślna postać wyników może być zmieniana, a nowe typy plików
wynikowych mogą być tworzone poprzez zmiany w szablonach
kontrolujących proces formatowania plików wynikowych.

%prep
%setup -q -n %{name}

%build
%configure \
	--datadir=%{_datadir}/postgresql_autodoc
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
%{_datadir}/postgresql_autodoc
