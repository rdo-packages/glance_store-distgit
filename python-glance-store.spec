%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global upstream_name glance_store

Name:           python-glance-store
Version:        XXX
Release:        XXX
Summary:        OpenStack Image Service Store Library

License:        ASL 2.0
URL:            https://github.com/openstack/%{upstream_name}
Source0:        https://tarballs.openstack.org/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
Requires:       python-debtcollector >= 1.2.0
Requires:       python-eventlet
Requires:       python-cinderclient >= 1.0.6
Requires:       python-keystoneclient >= 1.6.0
Requires:       python-iso8601
Requires:       python-requests
Requires:       python-six >= 1.9.0
Requires:       python-stevedore >= 1.5.0
Requires:       python-oslo-concurrency >= 3.5.0
Requires:       python-oslo-config >= 3.7.0
Requires:       python-oslo-i18n >= 2.1.0
Requires:       python-oslo-rootwrap
Requires:       python-oslo-serialization >= 1.10.0
Requires:       python-oslo-utils >= 3.5.0
Requires:       python-enum34
Requires:       python-jsonschema


%description
OpenStack image service store library


%prep
%setup -q -n %{upstream_name}-%{upstream_version}


%build
%{__python2} setup.py build
# Remove bundle egg-info
rm -rf %{upstream_name}.egg-info


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc AUTHORS ChangeLog
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/glance-rootwrap
%{python2_sitelib}/%{upstream_name}
%{python2_sitelib}/%{upstream_name}-*.egg-info


%changelog
