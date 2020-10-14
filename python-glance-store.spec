%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global upstream_name glance_store
%global pkg_name glance-store

Name:           python-glance-store
Version:        XXX
Release:        XXX
Summary:        OpenStack Image Service Store Library

License:        ASL 2.0
URL:            https://github.com/openstack/%{upstream_name}
Source0:        https://tarballs.openstack.org/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{upstream_name}/%{upstream_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:  git

%description
OpenStack image service store library


%package -n python3-%{pkg_name}
Summary:    %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
Requires:       python3-eventlet
Requires:       python3-cinderclient >= 4.1.0
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-keystoneclient >= 1:3.8.0
Requires:       python3-requests
Requires:       python3-six >= 1.10.0
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-oslo-concurrency >= 3.26.0
Requires:       python3-oslo-config >= 2:5.2.0
Requires:       python3-oslo-i18n >= 3.15.3
Requires:       python3-oslo-rootwrap
Requires:       python3-oslo-serialization >= 2.18.0
Requires:       python3-oslo-utils >= 3.33.0
Requires:       python3-os-brick >= 2.6.0
Requires:       python3-oslo-privsep >= 1.23.0
Requires:       python3-jsonschema
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
%{description}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -S git -n %{upstream_name}-%{upstream_version}

%build
%{py3_build}

%install
%{py3_install}

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s ./glance-rootwrap %{buildroot}%{_bindir}/glance-rootwrap-3

install -p -D -m 644 etc/glance/rootwrap.d/glance_cinder_store.filters %{buildroot}%{_datarootdir}/%{upstream_name}/glance_cinder_store.filters

rm -rf %{buildroot}%{_prefix}/etc/glance

%files -n python3-%{pkg_name}
%doc AUTHORS ChangeLog
%license LICENSE
%{_bindir}/glance-rootwrap
%{_bindir}/glance-rootwrap-3
%{_datarootdir}/%{upstream_name}
%{_datarootdir}/%{upstream_name}/*.filters
%{python3_sitelib}/%{upstream_name}
%{python3_sitelib}/%{upstream_name}-*.egg-info

%changelog
