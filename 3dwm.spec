Summary:	3D user environment
Summary(pl.UTF-8):   Trójwymiarowe środowisko użytkownika
Name:		3dwm
Version:	0.3.2
Release:	1
License:	LGPL
Group:		X11/Window Managers
Source0:	http://www.3dwm.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	61510b9e9769a36e5790c9d606bfbfbb
Source1:	%{name}-tdwmrc
Patch0:		%{name}-autocrap.patch
Patch1:		%{name}-gcc32.patch
Patch2:		%{name}-SDL-in-usr-X11R6.patch
Patch3:		%{name}-omniORB4.patch
Patch4:		%{name}-gcc33.patch
Patch5:		%{name}-opt.patch
URL:		http://www.3dwm.org/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	meshio-devel
BuildRequires:	omniORB-devel >= 4.0.2
# omniidl is here
BuildRequires:	omniORB
Requires:	%{name}-libs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3Dwm is a three-dimensional user environment that can run on immersive
Virtual Reality hardware (such as CAVEs and HMDs) as well as on
desktop computers. It is a platform for the research and development
of three-dimensional user interfaces, providing a means of exploring
possible future user interfaces. 3Dwm is fully distributed using
CORBA. Other planned and implemented features include OpenGL
rendering, X11 (and other windowing system) bindings, CAVELib support,
3D TrueType fonts, general streaming movie support, a 3DUI widget kit,
etc.

%description -l pl.UTF-8
3Dwm jest trójwymiarowym środowiskiem użytkownika, które można
uruchomić na sprzęcie do Rzeczywistości Wirtualnej (jak CAVE lub HMD)
oraz na komputerach biurkowych. Jest to platforma dla badań i rozwoju
trójwymiarowych interfejsów użytkownika, dostarczająca środków
odkrywania możliwej przyszłości interfejsów użytkownika. 3Dwm jest w
pełni rozproszony z użyciem technologii CORBA. Inne planowane i
zaimplementowane cechy to rendering z użyciem OpenGL, wiązania dla X11
(oraz innych systemów okienkowych), wsparcie dla CAVELib, czcionek
True Type 3D, ogólne wsparcie dla strumieni filmowych, zestaw
kontrolek 3DUI etc.

%package libs
Summary:	3D user environment - Libraries
Summary(pl.UTF-8):   Trójwymiarowe środowisko użytkownika - Bilioteki
Group:		X11/Libraries

%description libs
3Dwm is a three-dimensional user environment that can run on immersive
Virtual Reality hardware (such as CAVEs and HMDs) as well as on
desktop computers. It is a platform for the research and development
of three-dimensional user interfaces, providing a means of exploring
possible future user interfaces. 3Dwm is fully distributed using
CORBA. Other planned and implemented features include OpenGL
rendering, X11 (and other windowing system) bindings, CAVELib support,
3D TrueType fonts, general streaming movie support, a 3DUI widget kit,
etc.

%description libs -l pl.UTF-8
3Dwm jest trójwymiarowym środowiskiem użytkownika, które można
uruchomić na sprzęcie do Rzeczywistości Wirtualnej (jak CAVE lub HMD)
oraz na komputerach biurkowych. Jest to platforma dla badań i rozwoju
trójwymiarowych interfejsów użytkownika, dostarczająca środków
odkrywania możliwej przyszłości interfejsów użytkownika. 3Dwm jest w
pełni rozproszony z użyciem technologii CORBA. Inne planowane i
zaimplementowane cechy to rendering z użyciem OpenGL, wiązania dla X11
(oraz innych systemów okienkowych), wsparcie dla CAVELib, czcionek
True Type 3D, ogólne wsparcie dla strumieni filmowych, zestaw
kontrolek 3DUI etc.

%package devel
Summary:	3D user environment - development files
Summary(pl.UTF-8):   Trójwymiarowe środowisko użytkownika - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
3Dwm is a three-dimensional user environment that can run on immersive
Virtual Reality hardware (such as CAVEs and HMDs) as well as on
desktop computers. It is a platform for the research and development
of three-dimensional user interfaces, providing a means of exploring
possible future user interfaces. 3Dwm is fully distributed using
CORBA. Other planned and implemented features include OpenGL
rendering, X11 (and other windowing system) bindings, CAVELib support,
3D TrueType fonts, general streaming movie support, a 3DUI widget kit,
etc.

%description devel -l pl.UTF-8
3Dwm jest trójwymiarowym środowiskiem użytkownika, które można
uruchomić na sprzęcie do Rzeczywistości Wirtualnej (jak CAVE lub HMD)
oraz na komputerach biurkowych. Jest to platforma dla badań i rozwoju
trójwymiarowych interfejsów użytkownika, dostarczająca środków
odkrywania możliwej przyszłości interfejsów użytkownika. 3Dwm jest w
pełni rozproszony z użyciem technologii CORBA. Inne planowane i
zaimplementowane cechy to rendering z użyciem OpenGL, wiązania dla X11
(oraz innych systemów okienkowych), wsparcie dla CAVELib, czcionek
True Type 3D, ogólne wsparcie dla strumieni filmowych, zestaw
kontrolek 3DUI etc.

%package static
Summary:	3D user environment - static files
Summary(pl.UTF-8):   Trójwymiarowe środowisko użytkownika - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
3Dwm is a three-dimensional user environment that can run on immersive
Virtual Reality hardware (such as CAVEs and HMDs) as well as on
desktop computers. It is a platform for the research and development
of three-dimensional user interfaces, providing a means of exploring
possible future user interfaces. 3Dwm is fully distributed using
CORBA. Other planned and implemented features include OpenGL
rendering, X11 (and other windowing system) bindings, CAVELib support,
3D TrueType fonts, general streaming movie support, a 3DUI widget kit,
etc.

%description static -l pl.UTF-8
3Dwm jest trójwymiarowym środowiskiem użytkownika, które można
uruchomić na sprzęcie do Rzeczywistości Wirtualnej (jak CAVE lub HMD)
oraz na komputerach biurkowych. Jest to platforma dla badań i rozwoju
trójwymiarowych interfejsów użytkownika, dostarczająca środków
odkrywania możliwej przyszłości interfejsów użytkownika. 3Dwm jest w
pełni rozproszony z użyciem technologii CORBA. Inne planowane i
zaimplementowane cechy to rendering z użyciem OpenGL, wiązania dla X11
(oraz innych systemów okienkowych), wsparcie dla CAVELib, czcionek
True Type 3D, ogólne wsparcie dla strumieni filmowych, zestaw
kontrolek 3DUI etc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -f config/missing config/macros/ac_help_string.m4
mv -f INSTALL INSTALL.tmp
%{__libtoolize}
%{__aclocal} -I config/macros
%{__autoheader}
%{__autoconf}
%{__automake}
mv -f INSTALL.tmp INSTALL
%configure \
	--enable-optimize \
	--disable-rpath
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/3Dwm/tdwmrc
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/3Dwm/tdwrc

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/3Dwm

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/Nobel*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
