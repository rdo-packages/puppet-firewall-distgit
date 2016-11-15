%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-firewall
%global commit 46a61192f73aad42f9ec9905d42895c089b0508b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-firewall
Version:        1.8.1
Release:        2%{?alphatag}%{?dist}
Summary:        Manages Firewalls such as iptables
License:        Apache-2.0

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
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 1.8.1-2.46a6119.git
- Newton update 1.8.1 (46a61192f73aad42f9ec9905d42895c089b0508b)

* Wed Sep 21 2016 Haikel Guemar <hguemar@fedoraproject.org> - 1.8.1-1.e70157e.git
- Newton update 1.8.1 (e70157ef0692b679470a980d7051c4b73000ed9f)


