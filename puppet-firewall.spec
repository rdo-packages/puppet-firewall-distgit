%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppetlabs-firewall

Name:           puppet-firewall
Version:        7.0.2
Release:        1%{?dist}
Summary:        Manages Firewalls such as iptables
License:        ASL 2.0

URL:            http://github.com/puppetlabs/puppetlabs-firewall

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/v%{upstream_version}.tar.gz#/%{upstream_name}-v%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0
Requires:       rubygem(puppet-resource_api) >= 1.8.18

%description
Manages Firewalls such as iptables

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/firewall/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/firewall/



%files
%{_datadir}/openstack-puppet/modules/firewall/


%changelog
* Tue Oct 17 2023 RDO <dev@lists.rdoproject.org> 7.0.2-1
- Update to 7.0.2

