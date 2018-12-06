#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-ShareDir
Version  : 1.116
Release  : 11
URL      : http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/File-ShareDir-1.116.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/R/RE/REHSACK/File-ShareDir-1.116.tar.gz
Summary  : 'Locate per-dist and per-module shared files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-ShareDir-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Inspector)
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

%description dev
dev components for the perl-File-ShareDir package.


%package license
Summary: license components for the perl-File-ShareDir package.
Group: Default

%description license
license components for the perl-File-ShareDir package.


%prep
%setup -q -n File-ShareDir-1.116

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-ShareDir
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-File-ShareDir/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1/File/ShareDir.pm
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/File-ShareDir/sample.txt
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/File-ShareDir/subdir/sample.txt
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/module/File-ShareDir/test_file.txt

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::ShareDir.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-ShareDir/LICENSE
