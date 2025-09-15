#
# spec file for package koi
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define original_name Koi

# Define CMake Flags for DEB-Based Linux Distributions
%define _cmake_flags -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
#

Name:           koi
Version:        0.6
Release:        0
Summary:        Scheduled LIGHT/DARK Theme Switching for the KDE Plasma Desktop
License:        LGPL-3.0-only
URL:            https://github.com/baduhai/Koi
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Builds for SUSE Leap 15.6-
%if 0%{?sle_version} <= 150600 && 0%{?is_opensuse}
Patch0:         QT-5_Build.patch

BuildRequires:  cmake  cmake-full
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)

Requires:       (plasma-desktop   or plasma5-desktop)
Requires:       (plasma-workspace or plasma5-workspace)
Requires:       (plasma-framework or plasma5-framework)
%endif
#

# Builds for SUSE Leap 16.0, SUSE TumbleWeed, SUSE SlowRoll
%if 0%{?suse_version} > 1600 || 0%{?suse_version} == 1600 && 0%{?is_opensuse}
BuildRequires:  cmake  cmake-full  kf6-extra-cmake-modules
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  qt6-base-private-devel
BuildRequires:  qt6-gui-private-devel

Requires:       (plasma-desktop   or plasma6-desktop)
Requires:       (plasma-workspace or plasma6-workspace)
%endif
#

# Builds for Fedora 40+ / RawHide
%if 0%{?fedora} >= 40
BuildRequires:  cmake  cmake-fedora  extra-cmake-modules
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

Requires:       (plasma-desktop   or plasma6-desktop)
Requires:       (plasma-workspace or plasma6-workspace)
%endif
#

# Builds for Mageia 9 (Stable)
%if 0%{?mageia} == 9
Patch0:         QT-5_Build.patch

BuildRequires:  cmake  cmake-rpm-macros  extra-cmake-modules
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)

Requires:       (plasma-framework   or plasma5-framework or kf5-plasma-framework)
Requires:       (plasma-desktop     or plasma5-desktop)
Requires:       (plasma-integration or plasma5-integration)
Requires:       (plasma-workspace   or plasma5-workspace)
%endif
#

# Builds for Mageia 10+ / Cauldron
%if 0%{?mageia} >= 10
BuildRequires:  cmake  cmake-rpm-macros  extra-cmake-modules
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

Requires:       (plasma-desktop     or plasma6-desktop)
Requires:       (plasma-framework   or plasma6-framework)
Requires:       (plasma-integration or plasma6-integration)
Requires:       (plasma-workspace   or plasma6-workspace)
%endif
#

# Builds for Debian-Based (DebBuild) Linux Distributions:
%if "%{_vendor}" == "debbuild"
Packager: Martin Stibor <martin.von.reichenberg@proton.me>
Group:    KDE
Priority: optional

# Builds for Debian 12 - Bookworm (Stable)
%if "%{_repository}" == "Debian_debbuild_Debian_12"
Patch0:         QT-5_Build.patch

BuildRequires:  g++
BuildRequires:  cmake  cmake-extras  extra-cmake-modules
BuildRequires:  libkf5config-dev
BuildRequires:  libkf5coreaddons-dev
BuildRequires:  libkf5dbusaddons-dev
BuildRequires:  libkf5widgetsaddons-dev
BuildRequires:  qtbase5-dev

Requires:       libc6
Requires:       libgcc-s1
Requires:       libkf5coreaddons5
Requires:       libkf5widgetsaddons5
Requires:       libqt5core5
Requires:       libqt5dbus5
Requires:       libqt5gui5
Requires:       libqt5widgets5
Requires:       libstdc++6
Requires:       libkf5configcore5
Requires:       libkf5config-data
Requires:       libkf5configgui5
Requires:       libkf5guiaddons5
Requires:       libkf5guiaddons-data
Requires:       libkf5coreaddons-data
Requires:       libkf5dbusaddons5
Requires:       libkf5dbusaddons-data
Requires:       libqt5test5
Requires:       libkf5widgetsaddons-data
Requires:       libqt5xml5
Requires:       libqt5xmlpatterns5
Requires:       plasma-desktop
%endif
#

# Builds for Debian 13 - Trixie (Testing)
%if "%{_repository}" == "Debian_debbuild_Debian_Testing"
BuildRequires:  g++
BuildRequires:  cmake  cmake-extras  extra-cmake-modules
BuildRequires:  libkf6config-dev
BuildRequires:  libkf6coreaddons-dev
BuildRequires:  libkf6dbusaddons-dev
BuildRequires:  libkf6widgetsaddons-dev
BuildRequires:  qt6-base-dev

Requires:       libc6
Requires:       libgcc-s1
Requires:       libkf6coreaddons6
Requires:       libkf6widgetsaddons6
Requires:       libqt6core6
Requires:       libqt6dbus6
Requires:       libqt6gui6
Requires:       libqt6widgets6
Requires:       libstdc++6
Requires:       libkf6configcore6
Requires:       libkf6config-data
Requires:       libkf6configgui6
Requires:       libkf6guiaddons6
Requires:       libkf6guiaddons-data
Requires:       libkf6coreaddons-data
Requires:       libkf6dbusaddons6
Requires:       libkf6dbusaddons-data
Requires:       libqt6test6
Requires:       libkf6widgetsaddons-data
Requires:       libqt6xml6
Requires:       plasma-desktop
%endif
#

# Builds for Debian 13+ - Sid / Next (Unstable)
%if "%{_repository}" == "Debian_debbuild_Debian_Next"
BuildRequires:  g++
BuildRequires:  cmake  cmake-extras  extra-cmake-modules
BuildRequires:  libkf6config-dev
BuildRequires:  libkf6coreaddons-dev
BuildRequires:  libkf6dbusaddons-dev
BuildRequires:  libkf6widgetsaddons-dev
BuildRequires:  qt6-base-dev

Requires:       libc6
Requires:       libgcc-s1
Requires:       libkf6coreaddons6
Requires:       libkf6widgetsaddons6
Requires:       libqt6core6
Requires:       libqt6dbus6
Requires:       libqt6gui6
Requires:       libqt6widgets6
Requires:       libstdc++6
Requires:       libkf6configcore6
Requires:       libkf6config-data
Requires:       libkf6configgui6
Requires:       libkf6guiaddons6
Requires:       libkf6guiaddons-data
Requires:       libkf6coreaddons-data
Requires:       libkf6dbusaddons6
Requires:       libkf6dbusaddons-data
Requires:       libqt6test6
Requires:       libkf6widgetsaddons-data
Requires:       libqt6xml6
Requires:       plasma-desktop
%endif
#

# Builds for Ubuntu 24.04 - Noble Numbat (LTS)
%if "%{_repository}" == "Ubuntu_debbuild_Ubuntu_24.04"
Patch0:         QT-5_Build.patch

BuildRequires:  g++
BuildRequires:  cmake  cmake-extras  extra-cmake-modules
BuildRequires:  libkf5config-dev
BuildRequires:  libkf5coreaddons-dev
BuildRequires:  libkf5dbusaddons-dev
BuildRequires:  libkf5widgetsaddons-dev
BuildRequires:  qtbase5-dev

Requires:       libc6
Requires:       libgcc-s1
Requires:       libkf5coreaddons5
Requires:       libkf5widgetsaddons5
Requires:       libqt5core5
Requires:       libqt5dbus5
Requires:       libqt5gui5
Requires:       libqt5widgets5
Requires:       libstdc++6
Requires:       libkf5configcore5
Requires:       libkf5config-data
Requires:       libkf5configgui5
Requires:       libkf5guiaddons5
Requires:       libkf5guiaddons-data
Requires:       libkf5coreaddons-data
Requires:       libkf5dbusaddons5
Requires:       libkf5dbusaddons-data
Requires:       libqt5test5
Requires:       libkf5widgetsaddons-data
Requires:       libqt5xml5
Requires:       libqt5xmlpatterns5
Requires:       plasma-desktop
%endif
#

# Builds for Ubuntu 24.10 - Oracular Oriole
%if "%{_repository}" == "Ubuntu_debbuild_Ubuntu_24.10"
BuildRequires:  g++
BuildRequires:  cmake  cmake-extras  extra-cmake-modules
BuildRequires:  libkf6config-dev
BuildRequires:  libkf6coreaddons-dev
BuildRequires:  libkf6dbusaddons-dev
BuildRequires:  libkf6widgetsaddons-dev
BuildRequires:  qt6-base-dev

Requires:       libc6
Requires:       libgcc-s1
Requires:       libkf6coreaddons6
Requires:       libkf6widgetsaddons6
Requires:       libqt6core6
Requires:       libqt6dbus6
Requires:       libqt6gui6
Requires:       libqt6widgets6
Requires:       libstdc++6
Requires:       libkf6configcore6
Requires:       libkf6config-data
Requires:       libkf6configgui6
Requires:       libkf6guiaddons6
Requires:       libkf6guiaddons-data
Requires:       libkf6coreaddons-data
Requires:       libkf6dbusaddons6
Requires:       libkf6dbusaddons-data
Requires:       libqt6test6
Requires:       libkf6widgetsaddons-data
Requires:       libqt6xml6
Requires:       plasma-desktop
%endif
#

# Builds for Ubuntu 25.04 - Plucky Puffin
%if "%{_repository}" == "Ubuntu_debbuild_Ubuntu_25.04"
BuildRequires:  g++
BuildRequires:  cmake  cmake-extras  extra-cmake-modules
BuildRequires:  libkf6config-dev
BuildRequires:  libkf6coreaddons-dev
BuildRequires:  libkf6dbusaddons-dev
BuildRequires:  libkf6widgetsaddons-dev
BuildRequires:  qt6-base-dev

Requires:       libc6
Requires:       libgcc-s1
Requires:       libkf6coreaddons6
Requires:       libkf6widgetsaddons6
Requires:       libqt6core6
Requires:       libqt6dbus6
Requires:       libqt6gui6
Requires:       libqt6widgets6
Requires:       libstdc++6
Requires:       libkf6configcore6
Requires:       libkf6config-data
Requires:       libkf6configgui6
Requires:       libkf6guiaddons6
Requires:       libkf6guiaddons-data
Requires:       libkf6coreaddons-data
Requires:       libkf6dbusaddons6
Requires:       libkf6dbusaddons-data
Requires:       libqt6test6
Requires:       libkf6widgetsaddons-data
Requires:       libqt6xml6
Requires:       plasma-desktop
%endif
#

# Builds for Ubuntu 25.10+ - Questing Quokka / Next
%if "%{_repository}" == "Ubuntu_debbuild_Ubuntu_Next"
BuildRequires:  g++
BuildRequires:  cmake  cmake-extras  extra-cmake-modules
BuildRequires:  libkf6config-dev
BuildRequires:  libkf6coreaddons-dev
BuildRequires:  libkf6dbusaddons-dev
BuildRequires:  libkf6widgetsaddons-dev
BuildRequires:  qt6-base-dev

Requires:       libc6
Requires:       libgcc-s1
Requires:       libkf6coreaddons6
Requires:       libkf6widgetsaddons6
Requires:       libqt6core6
Requires:       libqt6dbus6
Requires:       libqt6gui6
Requires:       libqt6widgets6
Requires:       libstdc++6
Requires:       libkf6configcore6
Requires:       libkf6config-data
Requires:       libkf6configgui6
Requires:       libkf6guiaddons6
Requires:       libkf6guiaddons-data
Requires:       libkf6coreaddons-data
Requires:       libkf6dbusaddons6
Requires:       libkf6dbusaddons-data
Requires:       libqt6test6
Requires:       libkf6widgetsaddons-data
Requires:       libqt6xml6
Requires:       plasma-desktop
%endif
#

%endif
#

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes


%description
Koi is a program designed to provide the KDE Plasma Desktop functionality
to automatically switch between light and dark themes.
Koi allows users to automate and manage their desktop themes,
providing a convenient way to schedule theme changes on the KDE Plasma Desktop,
enhancing the user experience with timely and automated visual adjustments.
It supports full DBus service integration & running custom Bash scripts.

%prep
%autosetup -p1 -n %{original_name}-%{version}

%build
# CMake for RPM-Based Linux Distributions
%if 0%{?suse_version} && 0%{?is_opensuse} || 0%{?sle_version} && 0%{?is_opensuse} || 0%{?fedora} || 0%{?mageia}
%cmake

%cmake_build
#

# CMake for DEB-Based Linux Distributions
%else
cmake -S "." -B "./build/" %{?_cmake_flags}

cmake --build   "./build/" --parallel

%endif
#

%install
# CMake INSTALL for RPM-Based Linux Distributions
%if 0%{?suse_version} && 0%{?is_opensuse} || 0%{?sle_version} && 0%{?is_opensuse} || 0%{?fedora} || 0%{?mageia}
%cmake_install
#

# CMake INSTALL for DEB-Based Linux Distributions
%else
cmake --install "./build/"

%endif
#

%check
# Check the Packaged & Renamed Application .DESKTOP File; Fails on Debian 12 Due to Obsolete `desktop-file-utils`
%if 0%{?suse_version} > 1600 || 0%{?suse_version} == 1600 && 0%{?is_opensuse} || 0%{?fedora} || 0%{?mageia}
desktop-file-validate "%{buildroot}/%{_datadir}/applications/local.%{original_name}DbusInterface.desktop"
#
# Check for Duplicated Files at RPM-Based Linux Distributions
%fdupes                %{buildroot}/
#
# Check for Duplicated Files at DEB-Based Linux Distributions
%else
fdupes -s              %{buildroot}/

%endif
#

%files
%license LICENSE
%doc    "README.md"

     "%{_bindir}/%{name}"

     "%{_datadir}/applications/local.%{original_name}DbusInterface.desktop"
     "%{_datadir}/dbus-1/interfaces/dev.baduhai.%{original_name}.xml"
     "%{_datadir}/dbus-1/services/dev.baduhai.%{original_name}.service"
%if 0%{?sle_version} <= 150600 && 0%{?is_opensuse}
%dir "%{_datadir}/icons/hicolor/"
%dir "%{_datadir}/icons/hicolor/scalable/"
%dir "%{_datadir}/icons/hicolor/scalable/apps/"
%endif
      %{_datadir}/icons/hicolor/scalable/apps/{%{name}.svg,%{name}_tray.svg}

%changelog
