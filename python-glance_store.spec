Name:			python-glance_store
Version:		XXX
Release:		1%{?dist}
Summary:		Glance's stores library

License:		ASL 2.0
URL:			http://pypi.python.org/pypi/%{name}
Source0:		http://tarballs.openstack.org/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python-pbr

Requires:	python-setuptools
Requires:	python-eventlet
Requires:	python-oslo-config
Requires:	python-oslo-i18n
Requires:	python-oslo-utils
Requires:	python-oslo-serialization
Requires:	python-iso8601
Requires:	python-six
Requires:	python-stevedore

Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

%description
Glance's stores library

%prep

%setup -q -n glance_store-%{upstream_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc README.rst
%doc LICENSE
%{python_sitelib}/*


%changelog
* Wed Oct 08 2014 Dan Prince <dprince@redhat.com> - XXX
- initial package
