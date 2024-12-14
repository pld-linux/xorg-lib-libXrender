Summary:	X Render extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X Render
Name:		xorg-lib-libXrender
Version:	0.9.12
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXrender-%{version}.tar.xz
# Source0-md5:	4c54dce455d96e3bdee90823b0869f89
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-proto-renderproto-devel >= 0.9
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libX11 >= 1.6
Obsoletes:	XFree86-render < 4.4
Obsoletes:	libXrender < 0.9
Obsoletes:	xrender < 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Render extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia X Render.

%package devel
Summary:	Header files for libXrender library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXrender
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel >= 1.6
Requires:	xorg-proto-renderproto-devel >= 0.9
Obsoletes:	XFree86-render-devel < 4.4
Obsoletes:	libXrender-devel < 0.9
Obsoletes:	xrender-devel < 0.9

%description devel
X Render extension library.

This package contains the header files needed to develop programs that
use libXrender.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia X Render.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXrender.

%package static
Summary:	Static libXrender library
Summary(pl.UTF-8):	Biblioteka statyczna libXrender
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	XFree86-render-static < 4.4
Obsoletes:	libXrender-static < 0.9
Obsoletes:	xrender-static < 0.9

%description static
X Render extension library.

This package contains the static libXrender library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia X Render.

Pakiet zawiera statyczną bibliotekę libXrender.

%prep
%setup -q -n libXrender-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/libXrender/libXrender.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libXrender.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXrender.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/libXrender.txt
%attr(755,root,root) %{_libdir}/libXrender.so
%{_libdir}/libXrender.la
%{_includedir}/X11/extensions/Xrender.h
%{_pkgconfigdir}/xrender.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXrender.a
