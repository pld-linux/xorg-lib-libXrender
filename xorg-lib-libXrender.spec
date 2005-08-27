Summary:	X Render extension library
Summary(pl):	Biblioteka rozszerzenia X Render
Name:		xorg-lib-libXrender
Version:	0.9.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXrender-%{version}.tar.bz2
# Source0-md5:	0064c7d11a9c6e7cb901f840bb6ba877
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	XFree86-render
Obsoletes:	libXrender
Obsoletes:	xrender
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Render extension library.

%description -l pl
Biblioteka rozszerzenia X Render.

%package devel
Summary:	Header files libXrender development
Summary(pl):	Pliki nagłówkowe do biblioteki libXrender
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-proto-renderproto-devel
Obsoletes:	XFree86-render-devel
Obsoletes:	libXrender-devel
Obsoletes:	xrender-devel

%description devel
X Render extension library.

This package contains the header files needed to develop programs that
use these libXrender.

%description devel -l pl
Biblioteka rozszerzenia X Render.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXrender.

%package static
Summary:	Static libXrender library
Summary(pl):	Biblioteka statyczna libXrender
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	XFree86-render-static
Obsoletes:	libXrender-static
Obsoletes:	xrender-static

%description static
X Render extension library.

This package contains the static libXrender library.

%description static -l pl
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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libXrender.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXrender.so
%{_libdir}/libXrender.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xrender.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXrender.a
