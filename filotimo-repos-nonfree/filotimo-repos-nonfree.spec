Name:           filotimo-repos-nonfree
Version:        40
Release:        3%{?dist}
Summary:        Provides RPMFusion nonfree
BuildArch:      noarch
License:        MIT
URL:            https://github.com/filotimo-linux/filotimo-core-packages
Source0:        LICENSE
Source1:        rpmfusion-nonfree.repo
Source2:        rpmfusion-nonfree-updates.repo
Source3:        rpmfusion-nonfree-updates-testing.repo

# For rpmfusion-nonfree repo keys
# rpmfusion-free/nonfree-release is never being installed, so repo files take GPG keys from here
Requires:       distribution-gpg-keys

# For /etc/yum.repos.d
Requires:       filotimo-repos

# Replaces stripped down RPMFusion repositories that are included by default
Obsoletes:      fedora-workstation-repositories
Provides:       fedora-workstation-repositories

# So tainted repos and rawhide can be installed w/o package conflicts
Obsoletes:      rpmfusion-nonfree-release
Provides:       rpmfusion-nonfree-release

Obsoletes:      filotimo-repositories

%description
Repositories enabling the installation of nonfree software, through RPMFusion

%define debug_package %{nil}

%prep

%install
install -pm 0644 %{SOURCE0} LICENSE

mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d

install -t %{buildroot}%{_sysconfdir}/yum.repos.d/ %{SOURCE1} %{SOURCE2} %{SOURCE3}

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-nonfree.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-nonfree-updates.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/rpmfusion-nonfree-updates-testing.repo

%changelog
