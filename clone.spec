%define name clone
%define version 0.1
%define release %mkrel 2
%define tftpboot /var/lib/tftpboot

Summary: HOWTO duplicate an node with ka, dolly, and dollyC
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Cluster
Url: http://www.mandriva.com
requires: ka-deploy-source-node
Buildrequires: libxslt-proc
Buildarch: noarch

%description
all scripts, configuration files needed to create and
setup a golden node to duplicate computer.

%prep
%setup -q -n %name-%version

%build

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall PREFIX=%{buildroot}/%{_prefix} \
    TFTPBOOT=%{buildroot}%{tftpboot} \
	SYSCONFDIR=%{buildroot}%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc clone.spec html/ *.xml *.xsl Makefile *.dsssl *.css
%attr(644,root,root) %config(noreplace) %{tftpboot}/X86PC/linux/pxelinux.cfg/default.pxe.clone
%attr(755,root,root) %{_bindir}/ka-d-session.sh
%attr(755,root,root) %{_bindir}/clone_script
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/dhcpd.conf.clone
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/xinetd.d/tftp.clone
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/pxe.conf.clone
