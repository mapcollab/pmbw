Summary: Parallel Memory Bandwidth Benchmark
Name: pmbw
Version: 0.6.2
Release: 1
Group: System Environment/Libraries
URL: http://www.thalesgroup.com/
Vendor: Thales Avionics, Inc.
License: GPLv3
Packager: Builder <builder@thales-ktw.site>
Source: %{name}-%{version}.tar.gz


%description
Parallel Memory Bandwidth Benchmark


%prep
%setup -q -n %{name}-%{version}


%build
%configure
make


%install
mkdir -p %{buildroot}/%{_bindir}/
install -m755 pmbw %{buildroot}/%{_bindir}/
install -m755 stats2gnuplot %{buildroot}/%{_bindir}/


%files
%attr(0755,root,root) %{_bindir}/*


%changelog
