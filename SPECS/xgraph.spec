Name:           xgraph
Version:        4.30
Release:        1%{?dist}
Summary:        XGRAPH is a general purpose x-y data plotter

License:        custom
URL:            http://www.xgraph.org/
Source0:        http://www.xgraph.org/linux/%{name}_%{version}_linux64.tar.gz
Source1:        http://www.xgraph.org/linux/%{name}_%{version}_linux32.tar.gz
Requires:	libX11

%description 
XGRAPH is a general purpose x-y data plotter with interactive buttons for panning, zooming, printing, and selecting display options. It will plot data from any number of files on the same graph and can handle unlimited data-set sizes and any number of data files. 

%prep
%setup -c %{name}-%{version} -b1

%install
if test "%{_arch}" == x86_64; then
	cd %{_builddir}/%{name}-%{version}/XGraph%{version}_linux64
elif test "%{_arch}" == i386; then
	cd %{_builddir}/%{name}-%{version}/XGraph%{version}_linux32
fi
install -Dm755 ./bin/xgraph %{buildroot}/%{_bindir}/xgraph
install -Dm644 Readme.txt %{buildroot}/%{_datadir}/xgraph/Readme.txt
install -Dm644 testxy.dat %{buildroot}/%{_datadir}/xgraph/testxy.dat
install -Dm644 ./data/oofficedata.scz %{buildroot}/%{_datadir}/xgraph/data/oofficedata.scz
install -Dm644 ./data/pptxdata.scz %{buildroot}/%{_datadir}/xgraph/data/pptxdata.scz
install -Dm644 ./data/sxidata.scz %{buildroot}/%{_datadir}/xgraph/data/sxidata.scz
install -Dm644 ./data/pptx/thumbnail.jpeg %{buildroot}/%{_datadir}/xgraph/data/pptx/thumbnail.jpeg

%files
%{_bindir}/xgraph
%{_datadir}/xgraph/Readme.txt
%{_datadir}/xgraph/testxy.dat
%{_datadir}/xgraph/data/oofficedata.scz
%{_datadir}/xgraph/data/pptxdata.scz
%{_datadir}/xgraph/data/sxidata.scz
%{_datadir}/xgraph/data/pptx/thumbnail.jpeg

%changelog
* Thu May 04 2017 - 1.14-1
- Initial version of the package
