#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-ShareDir
Version  : 1.118
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-ShareDir-1.118.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-ShareDir-1.118.tar.gz
Summary  : 'Locate per-dist and per-module shared files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-ShareDir-license = %{version}-%{release}
Requires: perl-File-ShareDir-perl = %{version}-%{release}
Requires: perl(Class::Inspector)
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Exporter::Tiny)
BuildRequires : perl(File::ShareDir::Install)
BuildRequires : perl(List::MoreUtils)
BuildRequires : perl(Params::Util)

%description
# NAME
File::ShareDir - Locate per-dist and per-module shared files
<div>
<a href="https://travis-ci.org/perl5-utils/File-ShareDir"><img src="https://travis-ci.org/perl5-utils/File-ShareDir.svg?branch=master" alt="Travis CI"/></a>
<a href='https://coveralls.io/github/perl5-utils/File-ShareDir?branch=master'><img src='https://coveralls.io/repos/github/perl5-utils/File-ShareDir/badge.svg?branch=master' alt='Coverage Status' /></a>
<a href="https://saythanks.io/to/rehsack"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg" alt="Say Thanks" /></a>
</div>

%package dev
Summary: dev components for the perl-File-ShareDir package.
Group: Development
Provides: perl-File-ShareDir-devel = %{version}-%{release}
Requires: perl-File-ShareDir = %{version}-%{release}

%description dev
dev components for the perl-File-ShareDir package.


%package license
Summary: license components for the perl-File-ShareDir package.
Group: Default

%description license
license components for the perl-File-ShareDir package.


%package perl
Summary: perl components for the perl-File-ShareDir package.
Group: Default
Requires: perl-File-ShareDir = %{version}-%{release}

%description perl
perl components for the perl-File-ShareDir package.


%prep
%setup -q -n File-ShareDir-1.118
cd %{_builddir}/File-ShareDir-1.118

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-ShareDir
cp %{_builddir}/File-ShareDir-1.118/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-ShareDir/1f9320711c50d58e122b9880cee3426956e9dc15
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::ShareDir.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-ShareDir/1f9320711c50d58e122b9880cee3426956e9dc15

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/File/ShareDir.pm
/usr/lib/perl5/vendor_perl/5.34.0/auto/share/dist/File-ShareDir/sample.txt
/usr/lib/perl5/vendor_perl/5.34.0/auto/share/dist/File-ShareDir/subdir/sample.txt
/usr/lib/perl5/vendor_perl/5.34.0/auto/share/module/File-ShareDir/test_file.txt
