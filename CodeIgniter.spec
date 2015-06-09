%define		php_min_version 5.2.4
%include	/usr/lib/rpm/macros.php
Summary:	A powerful PHP framework with a very small footprint
Name:		CodeIgniter
Version:	2.2.2
Release:	0.1
License:	other
Group:		Development/Languages/PHP
Source0:	https://github.com/bcit-ci/CodeIgniter/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	042f94f7c59b22111c7cf56673769c8b
Source1:	INSTALL-PLD.txt
Source2:	codeigniter-install
Patch0:		pld.patch
URL:		http://codeigniter.com/
BuildRequires:	rpm-php-pearprov >= 4.3
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(hash)
Requires:	php(mbstring)
Requires:	php(mysql)
Requires:	php(pcre)
Requires:	php(session)
Requires:	php(simplexml)
Requires:	php(spl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}

%description
CodeIgniter is a powerful PHP framework with a very small footprint,
built for PHP coders who need a simple and elegant toolkit to create
full-featured web applications. If you're a developer who lives in the
real world of shared hosting accounts and clients with deadlines, and
if you're tired of ponderously large and thoroughly undocumented
frameworks.

%package doc
Summary:	CodeIgniter documentation
Group:		Development/Languages/PHP

%description doc
CodeIgniter documentation.

%prep
%setup -q
%patch0 -p1

cp -p %{SOURCE1} user_guide

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir}}
cp -r index.php application system $RPM_BUILD_ROOT%{_appdir}
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}

find $RPM_BUILD_ROOT%{_datadir}/%{name} -name index.html | xargs rm -v
rm -r $RPM_BUILD_ROOT%{_appdir}/application/{cache,core,helpers,hooks,libraries}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner -e %{name} <<-EOF
Please read INSTALL-PLD.txt to know how can use the users the installed CodeIgniter!
EOF

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/codeigniter-install

%dir %{_appdir}
%dir %{_appdir}/application
%dir %{_appdir}/application/config
%dir %{_appdir}/application/controllers
%dir %{_appdir}/application/errors
%dir %{_appdir}/application/language
%dir %{_appdir}/application/views
%dir %{_appdir}/system
%dir %{_appdir}/system/core
%dir %{_appdir}/system/database
%dir %{_appdir}/system/database/drivers
%dir %{_appdir}/system/fonts
%dir %{_appdir}/system/helpers
%dir %{_appdir}/system/language
%dir %{_appdir}/system/libraries

%{_appdir}/index.php
%{_appdir}/application/.htaccess
%{_appdir}/system/.htaccess

%{_appdir}/application/config/*
%{_appdir}/application/controllers/*
%{_appdir}/application/errors/*
%{_appdir}/application/language/*
%{_appdir}/application/views/*

%{_appdir}/system/core/*
%{_appdir}/system/database/DB*.php
%{_appdir}/system/database/drivers/*
%{_appdir}/system/fonts/*
%{_appdir}/system/helpers/*
%{_appdir}/system/language/*
%{_appdir}/system/libraries/*

%files doc
%defattr(644,root,root,755)
%doc user_guide/*
