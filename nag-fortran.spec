Name: nag-fortran
Summary: NAG Fortran compiler
Version: 6.1
Release: 2.lanl
License: Commercial
Group: Development/Languages
URL: http://www.nag.co.uk/nagware.html
Packager: Neil Carlson <nnc@lanl.gov>
Source0: npl6a61na_amd64.tgz
Source1: nag.licence
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: /opt/nag/nagfor-%{version}
ExclusiveArch: x86_64
ExclusiveOS: Linux
Provides: libf61rts.so.1 libf61rts.so.1()(64bit)

# don't strip *anything*, fools
%global __strip                 /bin/true
%global __os_install_post       %{nil}

%description
The NAG Fortran compiler.  Running the compiler requires
a license key or access to a NAG license server (kusari).

%prep
%setup -T -b 0 -n NAG_Fortran-amd64

%build

%install

rm -rf %{buildroot}
mkdir -p %{buildroot}/%{prefix}/{bin,doc,html,lib,man/man{1,3}}

### Binaries and libraries ###

install -m 755 bin/nagfmcheck %{buildroot}/%{prefix}/bin/nagfmcheck
install -m 755 bin/nagfor     %{buildroot}/%{prefix}/lib/nagfor
install -m 755 bin/dbx90      %{buildroot}/%{prefix}/lib/dbx90

touch %{buildroot}/%{prefix}/bin/nagfor
touch %{buildroot}/%{prefix}/bin/dbx90

cp -a lib %{buildroot}/%{prefix}

# Remove unneeded executable due to missing library dependency. 
rm %{buildroot}/%{prefix}/lib/kdongle

### Man pages ###

for x in man/*.1; do
  install -m 644 $x %{buildroot}/%{prefix}/man/man1
done

for x in man/*.3; do
  install -m 644 $x %{buildroot}/%{prefix}/man/man3
done

### License file and additional documentation ###

install -m 644 $RPM_SOURCE_DIR/nag.licence %{buildroot}/%{prefix}/lib

cp -a html doc %{buildroot}/%{prefix}

for x in KLICENCE.txt README.txt RELNOTES.txt TECHINFO.txt; do
  install -m 644 $x %{buildroot}/%{prefix}/doc
done

%clean
rm -rf %{buildroot}

%post
bindir=$RPM_INSTALL_PREFIX/bin
libdir=$RPM_INSTALL_PREFIX/lib

echo "#!/bin/sh" > $bindir/nagfor
echo $libdir/nagfor '"$@"' -Qpath $libdir >> $bindir/nagfor
chmod 755 $bindir/nagfor

echo "#!/bin/sh" > $bindir/dbx90
echo $libdir/dbx90 -Qpath $libdir '"$@"' >> $bindir/dbx90
chmod 755 $bindir/dbx90

%files
%defattr(-,root,root)
#%dir /opt/nag  # not for a relocatable package :(
%{prefix}
%ghost %{prefix}/bin/nagfor
%ghost %{prefix}/bin/dbx90

%changelog
* Fri Aug 26 2016 Neil Carlson <nnc@lanl.gov>
- Update to 6.1 build 6113.

* Tue Mar 29 2016 Neil Carlson <nnc@lanl.gov>
- Update to version 6.1

* Fri Jan 29 2016 Neil Carlson <nnc@lanl.gov>
- Update to edit 1067. New edit.

* Sat Jul 26 2015 Neil Carlson <nnc@lanl.gov>
- Update to edit 1057. New edit.

* Sat Jul 11 2015 Neil Carlson <nnc@lanl.gov>
- Update to edit 1054. New edit.

* Sun Jun 7 2015 Neil Carlson <nnc@lanl.gov>
- Update to edit 1052. Purportedly fixed two reported bugs.

* Tue May 19 2015 Neil Carlson <nnc@lanl.gov>
- Update to edit 1049.

* Sat Mar 21 2015 Neil Carlson <nnc@lanl.gov>
- Update to edit 1037.

* Mon Sep 22 2014 Neil Carlson <nnc@lanl.gov>
- Initial release of 6.0

* Thu Apr 24 2014 Neil Carlson <nnc@lanl.gov>
- Update to edit 983.  Fixes reported bug.

* Thu Apr 17 2014 Neil Carlson <nnc@lanl.gov>
- Update to edit 981.

* Fri Jan 17 2014 Neil Carlson <nnc@lanl.gov>
- Update to edit 978.  Fixes reported bug (with 975 and -nan).

* Mon Jan 6 2014 Neil Carlson <nnc@lanl.gov>
- Update to edit 973.  Fixes reported bug (with -C=all)

* Wed Dec 4 2013 Neil Carlson <nnc@lanl.gov>
- Update to edit 973

* Tue Oct 23 2013 Neil Carlson <nnc@lanl.gov>
- Update to edit 968.

* Mon Jun 5 2013 Neil Carlson <nnc@lanl.gov>
- Update to edit 950.

* Mon Apr 22 2013 Neil Carlson <nnc@lanl.gov>
- Update to 5.3.2 (942).

* Mon Jan 14 2013 Neil Carlson <nnc@lanl.gov>
- Update to edit 927.

* Fri Nov 16 2012 Neil Carlson <nnc@lanl.gov>
- Edit 917.  Fixes reported -C=all bug.

* Mon Nov 12 2012 Neil Carlson <nnc@lanl.gov>
- New edit.

* Thu Oct 4 2012 Neil Carlson <nnc@lanl.gov>
- New edit.

* Mon Jun 4 2012 Neil Carlson <nnc@lanl.gov>
- New edit.

* Thu Mar 29 2012 Neil Carlson <nnc@lanl.gov>
- New edit that fixes reported bug.

* Wed Mar 21 2012 Neil Carlson <nnc@lanl.gov>
- New edit that fixes several reported bugs.

* Wed Feb 22 2012 Neil Carlson <nnc@lanl.gov>
- New edit.

* Wed Feb 15 2012 Neil Carlson <nnc@lanl.gov>
- Edit that fixes serious compiler memory overwrite.

* Tue Feb 14 2012 Neil Carlson <nnc@lanl.gov>
- Edit that fixes -O bug with MERGE intrinsic.

* Sat Feb 4 2012 Neil Carlson <nnc@lanl.gov>
- Initial 5.3 release.  Don't distribute.

* Fri Oct 28 2011 Neil Carlson <nnc@lanl.gov>
- 5.3 release candidate. Includes trial license.

* Wed Jun 1 2011 Neil Carlson <nnc@lanl.gov>
- Update to beta pre-release of 5.3.  Don't distribute.

* Wed Apr 5 2011 Neil Carlson <nnc@lanl.gov>
- Update to beta pre-release of 5.3.  Don't distribute.

* Wed Mar 23 2011 Neil Carlson <nnc@lanl.gov>
- Beta pre-release of 5.3.  Don't distribute.
