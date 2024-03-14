%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2ef3fe0ec2b075ab7458b5f8b702b20b13df2318

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order sphinx openstackdocstheme
%global upstream_name glance_store
%global pkg_name glance-store

Name:           python-glance-store
Version:        4.7.0
Release:        1%{?dist}
Summary:        OpenStack Image Service Store Library

License:        Apache-2.0
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
BuildRequires:  git-core

%description
OpenStack image service store library


%package -n python3-%{pkg_name}
Summary:    %{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# cinder driver is the default one
Requires:  python3-%{pkg_name}+cinder = %{version}-%{release}

%description -n python3-%{pkg_name}
%{description}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -S git -n %{upstream_name}-%{upstream_version}

sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs};do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}

%build
%pyproject_wheel

%install
%pyproject_install

# Create a versioned binary for backwards compatibility until everything is pure py3
ln -s ./glance-rootwrap %{buildroot}%{_bindir}/glance-rootwrap-3

install -p -D -m 644 etc/glance/rootwrap.d/glance_cinder_store.filters %{buildroot}%{_datarootdir}/%{upstream_name}/glance_cinder_store.filters

rm -rf %{buildroot}%{_prefix}/etc/glance

%pyproject_extras_subpkg -n python3-%{pkg_name} cinder swift

%check
# CentOS CI environment is setting "http://cache.rdu2.centos.org:8080" which breaks the unit tests.
unset http_proxy
unset https_proxy
%tox -e %{default_toxenv}

%files -n python3-%{pkg_name}
%doc AUTHORS ChangeLog
%license LICENSE
%{_bindir}/glance-rootwrap
%{_bindir}/glance-rootwrap-3
%{_datarootdir}/%{upstream_name}
%{_datarootdir}/%{upstream_name}/*.filters
%{python3_sitelib}/%{upstream_name}
%{python3_sitelib}/%{upstream_name}*.dist-info

%changelog
* Thu Mar 14 2024 RDO <dev@lists.rdoproject.org> 4.7.0-1
- Update to 4.7.0


