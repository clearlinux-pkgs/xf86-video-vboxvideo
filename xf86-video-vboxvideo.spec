#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v18
# autospec commit: 356da62
#
# Source0 file verified with key 0xCFDF148828C642A7 (alan.coopersmith@oracle.com)
#
Name     : xf86-video-vboxvideo
Version  : 1.0.1
Release  : 993
URL      : https://www.x.org/releases/individual/driver/xf86-video-vboxvideo-1.0.1.tar.gz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-vboxvideo-1.0.1.tar.gz
Source1  : https://www.x.org/releases/individual/driver/xf86-video-vboxvideo-1.0.1.tar.gz.sig
Source2  : CFDF148828C642A7.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-vboxvideo-lib = %{version}-%{release}
Requires: xf86-video-vboxvideo-license = %{version}-%{release}
Requires: xf86-video-vboxvideo-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : gnupg
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
xf86-video-vboxvideo - VirtualBox video driver for the Xorg X server
--------------------------------------------------------------------

%package lib
Summary: lib components for the xf86-video-vboxvideo package.
Group: Libraries
Requires: xf86-video-vboxvideo-license = %{version}-%{release}

%description lib
lib components for the xf86-video-vboxvideo package.


%package license
Summary: license components for the xf86-video-vboxvideo package.
Group: Default

%description license
license components for the xf86-video-vboxvideo package.


%package man
Summary: man components for the xf86-video-vboxvideo package.
Group: Default

%description man
man components for the xf86-video-vboxvideo package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) CFDF148828C642A7' gpg.status
%setup -q -n xf86-video-vboxvideo-1.0.1
cd %{_builddir}/xf86-video-vboxvideo-1.0.1
pushd ..
cp -a xf86-video-vboxvideo-1.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1722449441
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O3 -g -fopt-info-vec "
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
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O3 -g -fopt-info-vec "
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
export SOURCE_DATE_EPOCH=1722449441
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-vboxvideo
cp %{_builddir}/xf86-video-vboxvideo-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xf86-video-vboxvideo/664d822c161b3cb3b4b663436ed13892c7a87c8f || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/xorg/modules/drivers/vboxvideo_drv.so
/usr/lib64/xorg/modules/drivers/vboxvideo_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-vboxvideo/664d822c161b3cb3b4b663436ed13892c7a87c8f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/vboxvideo.4
