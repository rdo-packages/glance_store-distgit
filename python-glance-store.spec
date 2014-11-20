%global upstream_name glance_store

Name:           python-glance-store
Version:        XXX
Release:        XXX{?dist}
Summary:        OpenStack Image Service Store Library

License:        ASL 2.0
URL:            https://github.com/openstack/%{upstream_name}
Source0:        https://pypi.python.org/packages/source/g/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
Requires:       python-eventlet
Requires:       python-cinderclient >= 1.0.6
Requires:       python-iso8601
Requires:       python-six
Requires:       python-stevedore
Requires:       python-oslo-config
Requires:       python-oslo-i18n
Requires:       python-oslo-utils
Requires:       python-oslo-serialization


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
# Remove spurious shebang in module without changing timestamp
pushd %{buildroot}%{python_sitelib}/%{upstream_name}/common/
sed 1,2d config.py > config.py.new
touch -r config.py config.py.new
mv config.py.new config.py
popd


%files
%doc AUTHORS ChangeLog
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{python2_sitelib}/%{upstream_name}
%{python2_sitelib}/%{upstream_name}-*.egg-info


%changelog
* Fri Sep 12 2014 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.8-1
- Initial package
