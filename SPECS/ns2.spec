Name:           ns2
Version:        2.35
Release:        1%{?dist}
Summary:        Discrete event simulator targeted at networking research

License:        GPLv3+
URL:            https://sourceforge.net/projects/nsnam/
Source0:        https://sourceforge.net/projects/nsnam/files/ns-2/%{version}/ns-src-%{version}.tar.gz
Patch0:		ns-2.35-linkstate-erase.fix
Patch1:		ns-2.35-tcl86.patch
Patch2:		ns-2.35-getopts.patch
Patch3:		ns-2.35-gcc-compile-errors.patch

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
BuildRequires:	tclcl

%description 
OTcl, short for MIT Object Tcl, is an extension to Tcl/Tk for object-oriented programming. It shouldn't be confused with the IXI Object Tcl extension by Dean Sheenan. (Sorry, but we both like the name and have been using it for a while.)

%prep
%setup -n ns-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
./configure --prefix=/usr --enable-static
%make_build

%install
install -Dm755 ns %{buildroot}/%{_bindir}/ns
install -Dm644 ns.1 %{buildroot}/%{_mandir}/man1/ns.1.gz

%files
%{_bindir}/ns
%{_mandir}/man1/ns.1.gz

%changelog
* Wed May 03 2017 - 1.14-1
- Initial version of the package
