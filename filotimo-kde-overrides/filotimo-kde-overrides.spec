Name:           filotimo-kde-overrides
Version:        1.2
Release:        1%{?dist}
Summary:        KDE defaults for Filotimo
URL:            https://github.com/filotimo-linux/filotimo-core-packages
Source0:        %URL/releases/download/latest/filotimo-kde-overrides.tar.gz
BuildArch:      noarch
License:        GPLv2+

Requires:       rsms-inter-fonts
Requires:       ibm-plex-fonts-all
#Requires:       filotimo-atychia TODO: Not packaged yet
Obsoletes:      plasma-discover-offline-updates
Provides:       plasma-discover-offline-updates

%description
KDE defaults for Filotimo

%define debug_package %{nil}

%prep
%setup -T -b 0 -q -n filotimo-kde-overrides

%install
mkdir -p %{buildroot}%{_sysconfdir}/
mkdir -p %{buildroot}%{_datadir}/
cp -rv etc/* %{buildroot}%{_sysconfdir}
cp -rv usr/share/* %{buildroot}%{_datadir}

%files
%license LICENSE
%{_sysconfdir}/xdg/*
%{_sysconfdir}/sddm.conf.d/*
%{_datadir}/share/applications/org.filotimo.atychia.desktop
%{_datadir}/share/kglobalaccel/org.filotimo.atychia.desktop

%changelog
