Name:           otcl
Version:        1.14
Release:        1%{?dist}
Summary:        OTcl, short for MIT Object Tcl, is an extension to Tcl/Tk for object-oriented programming

License:        GPLv3+
URL:            https://sourceforge.net/projects/otcl-tclcl/
Source0:        https://sourceforge.net/projects/otcl-tclcl/files/OTcl/%{version}/%{name}-src-%{version}.tar.gz
Patch0:		otcl-1.14-tcl86-compat.patch

Requires:	libX11
Requires:	libXt
Requires:	tcl
Requires:	tk
BuildRequires:	libX11-devel
BuildRequires:	libXt-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel

%description 
OTcl, short for MIT Object Tcl, is an extension to Tcl/Tk for object-oriented programming. It shouldn't be confused with the IXI Object Tcl extension by Dean Sheenan. (Sorry, but we both like the name and have been using it for a while.)

%prep
%setup
%patch0 -p1

%build
./configure --prefix=/usr --enable-static
%make_build -j1

%install
install -Dm755 otclsh %{buildroot}/%{_bindir}/otclsh
install -Dm755 owish %{buildroot}/%{_bindir}/owish
install -Dm644 otcl.h %{buildroot}/%{_includedir}/otcl.h
install -Dm644 libotcl.a %{buildroot}/%{_libdir}/libotcl.a

%files
%{_bindir}/otclsh
%{_bindir}/owish
%{_includedir}/otcl.h
%{_libdir}/libotcl.a

%changelog
* Wed May 03 2017 - 1.14-1
- Initial version of the package
