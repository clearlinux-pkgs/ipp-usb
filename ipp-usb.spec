#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : ipp-usb
Version  : 0.9.30
Release  : 5
URL      : https://github.com/OpenPrinting/ipp-usb/archive/0.9.30/ipp-usb-0.9.30.tar.gz
Source0  : https://github.com/OpenPrinting/ipp-usb/archive/0.9.30/ipp-usb-0.9.30.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: ipp-usb-bin = %{version}-%{release}
Requires: ipp-usb-config = %{version}-%{release}
Requires: ipp-usb-data = %{version}-%{release}
Requires: ipp-usb-license = %{version}-%{release}
Requires: ipp-usb-man = %{version}-%{release}
Requires: ipp-usb-services = %{version}-%{release}
BuildRequires : go
BuildRequires : pkgconfig(avahi-client)
BuildRequires : pkgconfig(libusb-1.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Don-t-call-gotags.patch

%description
This directory contains a collection of quirks files for various
devices.
See `man ipp-usb` for details

%package bin
Summary: bin components for the ipp-usb package.
Group: Binaries
Requires: ipp-usb-data = %{version}-%{release}
Requires: ipp-usb-config = %{version}-%{release}
Requires: ipp-usb-license = %{version}-%{release}
Requires: ipp-usb-services = %{version}-%{release}

%description bin
bin components for the ipp-usb package.


%package config
Summary: config components for the ipp-usb package.
Group: Default

%description config
config components for the ipp-usb package.


%package data
Summary: data components for the ipp-usb package.
Group: Data

%description data
data components for the ipp-usb package.


%package license
Summary: license components for the ipp-usb package.
Group: Default

%description license
license components for the ipp-usb package.


%package man
Summary: man components for the ipp-usb package.
Group: Default

%description man
man components for the ipp-usb package.


%package services
Summary: services components for the ipp-usb package.
Group: Systemd services
Requires: systemd

%description services
services components for the ipp-usb package.


%prep
%setup -q -n ipp-usb-0.9.30
cd %{_builddir}/ipp-usb-0.9.30
%patch -P 1 -p1

%build
## build_prepend content
export GOFLAGS='-buildmode=pie' GO111MODULE="auto"
unset CLEAR_DEBUG_TERSE
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742418227
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742418227
rm -rf %{buildroot}
## install_prepend content
export GOFLAGS='-buildmode=pie' GO111MODULE="auto"
unset CLEAR_DEBUG_TERSE
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/ipp-usb
cp %{_builddir}/ipp-usb-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/ipp-usb/39b4e8671fbf28a1df2ade414c3c642d6cc7130f || :
cp %{_builddir}/ipp-usb-%{version}/vendor/github.com/OpenPrinting/goipp/LICENSE %{buildroot}/usr/share/package-licenses/ipp-usb/39b4e8671fbf28a1df2ade414c3c642d6cc7130f || :
export GOAMD64=v2
GOAMD64=v2
%make_install
## install_append content
# Use /usr/lib, not /lib
mv %{buildroot}/lib %{buildroot}/usr/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipp-usb

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/71-ipp-usb.rules

%files data
%defattr(-,root,root,-)
/usr/share/ipp-usb/quirks/Brother.conf
/usr/share/ipp-usb/quirks/Canon.conf
/usr/share/ipp-usb/quirks/HP.conf
/usr/share/ipp-usb/quirks/Pantum.conf
/usr/share/ipp-usb/quirks/README
/usr/share/ipp-usb/quirks/blacklist.conf
/usr/share/ipp-usb/quirks/default.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipp-usb/39b4e8671fbf28a1df2ade414c3c642d6cc7130f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/ipp-usb.8.gz

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ipp-usb.service
