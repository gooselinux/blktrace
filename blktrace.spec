Summary: Utilities for performing block layer IO tracing in the linux kernel
Name: blktrace
Version: 1.0.1
Release: 3.1%{?dist}
License: GPLv2+
Group: Development/System
Source:  http://brick.kernel.dk/snaps/blktrace-%{version}.tar.bz2
Url: http://brick.kernel.dk/snaps

Requires: python
BuildRequires: libaio-devel python texlive-latex dvipdfm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations to user space.  This package
includes both blktrace, a utility which gathers event traces from the kernel;
and blkparse, a utility which formats trace data collected by blktrace.

You should install the blktrace package if you need to gather detailed
information about IO patterns.

%prep
%setup -q

%build
make CFLAGS="%{optflags}" all
make CFLAGS="%{optflags}" docs

%install
rm -rf %{buildroot}
make dest=%{buildroot} prefix=%{buildroot}/%{_prefix} mandir=%{buildroot}/usr/share/man install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%doc btt/doc/btt.pdf btreplay/doc/btreplay.pdf doc/blktrace.pdf
%{_bindir}/*
%attr(0644,root,root) /usr/share/man/man1/*
%attr(0644,root,root) /usr/share/man/man8/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.1-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.1-2
- Upstream respun the release tarball to re-include top-level dir
- drop exclude of bno_plot.py[co], not getting built now?

* Mon May 11 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.1-1
- New upstream version

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.0-2
- Build PDF documentation after all

* Sun Nov 02 2008 Eric Sandeen <sandeen@redhat.com> - 1.0.0-1
- New upstream version (now with actual versioning!)

* Fri Feb 08 2008 Eric Sandeen <sandeen@redhat.com> - 0.0-0.9.20080103162505git
- gcc-4.3 rebuild

* Sat Jan 26 2008 Eric Sandeen <sandeen@redhat.com> - 0.0-0.8.20080103162505git
- New upstream version

* Wed Oct 24 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.6.20071010202719git
- Add libaio-devel to BuildRequires

* Wed Oct 24 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.5.20071010202719git
- New upstream version

* Wed Aug 15 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.4.20070730162628git
- Fix up btt/Makefile to accept rpm's CFLAGS

* Tue Aug 14 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.3.20070730162628git
- Just drop the pdf build, bloats the buildroot for such a simple tool

* Wed Aug 01 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.2.20070730162628git
- Add ghostscript to BuildRequires, use attr macro for man pages

* Wed Aug 01 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.1.20070730162628git
- New package, initial build.
