# Force out of source build
%undefine __cmake_in_source_build

Name:		filotimo-dnfdragora
Version:	2.1.6
Release:	4%{?dist}
Summary:	DNF package-manager based on libYui abstraction

License:	GPLv3+
URL:		https://github.com/manatools/dnfdragora
Source0:	%{url}/archive/%{version}/dnfdragora-%{version}.tar.gz
Patch0:     01-filotimo.patch

BuildArch:	noarch

BuildRequires:	cmake			>= 3.4.0
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:	pkgconfig
BuildRequires:	python3-devel		>= 3.4.0
BuildRequires:	python3-dnfdaemon	>= 0.3.20
BuildRequires:	python3-manatools	>= 0.0.3
BuildRequires:	python3-PyYAML
BuildRequires:	python3-setuptools
BuildRequires:	python3-sphinx
BuildRequires:	python3-yui
BuildRequires:	python3-pyxdg
BuildRequires:	python3-cairosvg
BuildRequires:	python3-pillow
BuildRequires:	python3-pystray		>= 0.16

Requires:	dnf			>= 1.0.9
Requires:	filesystem
Requires:	comps-extras
Requires:	hicolor-icon-theme
Requires:	libyui-mga-ncurses
Requires:	python3-dnfdaemon	>= 0.3.20
Requires:	python3-manatools	>= 0.0.3
Requires:	python3-PyYAML
Requires:	python3-yui		>= 1.1.1-10

Provides:	dnfdragora-gui		= %{version}-%{release}
Recommends:	(libyui-mga-qt if qt5-qtbase-gui)
Recommends:	(libyui-mga-gtk if gtk3)

Provides:       dnfdragora
Conflicts:	dnfdragora

%description
dnfdragora is a DNF frontend, based on rpmdragora from Mageia
(originally rpmdrake) Perl code.

dnfdragora is written in Python 3 and uses libYui, the widget
abstraction library written by SUSE, so that it can be run
using Qt 5, GTK+ 3, or ncurses interfaces.

%prep
%autosetup -p 1 -n dnfdragora-%{version}


%build
%cmake \
  -DCHECK_RUNTIME_DEPENDENCIES=ON \
  -DENABLE_COMPS=ON               \
  %{nil}
%cmake_build

%install
%cmake_install
%find_lang dnfdragora


%check
# Validate desktop-files.
desktop-file-validate				\
	%{buildroot}%{_datadir}/applications/*.desktop

%files -f dnfdragora.lang
%config(noreplace) %{_sysconfdir}/dnfdragora/dnfdragora.yaml
%dir %{_sysconfdir}/dnfdragora
%doc README.md dnfdragora.yaml*.example
%license AUTHORS LICENSE
%{_bindir}/dnfdragora
%{_datadir}/applications/*dnfdragora.desktop
%{_datadir}/dnfdragora
%{_mandir}/man5/dnfdragora*.5*
%{_mandir}/man8/dnfdragora*.8*
%dir %{python3_sitelib}/dnfdragora
%{python3_sitelib}/dnfdragora/*

%changelog
