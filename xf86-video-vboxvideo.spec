#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAA9B2D1A308B5859 (michael.thayer@oracle.com)
#
Name     : xf86-video-vboxvideo
Version  : 1.0.0
Release  : 735
URL      : https://www.x.org/releases/individual/driver/xf86-video-vboxvideo-1.0.0.tar.gz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-vboxvideo-1.0.0.tar.gz
Source1  : https://www.x.org/releases/individual/driver/xf86-video-vboxvideo-1.0.0.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : X11
Requires: xf86-video-vboxvideo-lib = %{version}-%{release}
Requires: xf86-video-vboxvideo-license = %{version}-%{release}
Requires: xf86-video-vboxvideo-man = %{version}-%{release}
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)

%description
xf86-video-vboxvideo - VirtualBox video driver for the Xorg X server
Please submit bugs & patches to the Xorg bugzilla:

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
%setup -q -n xf86-video-vboxvideo-1.0.0
cd %{_builddir}/xf86-video-vboxvideo-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614228702
export GCC_IGNORE_WERROR=1
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1614228702
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-vboxvideo
cp %{_builddir}/xf86-video-vboxvideo-1.0.0/COPYING %{buildroot}/usr/share/package-licenses/xf86-video-vboxvideo/3308f3b8353e24059b26fee1519f6dd67d89cf54
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/vboxvideo_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-vboxvideo/3308f3b8353e24059b26fee1519f6dd67d89cf54

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/vboxvideo.4
