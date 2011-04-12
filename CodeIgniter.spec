%define		php_min_version 5.2.4
%include	/usr/lib/rpm/macros.php
Summary:	A powerful PHP framework with a very small footprint
Name:		CodeIgniter
Version:	2.0.2
Release:	0.2
License:	other
Group:		Development/Languages/PHP
Source0:	http://www.codeigniter.com/download_files/reactor/%{name}_%{version}.zip
# Source0-md5:	e75bab8cf27d2fb2483c5bb61b85a524
Source1:	apache.conf
Source2:	httpd.conf
Source3:	lighttpd.conf
URL:		http://www.kohanaframework.org/
BuildRequires:	rpm-php-pearprov >= 4.3
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-ctype
Requires:	php-date
Requires:	php-hash
Requires:	php-mbstring
Requires:	php-mysql
Requires:	php-pcre
Requires:	php-session
Requires:	php-simplexml
Requires:	php-spl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}
%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}

%description
CodeIgniter is a powerful PHP framework with a very small footprint,
built for PHP coders who need a simple and elegant toolkit to create
full-featured web applications. If you're a developer who lives in the
real world of shared hosting accounts and clients with deadlines, and
if you're tired of ponderously large and thoroughly undocumented
frameworks.

%prep
%setup -q -n %{name}_%{version}
%{__sed} -i 's,\$application_folder.*=.*,$application_folder = "/home/users";,' index.php

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_appdir}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

cp -r index.php application system $RPM_BUILD_ROOT%{_appdir}
cp -r user_guide/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_sysconfdir}
%doc %{_docdir}/%{name}-%{version}

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf

%{_appdir}
