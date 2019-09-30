# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global upstream_name glance_store

Name:           python-glance-store
Version:        1.0.1
Release:        1%{?dist}
Summary:        OpenStack Image Service Store Library

License:        ASL 2.0
URL:            https://github.com/openstack/%{upstream_name}
Source0:        https://tarballs.openstack.org/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git

%description
OpenStack image service store library


%package -n python%{pyver}-glance-store
Summary:    %{summary}
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr
Requires:       python%{pyver}-eventlet
Requires:       python%{pyver}-cinderclient >= 2.0.1
Requires:       python%{pyver}-keystoneauth1 >= 3.4.0
Requires:       python%{pyver}-keystoneclient >= 1:3.8.0
Requires:       python%{pyver}-requests
Requires:       python%{pyver}-six >= 1.10.0
Requires:       python%{pyver}-stevedore >= 1.20.0
Requires:       python%{pyver}-oslo-concurrency >= 3.26.0
Requires:       python%{pyver}-oslo-config >= 2:5.2.0
Requires:       python%{pyver}-oslo-i18n >= 3.15.3
Requires:       python%{pyver}-oslo-rootwrap
Requires:       python%{pyver}-oslo-serialization >= 2.18.0
Requires:       python%{pyver}-oslo-utils >= 3.33.0
Requires:       python%{pyver}-os-brick >= 1.11.0
Requires:       python%{pyver}-oslo-privsep >= 1.23.0
# Handle python2 exception
%if %{pyver} == 2
Requires:       python-enum34
Requires:       python-jsonschema
%else
Requires:       python%{pyver}-jsonschema
%endif
%{?python_provide:%python_provide python%{pyver}-glance-store}

%description -n python%{pyver}-glance-store
%{description}

%prep
%autosetup -S git -n %{upstream_name}-%{upstream_version}

%build
%{pyver_build}

%install
%{pyver_install}

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s ./glance-rootwrap %{buildroot}%{_bindir}/glance-rootwrap-%{pyver}

install -p -D -m 644 etc/glance/rootwrap.d/glance_cinder_store.filters %{buildroot}%{_datarootdir}/%{upstream_name}/glance_cinder_store.filters

%files -n python%{pyver}-glance-store
%doc AUTHORS ChangeLog
%license LICENSE
%{_bindir}/glance-rootwrap
%{_bindir}/glance-rootwrap-%{pyver}
%{_datarootdir}/%{upstream_name}
%{_datarootdir}/%{upstream_name}/*.filters
%{pyver_sitelib}/%{upstream_name}
%{pyver_sitelib}/%{upstream_name}-*.egg-info

%changelog
* Mon Sep 30 2019 RDO <dev@lists.rdoproject.org> 1.0.1-1
- Update to 1.0.1

* Mon Sep 23 2019 RDO <dev@lists.rdoproject.org> 1.0.0-1
- Update to 1.0.0

