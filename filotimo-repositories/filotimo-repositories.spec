Name:		filotimo-repositories
Version:	1.0
Release:	1%{?dist}
Summary:	Provides RPMFusion and sentry/kernel-fsync
BuildArch:  noarch
License:	MIT
URL:        https://github.com/filotimo-linux/filotimo-core-packages
Source0:    %URL/releases/download/latest/filotimo-repositories.tar.gz

# For rpmfusion-nonfree repo keys
# rpmfusion-free/nonfree-release is never being installed, so repo files take GPG keys from here
Requires:	distribution-gpg-keys

# For /etc/yum.repos.d
Requires:	fedora-repos

# Replaces stripped down RPMFusion repositories that are included by default
Obsoletes:  fedora-workstation-repositories
# This is the tool that allows you to enable third party repositories
# - we don't want this, we simply want them to be enabled regardless
Obsoletes:  fedora-third-party

%description
Repositories to allow the installation of software not packaged with Fedora.
Enables RPMFusion and sentry/kernel-fsync, installing a patched kernel.

%prep
%setup -T -b 0 -q -n filotimo-repositories

%install
mkdir -p %{buildroot}%{_sysconfdir}/
cp -rv etc/* %{buildroot}%{_sysconfdir}

%post
if [ $1 -gt 1 ] ; then
    dnf update -y @core
    dnf config-manager --enable -y fedora-cisco-openh264
fi

%files
%license LICENSE
%{_sysconfdir}/yum.repos.d/*

%changelog
