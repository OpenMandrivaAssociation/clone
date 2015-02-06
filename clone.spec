%define name clone
%define version 0.1
%define release 7
%define tftpboot /var/lib/tftpboot

Summary: HOWTO duplicate an node with ka, dolly, and dollyC
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Cluster
Url: http://www.mandriva.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-6mdv2011.0
+ Revision: 617043
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.1-5mdv2010.0
+ Revision: 424880
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2009.0
+ Revision: 243530
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.1-2mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 13 2007 Nicolas Vigier <nvigier@mandriva.com> 0.1-2mdv2008.0
+ Revision: 62471
- Import clone



* Tue Mar  6 2007 Antoine Ginies <aginies@mandriva.com> 0.1-2mdviggi
- remove fdisk_to_desc

* Fri Sep  1 2006  <guibo@guibpiv.guibland.com> 0.1-0.1.20060mlcs4
- first release
