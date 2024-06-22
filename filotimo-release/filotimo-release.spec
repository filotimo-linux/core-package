
%define release_name Forty
%define is_rawhide 0

%define eol_date 2025-05-13

%define dist_version 40
%define rhel_dist_version 10

%if %{is_rawhide}
%define bug_version rawhide
%if 0%{?eln}
  %define releasever eln
%else
  %define releasever rawhide
%endif
%define doc_version rawhide
%else
%define bug_version %{dist_version}
%define releasever %{dist_version}
%define doc_version f%{dist_version}
%endif

%if 0%{?eln}
%bcond_with basic
%bcond_without eln
%bcond_with kde
%bcond_with workstation
%else
%bcond_with eln
%bcond_without kde
%bcond_without workstation
%endif

%if %{with silverblue} || %{with kinoite} || %{with sway_atomic} || %{with budgie_atomic}
%global with_ostree_desktop 1
%endif

%global dist %{?eln:.eln%{eln}}

Summary:        Filotimo release files
Name:           filotimo-release
Version:        40
# The numbering is 0.<r> before a given Fedora Linux release is released,
# with r starting at 1, and then just <r>, with r starting again at 1.
# Use '%%autorelease -p' before final, and then drop the '-p'.
#Release:        %autorelease
Release:        6%{?dist}
License:        MIT
URL:            https://github.com/filotimo-linux

Source1:        LICENSE
Source2:        Fedora-Legal-README.txt

Source10:       85-display-manager.preset
Source11:       90-default.preset
Source12:       90-default-user.preset
Source13:       99-default-disable.preset
Source14:       80-server.preset
Source15:       80-workstation.preset
Source16:       org.gnome.shell.gschema.override
Source17:       org.projectatomic.rpmostree1.rules
Source18:       80-iot.preset
Source19:       distro-template.swidtag
Source20:       distro-edition-template.swidtag
Source21:       fedora-workstation.conf
Source22:       80-coreos.preset
Source23:       zezere-ignition-url
Source24:       80-iot-user.preset
Source25:       plasma-desktop.conf
Source26:       80-kde.preset
Source27:       81-desktop.preset
Source28:       longer-default-shutdown-timeout.conf
Source29:       org.gnome.settings-daemon.plugins.power.gschema.override

BuildArch:      noarch

Provides:       filotimo-release = %{version}-%{release}
Provides:       filotimo-release-variant = %{version}-%{release}
Obsoletes:      fedora-release = %{version}-%{release}
Obsoletes:      fedora-release-variant = %{version}-%{release}


Provides:       system-release
Provides:       fedora-release = %{version}-%{release}
Provides:       system-release(%{version})
Requires:       filotimo-release-common = %{version}-%{release}
#Requires:       filotimo-login -- TODO: This doesn't exist yet

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-basic if nothing else is already doing so.
Recommends:     filotimo-release-identity-basic


BuildRequires:  redhat-rpm-config > 121-1
BuildRequires:  systemd-rpm-macros

%description
Filotimo release files such as various /etc/ files that define the release
and systemd preset files that determine which services are enabled by default.
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/DefaultServices/ for details.


%package common
Summary: Filotimo release files

Requires:   filotimo-release-variant = %{version}-%{release}
Suggests:   filotimo-release

Requires:   fedora-repos(%{version})
Requires:   filotimo-release-identity = %{version}-%{release}
Provides:	filotimo-release-common = %{version}-%{release}
Obsoletes:	fedora-release-common

%if %{is_rawhide}
# Make $releasever return "rawhide" on Rawhide
# https://pagure.io/releng/issue/7445
Provides:       system-release(releasever) = %{releasever}
%endif

# Fedora ships a generic-release package to make the creation of Remixes
# easier, but it cannot coexist with the fedora-release[-*] packages, so we
# will explicitly conflict with it.
Conflicts:  generic-release

# rpm-ostree count me is now enabled in 90-default.preset
Obsoletes: fedora-release-ostree-counting <= 36-0.7

%description common
Release files common to all Editions and Spins of Filotimo


%if %{with basic}
%package identity-basic
Summary:        Package providing the basic Filotimo identity

RemovePathPostfixes: .basic
Provides:       filotimo-release-identity = %{version}-%{release}
Obsoletes:      fedora-release-identity
Conflicts:      filotimo-release-identity

%description identity-basic
Provides the necessary files for a Filotimo installation that is not identifying
itself as a particular Edition or Spin.
%endif

# TODO
%if %{with eln}
%package eln
Summary:        Base package for Filotimo ELN specific default configurations

RemovePathPostfixes: .eln
Provides:       filotimo-release = %{version}-%{release}
Provides:       filotimo-release-variant = %{version}-%{release}
Provides:       fedora-release = %{version}-%{release}
Provides:       fedora-release-variant = %{version}-%{release}
Obsoletes:      fedora-release
Obsoletes:      fedora-release-variant
Provides:       system-release
Provides:       system-release(%{version})
Requires:       filotimo-release-common = %{version}-%{release}
Provides:       system-release-product
Requires:       fedora-repos-eln

Obsoletes:      redhat-release
Provides:       redhat-release

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-eln if nothing else is already doing so.
Recommends:     filotimo-release-identity-eln


%description eln
Provides a base package for Filotimo ELN specific configuration files to
depend on.


%package identity-eln
Summary:        Package providing the identity for Filotimo ELN

# When running a compose for ELN, we want to make sure that we pull in the
# correct templates when lorax is installed. This Suggests: will clue
# libdnf to use this set of templates instead of lorax-templates-generic.
Suggests: lorax-templates-rhel

# Both netcat and nmap-ncat provide /usr/bin/nc, so prefer the latter like
# RHEL does.
Suggests: nmap-ncat

# Prefer over original standalone versions (without pipewire- prefix)
Suggests: pipewire-jack-audio-connection-kit
Suggests: pipewire-jack-audio-connection-kit-devel
Suggests: pipewire-pulseaudio

# Prefer over Lmod for Provides: environment(modules)
Suggests: environment-modules

# Prefer over elinks, w3m for Provides: text-www-browser
Suggests: lynx

# Prefer over bind9-next and its subpackages
Suggests: bind
Suggests: bind-devel
Suggests: bind-dnssec-utils
Suggests: bind-utils

# Default OpenJDK version, prefer over other versions for
# Provides: java, java-devel, java-headless, maven-jdk-binding, etc.
Suggests: java-17-openjdk
Suggests: java-17-openjdk-devel
Suggests: java-17-openjdk-headless
Suggests: maven-openjdk17

# Prefer over Fedora freeipa (same code, different name, each Provides the other)
Suggests: ipa-client
Suggests: ipa-client-common
Suggests: ipa-client-epn
Suggests: ipa-client-samba
Suggests: ipa-common
Suggests: ipa-selinux
Suggests: ipa-server
Suggests: ipa-server-common
Suggests: ipa-server-dns
Suggests: ipa-server-trust-ad
Suggests: ipa-healthcheck
Suggests: ipa-healthcheck-core

# Prefer over exim, opensmtpd, sendmail for Provides: MTA smtpd smtpdaemon server(smtp)
Suggests: postfix

# Prefer over cdrkit/genisoimage for /usr/bin/mkisofs
Suggests: xorriso

# Prefer over wget-1.x for /usr/bin/wget
Suggests: wget2-wget

# Prefer over zlib, zlib-devel, zlib-static
Suggests: zlib-ng-compat
Suggests: zlib-ng-compat-devel
Suggests: zlib-ng-compat-static

# Prefer over sdubby which also Provides: grubby
Suggests: grubby

# Prefer over arptables-legacy, ebtables-legacy, and iptables-legacy
# for Provides: arptables-helper, ebtables, or iptables
Suggests: iptables-nft

# Prefer over blis for libblas*.so.3()(64bit)
Suggests: blas
Suggests: blas64

RemovePathPostfixes: .eln
Provides:       filotimo-release-identity = %{version}-%{release}
Conflicts:      fedora-release-identity
Obsoletes:      fedora-release-identity


%description identity-eln
Provides the necessary files for a Filotimo installation that is identifying
itself as Filotimo ELN.
%endif

%if %{with kde}
%package kde
Summary:        Base package for Filotimo KDE Plasma-specific default configurations

RemovePathPostfixes: .kde
Provides:       filotimo-release = %{version}-%{release}
Provides:       filotimo-release-kde
Provides:       filotimo-release-variant = %{version}-%{release}
Provides:       filotimo-release = %{version}-%{release}
Provides:       filotimo-release-variant = %{version}-%{release}
Obsoletes:       fedora-release
Obsoletes:       fedora-release-variant
Obsoletes:       fedora-release-kde
Provides:       system-release
Provides:       system-release(%{version})
Requires:       filotimo-release-common = %{version}-%{release}

# fedora-release-common Requires: fedora-release-identity, so at least one
# package must provide it. This Recommends: pulls in
# fedora-release-identity-kde if nothing else is already doing so.
Recommends:     filotimo-release-identity-kde


%description kde
Provides a base package for Filotimo KDE Plasma-specific configuration files to
depend on as well as KDE Plasma system defaults.


%package identity-kde
Summary:        Package providing the identity for Filotimo KDE Plasma Spin

RemovePathPostfixes: .kde
Provides:       filotimo-release-identity = %{version}-%{release}
Provides:       filotimo-release-identity-kde
Obsoletes:       fedora-release-identity
Obsoletes:       fedora-release-identity-kde
Conflicts:      fedora-release-identity


%description identity-kde
Provides the necessary files for a Filotimo installation that is identifying
itself as Filotimo (KDE will be the only version of Filotimo)
%endif

%prep
mkdir -p licenses
sed 's|@@VERSION@@|%{dist_version}|g' %{SOURCE2} >licenses/Fedora-Legal-README.txt

%build

%install
install -d %{buildroot}%{_prefix}/lib
echo "Filotimo release %{version} (%{release_name})" > %{buildroot}%{_prefix}/lib/filotimo-release
echo "cpe:/o:fedoraproject:fedora:%{version}" > %{buildroot}%{_prefix}/lib/system-release-cpe

# Symlink the -release files
install -d %{buildroot}%{_sysconfdir}
ln -s ../usr/lib/filotimo-release %{buildroot}%{_sysconfdir}/filotimo-release
ln -s ../usr/lib/system-release-cpe %{buildroot}%{_sysconfdir}/system-release-cpe
ln -s filotimo-release %{buildroot}%{_sysconfdir}/redhat-release
ln -s filotimo-release %{buildroot}%{_sysconfdir}/system-release

# Create the common os-release file
%{lua:
  function starts_with(str, start)
   return str:sub(1, #start) == start
  end
}
%define starts_with(str,prefix) (%{expand:%%{lua:print(starts_with(%1, %2) and "1" or "0")}})
%if %{starts_with "a%{release}" "a0"}
  %global prerelease \ Prerelease
%endif

# -------------------------------------------------------------------------
# Definitions for /etc/os-release and for macros in macros.dist.  These
# macros are useful for spec files where distribution-specific identifiers
# are used to customize packages.

# Name of vendor / name of distribution. Typically used to identify where
# the binary comes from in --help or --version messages of programs.
# Examples: gdb.spec, clang.spec
%global dist_vendor Filotimo
%global dist_name   Filotimo Linux

# URL of the homepage of the distribution
# Example: gstreamer1-plugins-base.spec
%global dist_home_url https://github.com/filotimo-linux/

# Bugzilla / bug reporting URLs shown to users.
# Examples: gcc.spec
%global dist_bug_report_url https://github.com/filotimo-linux/

# debuginfod server, as used in elfutils.spec.
%global dist_debuginfod_url https://github.com/filotimo-linux/
# -------------------------------------------------------------------------

cat << EOF >> os-release
NAME="Filotimo Linux"
VERSION="%{dist_version} (%{release_name}%{?prerelease})"
ID=filotimo
ID_LIKE="rhel centos fedora"
VERSION_ID=%{dist_version}
VERSION_CODENAME=""
PLATFORM_ID="platform:f%{dist_version}"
PRETTY_NAME="Filotimo Linux %{dist_version} (%{release_name}%{?prerelease})"
ANSI_COLOR="0;38;2;60;110;180"
LOGO=fedora-logo-icon
CPE_NAME="cpe:/o:filotimoproject:filotimo:%{dist_version}"
DEFAULT_HOSTNAME="filotimo"
HOME_URL="%{dist_home_url}"
DOCUMENTATION_URL="https://github.com/filotimo-linux/"
SUPPORT_URL="https://github.com/filotimo-linux/"
BUG_REPORT_URL="%{dist_bug_report_url}"
REDHAT_BUGZILLA_PRODUCT="Filotimo"
REDHAT_BUGZILLA_PRODUCT_VERSION=%{bug_version}
REDHAT_SUPPORT_PRODUCT="Filotimo"
REDHAT_SUPPORT_PRODUCT_VERSION=%{bug_version}
SUPPORT_END=%{eol_date}
EOF

# Create the common /etc/issue
echo "\S" > %{buildroot}%{_prefix}/lib/issue
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue
echo >> %{buildroot}%{_prefix}/lib/issue
ln -s ../usr/lib/issue %{buildroot}%{_sysconfdir}/issue

# Create /etc/issue.net
echo "\S" > %{buildroot}%{_prefix}/lib/issue.net
echo "Kernel \r on an \m (\l)" >> %{buildroot}%{_prefix}/lib/issue.net
ln -s ../usr/lib/issue.net %{buildroot}%{_sysconfdir}/issue.net

# Create /etc/issue.d
mkdir -p %{buildroot}%{_sysconfdir}/issue.d

mkdir -p %{buildroot}%{_swidtagdir}

# Create os-release files for the different editions

%if %{with basic}
# Basic
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.basic
%endif

%if %{with eln}
# ELN
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.eln
echo "VARIANT=\"ELN\"" >> %{buildroot}%{_prefix}/lib/os-release.eln
echo "VARIANT_ID=eln" >> %{buildroot}%{_prefix}/lib/os-release.eln
sed -i -e 's|PLATFORM_ID=.*|PLATFORM_ID="platform:eln"|' %{buildroot}/%{_prefix}/lib/os-release.eln
sed -i -e 's|PRETTY_NAME=.*|PRETTY_NAME="Fedora ELN"|' %{buildroot}/%{_prefix}/lib/os-release.eln
sed -i -e 's|DOCUMENTATION_URL=.*|DOCUMENTATION_URL="https://docs.fedoraproject.org/en-US/eln/"|' %{buildroot}%{_prefix}/lib/os-release.eln
sed -i -e "/^DEFAULT_HOSTNAME=/d" %{buildroot}%{_prefix}/lib/os-release.eln
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/ELN/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.eln
%endif

%if %{with kde}
# KDE Plasma
cp -p os-release \
      %{buildroot}%{_prefix}/lib/os-release.kde
echo "VARIANT=\"KDE Plasma\"" >> %{buildroot}%{_prefix}/lib/os-release.kde
echo "VARIANT_ID=kde" >> %{buildroot}%{_prefix}/lib/os-release.kde
sed -i -e "s|(%{release_name}%{?prerelease})|(KDE Plasma%{?prerelease})|g" %{buildroot}%{_prefix}/lib/os-release.kde
sed -e "s#\$version#%{bug_version}#g" -e 's/$edition/KDE/;s/<!--.*-->//;/^$/d' %{SOURCE20} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kde
# Add plasma-desktop to dnf protected packages list for KDE
install -Dm0644 %{SOURCE25} -t %{buildroot}%{_sysconfdir}/dnf/protected.d/
%endif

%if %{with kde} || %{with kinoite}
# Common desktop preset and spin specific preset
install -Dm0644 %{SOURCE26} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE27} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
%endif

# Create the symlink for /etc/os-release
ln -s ../usr/lib/os-release %{buildroot}%{_sysconfdir}/os-release

# Set up the dist tag macros
install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d
cat >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.dist << EOF
# dist macros.

%%__bootstrap         ~bootstrap
%if 0%{?eln}
%%rhel              %{rhel_dist_version}
%%el%{rhel_dist_version}                1
# Although eln is set in koji tags, we put it in the macros.dist file for local and mock builds.
%%eln              %{eln}
%%distcore            .eln%%{eln}
%else
%%fedora              %{dist_version}
%%fc%{dist_version}                1
%%distcore            .fc%%{fedora}
%endif
%%dist                %%{!?distprefix0:%%{?distprefix}}%%{expand:%%{lua:for i=0,9999 do print("%%{?distprefix" .. i .."}") end}}%%{distcore}%%{?with_bootstrap:%%{__bootstrap}}
%%dist_vendor         %{dist_vendor}
%%dist_name           %{dist_name}
%%dist_home_url       %{dist_home_url}
%%dist_bug_report_url %{dist_bug_report_url}
%%dist_debuginfod_url %{dist_debuginfod_url}
EOF

# Install licenses
install -pm 0644 %{SOURCE1} licenses/LICENSE

# Default system wide
install -Dm0644 %{SOURCE10} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE11} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE12} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/
# The same file is installed in two places with identical contents
install -Dm0644 %{SOURCE13} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE13} -t %{buildroot}%{_prefix}/lib/systemd/user-preset/

# Create distro-level SWID tag file
install -d %{buildroot}%{_swidtagdir}
sed -e "s#\$version#%{bug_version}#g" -e 's/<!--.*-->//;/^$/d' %{SOURCE19} > %{buildroot}%{_swidtagdir}/org.fedoraproject.Fedora-%{bug_version}.swidtag
install -d %{buildroot}%{_sysconfdir}/swid/swidtags.d
ln -s --relative %{buildroot}%{_swidtagdir} %{buildroot}%{_sysconfdir}/swid/swidtags.d/fedoraproject.org


%files common
%license licenses/LICENSE licenses/Fedora-Legal-README.txt
%{_prefix}/lib/filotimo-release
%{_prefix}/lib/system-release-cpe
%{_sysconfdir}/os-release
%{_sysconfdir}/filotimo-release
%{_sysconfdir}/redhat-release
%{_sysconfdir}/system-release
%{_sysconfdir}/system-release-cpe
%attr(0644,root,root) %{_prefix}/lib/issue
%config(noreplace) %{_sysconfdir}/issue
%attr(0644,root,root) %{_prefix}/lib/issue.net
%config(noreplace) %{_sysconfdir}/issue.net
%dir %{_sysconfdir}/issue.d
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist
%dir %{_prefix}/lib/systemd/user-preset/
%{_prefix}/lib/systemd/user-preset/90-default-user.preset
%{_prefix}/lib/systemd/user-preset/99-default-disable.preset
%dir %{_prefix}/lib/systemd/system-preset/
%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset
%dir %{_swidtagdir}
%{_swidtagdir}/org.fedoraproject.Fedora-%{bug_version}.swidtag
%dir %{_sysconfdir}/swid
%{_sysconfdir}/swid/swidtags.d


%if %{with basic}
%files
%files identity-basic
%{_prefix}/lib/os-release.basic
%endif

%if %{with eln}
%files eln
%files identity-eln
%{_prefix}/lib/os-release.eln
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.eln
%endif

%if %{with kde}
%files kde
%files identity-kde
%{_prefix}/lib/os-release.kde
%{_prefix}/lib/systemd/system-preset/80-kde.preset
%{_prefix}/lib/systemd/system-preset/81-desktop.preset
%attr(0644,root,root) %{_swidtagdir}/org.fedoraproject.Fedora-edition.swidtag.kde
%{_sysconfdir}/dnf/protected.d/plasma-desktop.conf
%endif

%changelog
