#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86-video-vboxvideo
Version  : 1.0.0
Release  : 19
URL      : https://cgit.freedesktop.org/xorg/driver/xf86-video-vbox/snapshot/xf86-video-vboxvideo-1.0.0.tar.gz
Source0  : https://cgit.freedesktop.org/xorg/driver/xf86-video-vbox/snapshot/xf86-video-vboxvideo-1.0.0.tar.gz
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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557105433
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557105433
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-vboxvideo
cp COPYING %{buildroot}/usr/share/package-licenses/xf86-video-vboxvideo/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/vboxvideo_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-vboxvideo/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/vboxvideo.4
