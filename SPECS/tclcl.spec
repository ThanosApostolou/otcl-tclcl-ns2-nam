Name:           tclcl
Version:        1.20
Release:        1%{?dist}
Summary:        clCL is a Tcl/C++ interface used by Mash, vic, vat, rtp_play, ns, and nam

License:        GPLv3+
URL:            https://sourceforge.net/projects/otcl-tclcl/
Source0:        https://sourceforge.net/projects/otcl-tclcl/files/TclCL/%{version}/%{name}-src-%{version}.tar.gz
Patch0:		tclcl-1.20-tcl86-compat.patch

Requires:	libX11
Requires:	libXt
Requires:	tcl
Requires:	tk
Requires:	otcl
BuildRequires:	libX11-devel
BuildRequires:	libXt-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	otcl
BuildRequires:	libstdc++-static
BuildRequires:	glibc-static

%description 
TclCL (Tcl with classes) is a Tcl/C++ interface used by Mash, vic, vat, rtp_play, ns, and nam. It provides a layer of C++ glue over OTcl

%prep
%setup
%patch0 -p1

%build
./configure --prefix=/usr/ --enable-static
%make_build -j1

%install
install -Dm755 tcl2c++ %{buildroot}/%{_bindir}/tcl2c++
install -Dm644 config.h %{buildroot}/%{_includedir}/config.h
install -Dm644 idlecallback.h %{buildroot}/%{_includedir}/idlecallback.h
install -Dm644 iohandler.h %{buildroot}/%{_includedir}/iohandler.h
install -Dm644 rate-variable.h %{buildroot}/%{_includedir}/rate-variable.h
install -Dm644 tclcl-config.h %{buildroot}/%{_includedir}/tclcl-config.h
install -Dm644 tclcl-internal.h %{buildroot}/%{_includedir}/tclcl-internal.h
install -Dm644 tclcl-mappings.h %{buildroot}/%{_includedir}/tclcl-mappings.h
install -Dm644 tclcl.h %{buildroot}/%{_includedir}/tclcl.h
install -Dm644 timer.h %{buildroot}/%{_includedir}/timer.h
install -Dm644 tracedvar.h %{buildroot}/%{_includedir}/tracedvar.h
install -Dm644 libtclcl.a %{buildroot}/%{_libdir}/libtclcl.a

%files
%{_bindir}/tcl2c++
%{_includedir}/config.h
%{_includedir}/idlecallback.h
%{_includedir}/iohandler.h
%{_includedir}/rate-variable.h
%{_includedir}/tclcl-config.h
%{_includedir}/tclcl-internal.h
%{_includedir}/tclcl-mappings.h
%{_includedir}/tclcl.h
%{_includedir}/timer.h
%{_includedir}/tracedvar.h
%{_libdir}/libtclcl.a

%changelog
* Thu May 04 2017 - 1.14-1
- Initial version of the package
