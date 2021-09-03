%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-firewall
%global commit 6e08f9678d8c4a80e96888a1a82b5fabd647efec
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-firewall
Version:        2.6.0
Release:        1%{?alphatag}%{?dist}
Summary:        Manages Firewalls such as iptables
License:        ASL 2.0

URL:            http://github.com/puppetlabs/puppetlabs-firewall

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

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
* Fri Sep 03 2021 RDO <dev@lists.rdoproject.org> 2.6.0-1.6e08f96git
- Update to 2.6.0

* Thu Mar 25 2021 RDO <dev@lists.rdoproject.org> 2.5.0-2.6e08f96git
- Update to post 2.5.0 (6e08f9678d8c4a80e96888a1a82b5fabd647efec)

