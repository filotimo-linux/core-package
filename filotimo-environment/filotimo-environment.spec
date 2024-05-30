Name:           filotimo-environment
Version:        1.1
Release:        1%{?dist}
Summary:        Environment variables and sysctl configuration for Filotimo
URL:            https://github.com/filotimo-linux/filotimo-core-packages
Source0:        %URL/releases/download/latest/filotimo-environment.tar.gz
BuildArch:      noarch
License:        GPLv2+
Requires:       flatpak

%description
Environment variables and sysctl configuration for Filotimo.

%define debug_package %{nil}

%prep
%setup -T -b 0 -q -n filotimo-environment

%install
mkdir -p %{buildroot}%{_sysconfdir}/
mkdir -p %{buildroot}%{_sharedstatedir}/flatpak/overrides/
cp -rv etc/* %{buildroot}%{_sysconfdir}
cp -rv var/lib/* %{buildroot}%{_sharedstatedir}

%files
%license LICENSE
%{_sysconfdir}/profile.d/*
%{_sysconfdir}/sysctl.d/*
%{_sharedstatedir}/flatpak/overrides/*

%changelog
