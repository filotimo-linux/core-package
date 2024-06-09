Name:           filotimo-environment
Version:        1.2
Release:        2%{?dist}
Summary:        Environment variables and sysctl configuration for Filotimo
URL:            https://github.com/filotimo-linux/filotimo-core-packages
Source0:        %URL/releases/download/latest/filotimo-environment.tar.gz
BuildArch:      noarch
License:        GPLv2+
Requires:       flatpak

# Fonts to install as part of the environment
Requires:       rsms-inter-fonts
Requires:       rsms-inter-vf-fonts
Requires:       ibm-plex-fonts-all

%description
Environment variables and sysctl configuration for Filotimo.

%define debug_package %{nil}

%prep
%setup -T -b 0 -q -n filotimo-environment

%install
mkdir -p %{buildroot}%{_sysconfdir}/
mkdir -p %{buildroot}%{_sharedstatedir}/
cp -rv etc/* %{buildroot}%{_sysconfdir}
cp -rv var/lib/* %{buildroot}%{_sharedstatedir}

%files
%license LICENSE
%{_sysconfdir}/profile.d/*
%{_sysconfdir}/sysctl.d/*
%{_sysconfdir}/fonts/conf.d/*
%{_sharedstatedir}/flatpak/overrides/*

%changelog
