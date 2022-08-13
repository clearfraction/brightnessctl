Name     : brightnessctl
Version  : 0.5.1
Release  : 1
URL      : https://github.com/Hummer12007/brightnessctl
Source0  : https://github.com/Hummer12007/brightnessctl/archive/refs/tags/%{version}.tar.gz
Summary  : Control backlight controllers
Group    : Development/Tools
License  : MIT
BuildRequires : make
BuildRequires : gcc
BuildRequires : systemd-dev

%description
Light is a program to control backlight controllers under GNU/Linux

%prep
%setup -q

%build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export FCFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export FFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export CXXFLAGS="$CXXFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export ENABLE_SYSTEMD=1
%make_build

%install
%make_install INSTALL_UDEV_RULES=0 ENABLE_SYSTEMD=1 PREFIX=/usr
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/brightnessctl
