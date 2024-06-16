Name:           filotimo-kde-overrides
Version:        1.4
Release:        1%{?dist}
Summary:        KDE defaults for Filotimo
URL:            https://github.com/filotimo-linux/filotimo-core-packages

Source0:        LICENSE
# KDE global config files
Source1:        discoverrc
Source2:        kded5rc
Source3:        kded_device_automounterrc
Source4:        kdeglobals
Source5:        kdesurc
Source6:        krunnerrc
Source7:        ksplashrc
Source8:        kuriikwsfilterrc
Source9:        kwinrc
Source10:       kwriterc
Source11:       spectaclerc
# SDDM config files
Source21:       10-filotimo-kde-overrides.conf

BuildArch:      noarch
License:        GPLv2+

Requires:       rsms-inter-fonts
Requires:       ibm-plex-fonts-all
Obsoletes:      plasma-discover-offline-updates
Provides:       plasma-discover-offline-updates

%description
KDE defaults for Filotimo

%define debug_package %{nil}

%prep

%install
install -pm 0644 %{SOURCE0} LICENSE

mkdir -p %{buildroot}%{_sysconfdir}/xdg/
mkdir -p %{buildroot}%{_sysconfdir}/sddm.conf.d/

install -t %{buildroot}%{_sysconfdir}/xdg/ %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11}
install -t %{buildroot}%{_sysconfdir}/sddm.conf.d/ %{SOURCE21}

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/xdg/discoverrc
%config(noreplace) %{_sysconfdir}/xdg/kded5rc
%config(noreplace) %{_sysconfdir}/xdg/kded_device_automounterrc
%config(noreplace) %{_sysconfdir}/xdg/kdeglobals
%config(noreplace) %{_sysconfdir}/xdg/kdesurc
%config(noreplace) %{_sysconfdir}/xdg/krunnerrc
%config(noreplace) %{_sysconfdir}/xdg/ksplashrc
%config(noreplace) %{_sysconfdir}/xdg/kuriikwsfilterrc
%config(noreplace) %{_sysconfdir}/xdg/kwinrc
%config(noreplace) %{_sysconfdir}/xdg/kwriterc
%config(noreplace) %{_sysconfdir}/xdg/spectaclerc
%config(noreplace) %{_sysconfdir}/sddm.conf.d/10-filotimo-kde-overrides.conf

%changelog
