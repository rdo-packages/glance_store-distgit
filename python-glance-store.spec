%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global upstream_name glance_store

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-glance-store
Version:        XXX
Release:        XXX
Summary:        OpenStack Image Service Store Library

License:        ASL 2.0
URL:            https://github.com/openstack/%{upstream_name}
Source0:        https://tarballs.openstack.org/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:      noarch

%description
OpenStack image service store library


%package -n python2-glance-store
Summary:    %{summary}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr
Requires:       python-debtcollector >= 1.2.0
Requires:       python-eventlet
Requires:       python-cinderclient >= 2.0.1
Requires:       python-keystoneauth1 >= 2.18.0
Requires:       python-keystoneclient >= 1:3.8.0
Requires:       python-iso8601
Requires:       python-requests
Requires:       python-six >= 1.9.0
Requires:       python-stevedore >= 1.20.0
Requires:       python-oslo-concurrency >= 3.8.0
Requires:       python-oslo-config >= 2:3.22.0
Requires:       python-oslo-i18n >= 2.1.0
Requires:       python-oslo-rootwrap
Requires:       python-oslo-serialization >= 1.10.0
Requires:       python-oslo-utils >= 3.20.0
Requires:       python-enum34
Requires:       python-jsonschema
Requires:       python-os-brick >= 1.11.0
Requires:       python-oslo-privsep >= 1.9.0
%{?python_provide:%python_provide python2-glance-store}

%description -n python2-glance-store
%{description}


%if 0%{?with_python3}
%package -n python3-glance-store
Summary:    %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-eventlet
Requires:       python3-cinderclient >= 2.0.1
Requires:       python3-keystoneauth1 >= 2.18.0
Requires:       python3-keystoneclient >= 1:3.8.0
Requires:       python3-iso8601
Requires:       python3-requests
Requires:       python3-six >= 1.9.0
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-oslo-concurrency >= 3.8.0
Requires:       python3-oslo-config >= 2:3.22.0
Requires:       python3-oslo-i18n >= 2.1.0
Requires:       python3-oslo-rootwrap
Requires:       python3-oslo-serialization >= 1.10.0
Requires:       python3-oslo-utils >= 3.20.0
Requires:       python3-enum34
Requires:       python3-jsonschema
Requires:       python3-os-brick >= 1.11.0
Requires:       python3-oslo-privsep >= 1.9.0
%{?python_provide:%python_provide python3-glance-store}

%description -n python3-glance-store
%{description}
%endif

%prep
%setup -q -n %{upstream_name}-%{upstream_version}


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/glance-rootwrap %{buildroot}%{_bindir}/glance-rootwrap-%{python3_version}
ln -s ./glance-rootwrap-%{python3_version} %{buildroot}%{_bindir}/glance-rootwrap-3
%endif

%py2_install
mv %{buildroot}%{_bindir}/glance-rootwrap %{buildroot}%{_bindir}/glance-rootwrap-%{python2_version}
ln -s ./glance-rootwrap-%{python2_version} %{buildroot}%{_bindir}/glance-rootwrap-2
ln -s ./glance-rootwrap-%{python2_version} %{buildroot}%{_bindir}/glance-rootwrap

install -p -D -m 644 etc/glance/rootwrap.d/glance_cinder_store.filters %{buildroot}%{_datarootdir}/%{upstream_name}/glance_cinder_store.filters

%files -n python2-glance-store
%doc AUTHORS ChangeLog
%license LICENSE
%{_bindir}/glance-rootwrap
%{_bindir}/glance-rootwrap-2*
%{_datarootdir}/%{upstream_name}
%{_datarootdir}/%{upstream_name}/*.filters
%{python2_sitelib}/%{upstream_name}
%{python2_sitelib}/%{upstream_name}-*.egg-info

%if 0%{?with_python3}
%files -n python3-glance-store
%doc AUTHORS ChangeLog
%license LICENSE
%{_bindir}/glance-rootwrap-3*
%{_datarootdir}/%{upstream_name}
%{_datarootdir}/%{upstream_name}/*.filters
%{python3_sitelib}/%{upstream_name}
%{python3_sitelib}/%{upstream_name}-*.egg-info
%endif

%changelog
