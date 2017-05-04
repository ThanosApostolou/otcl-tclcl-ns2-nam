Name:           nam
Version:        1.15
Release:        1%{?dist}
Summary:        Nam is a Tcl/TK based animation tool for viewing network simulation traces and real world packet traces

License:        GPLv3+
URL:            https://sourceforge.net/projects/nsnam/
Source0:        https://sourceforge.net/projects/nsnam/files/nam-1/%{version}/%{name}-src-%{version}.tar.gz
Patch0:		nam-1.15-gcc61.patch
Patch1:		nam-1.15-tcl86.patch

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
Nam is a Tcl/TK based animation tool for viewing network simulation traces and real world packet traces. It supports topology layout, packet level animation, and various data inspection tools. Nam began at LBL. It has evolved substantially over the past few years. The nam development effort was an ongoing collaboration with the VINT project. Currently, it is being developed as an open source project hosted at Sourceforge. 

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
./configure --prefix=/usr
%make_build

%install
install -d %{buildroot}/usr/bin
%make_install

%files
%{_bindir}/nam

%changelog
* Thu May 04 2017 - 1.14-1
- Initial version of the package
