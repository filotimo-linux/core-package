Name:           filotimo-repos-nonfree
Version:        40
Release:        3%{?dist}
Summary:        Provides RPMFusion nonfree
BuildArch:      noarch
License:        MIT
URL:            https://github.com/filotimo-linux/filotimo-core-packages
Source0:        %URL/releases/download/latest/filotimo-repos-nonfree.tar.gz

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
Repositories enabling the installation of nonfree software, through RPMFusion nonfree.

%prep
%setup -T -b 0 -q -n filotimo-repos-nonfree

%install
mkdir -p %{buildroot}%{_sysconfdir}/
cp -rv etc/* %{buildroot}%{_sysconfdir}

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/yum.repos.d/*

%changelog
