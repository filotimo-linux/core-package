Name:           filotimo-environment
Version:        1.0
Release:        1%{?dist}
Summary:        Environment variables and sysctl configuration for Filotimo
URL:            https://github.com/filotimo-linux/filotimo-core-packages
Source0:        %URL/releases/download/1.0/filotimo-environment.tar.gz
BuildArch:      noarch
License:        GPLv2+

%description
Environment variables and sysctl configuration for Filotimo

%define debug_package %{nil}

%prep
%setup -T -b 0 -q -n filotimo-environment

%install
mkdir -p %{buildroot}%{_sysconfdir}/
cp -rv etc/* %{buildroot}%{_sysconfdir}

%files
%license LICENSE
%{_sysconfdir}/profile.d/*
%{_sysconfdir}/sysctl.d/*

%changelog
