Name:              pixman
Version:           0.42.2
Release:           2
Summary:           Pixman is a pixel manipulation library for X and Cairo
License:           MIT
URL:               https://gitlab.freedesktop.org/pixman/pixman
Source0:           https://gitlab.freedesktop.org/pixman/pixman/-/archive/pixman-%{version}/pixman-pixman-%{version}.tar.bz2
#%if "toolchain"=="clang"
%ifarch aarch64
Patch0:            fix-arm.patch
%endif
%ifarch riscv64
Patch1:            fix-timeout.patch
%endif
#%endif
BuildRequires:     gcc meson

%description
Pixman is a low-level software library for pixel manipulation, providing features such\
\as image compositing and trapezoid rasterization.\

%package           devel
Summary:           Provide library and header files for pixman
Requires:          %{name} = %{version}-%{release}
Requires:          pkgconfig

%description       devel
Provide library and header files for pixman

%prep
%autosetup -n pixman-%{name}-%{version} -p1
sed -i 's/120/600/' test/meson.build

%build
%meson --auto-features=auto \
%ifarch %{arm}
  -Diwmmxt=disabled -Diwmmxt2=false \
%endif
  %nil

%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libpixman-1*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/pixman-1/pixman*.h
%{_libdir}/libpixman-1*.so
%{_libdir}/pkgconfig/*

%changelog
* Mon Jun 12 2023 zhangxiang <zhangxiang@iscas.ac.cn> - 0.42.2-2
- Fix clang build error

* Fri Feb 03 2023 zhangpan <zhangpan@h-partners.com> - 0.42.2-1
- update to 0.42.2

* Tue Nov 08 2022 wangkerong <wangkerong@h-partners.com> - 0.40.0-3
- fix CVE-2022-44638

* Wed Oct 26 2022 zhouwenpei <zhouwenpei1@h-partners.com> - 0.40.0-2
- Rebuild for next release

* Mon Apr 20 2020 openEuler Buildteam <buildteam@openeuler.org> - 0.40.0-1
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:update to 0.40.0

* Mon Sep 9 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.38.0-1
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:Modify the spec according to the new rules

* Thu Aug 22 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.34.0-11 
- Package init
