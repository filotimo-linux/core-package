Name:           filotimo-kde-overrides
Version:        1.10
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
Source12:       12-filotimo-kde-policy.rules
# SDDM config files
Source21:       10-filotimo-kde-overrides.conf
# look-and-feel
Source31:       metadata.json
Source32:       defaults
Source33:       org.kde.plasma.kickoff.js
Source34:       org.kde.plasma.desktop-layout.js

BuildArch:      noarch
License:        GPLv2+

Requires:       rsms-inter-fonts
Requires:       ibm-plex-fonts-all
Requires:       plasma-workspace
# stupid for just one folder
BuildRequires:  plasma-workspace
Obsoletes:      plasma-discover-offline-updates
Provides:       plasma-discover-offline-updates

# plasma-lookandfeel-fedora
BuildRequires:  kf6-rpm-macros
Requires:       qt6-qtvirtualkeyboard
Provides:       plasma-lookandfeel-fedora
Obsoletes:      plasma-lookandfeel-fedora

%description
KDE defaults for Filotimo

%define debug_package %{nil}

%prep

%install
install -pm 0644 %{SOURCE0} LICENSE

mkdir -p %{buildroot}%{_sysconfdir}/xdg/
mkdir -p %{buildroot}%{_sysconfdir}/sddm.conf.d/
mkdir -p %{buildroot}%{_datadir}/polkit-1/rules.d

install -t %{buildroot}%{_sysconfdir}/xdg/ %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11}
install -t %{buildroot}%{_sysconfdir}/sddm.conf.d/ %{SOURCE21}
install -t %{buildroot}%{_datadir}/polkit-1/rules.d/ %{SOURCE12}

# plasma-lookandfeel-fedora
mkdir -p %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop
mkdir -p %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop/contents

cp -r %{_kf6_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop

rm -f %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop/metadata.json
install -t %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop/ %{SOURCE31}

rm -f %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop/defaults
install -t %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop/contents/ %{SOURCE32}

mkdir -p %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop/contents/plasmoidsetupscripts/
install -t %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop/contents/plasmoidsetupscripts/ %{SOURCE33}

mkdir -p %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop/contents/layouts
install -t %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop/contents/layouts/ %{SOURCE34}

%post

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
%{_datadir}/polkit-1/rules.d/12-filotimo-kde-policy.rules
# plasma-lookandfeel-fedora
%{_kf6_datadir}/plasma/look-and-feel/org.filotimolinux.filotimo.desktop

%changelog
