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
BuildRequires:  python2-setuptools
BuildRequires:  python2-pbr
Requires:       python2-eventlet
Requires:       python2-cinderclient >= 2.0.1
Requires:       python2-keystoneauth1 >= 3.3.0
Requires:       python2-keystoneclient >= 1:3.8.0
Requires:       python2-requests
Requires:       python2-six >= 1.10.0
Requires:       python2-stevedore >= 1.20.0
Requires:       python2-oslo-concurrency >= 3.25.0
Requires:       python2-oslo-config >= 2:5.1.0
Requires:       python2-oslo-i18n >= 3.15.3
Requires:       python2-oslo-rootwrap
Requires:       python2-oslo-serialization >= 2.18.0
Requires:       python2-oslo-utils >= 3.33.0
Requires:       python2-os-brick >= 1.11.0
Requires:       python2-oslo-privsep >= 1.23.0
%if 0%{?fedora} > 0
Requires:       python2-enum34
Requires:       python2-jsonschema
%else
Requires:       python-enum34
Requires:       python-jsonschema
%endif
%{?python_provide:%python_provide python2-glance-store}

%description -n python2-glance-store
%{description}


%if 0%{?with_python3}
%package -n python3-glance-store
Summary:    %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
Requires:       python3-eventlet
Requires:       python3-cinderclient >= 2.0.1
Requires:       python3-keystoneauth1 >= 3.3.0
Requires:       python3-keystoneclient >= 1:3.8.0
Requires:       python3-requests
Requires:       python3-six >= 1.10.0
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-oslo-concurrency >= 3.25.0
Requires:       python3-oslo-config >= 2:5.1.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-rootwrap
Requires:       python3-oslo-serialization >= 2.18.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-enum34
Requires:       python3-jsonschema
Requires:       python3-os-brick >= 1.11.0
Requires:       python3-oslo-privsep >= 1.23.0
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
# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/glance_store/commit/?id=6d97ea212b689348baaa59ae3677ce4f65cb58f4
