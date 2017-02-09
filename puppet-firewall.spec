%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-firewall
%global commit 463ec1d0f5c50a719cb96e6479d90b8de8f41489
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-firewall
Version:        1.8.2
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
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 1.8.2-1.463ec1dgit
- Ocata update 1.8.2 (463ec1d0f5c50a719cb96e6479d90b8de8f41489)

