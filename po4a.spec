#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : po4a
Version  : 0.57
Release  : 3
URL      : https://github.com/mquinson/po4a/archive/v0.57/po4a-0.57.tar.gz
Source0  : https://github.com/mquinson/po4a/archive/v0.57/po4a-0.57.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: po4a-bin = %{version}-%{release}
Requires: po4a-license = %{version}-%{release}
Requires: po4a-locales = %{version}-%{release}
Requires: po4a-man = %{version}-%{release}
Requires: po4a-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : docbook-xml
BuildRequires : libxslt
BuildRequires : perl(Locale::gettext)
BuildRequires : perl(SGMLS)
BuildRequires : perl(Text::WrapI18N)
BuildRequires : perl(Unicode::GCString)
BuildRequires : perl(YAML::Tiny)
BuildRequires : perl-Term-ReadKey
BuildRequires : util-linux

%description
# Introduction to Po4a
[![Build Status](https://travis-ci.org/mquinson/po4a.svg?branch=master)](https://travis-ci.org/mquinson/po4a)
[![First Timers Friendly](https://img.shields.io/badge/Beginners-Welcome-brightgreen.svg?style=flat-square)](http://www.firsttimersonly.com)

%package bin
Summary: bin components for the po4a package.
Group: Binaries
Requires: po4a-license = %{version}-%{release}

%description bin
bin components for the po4a package.


%package dev
Summary: dev components for the po4a package.
Group: Development
Requires: po4a-bin = %{version}-%{release}
Provides: po4a-devel = %{version}-%{release}
Requires: po4a = %{version}-%{release}

%description dev
dev components for the po4a package.


%package license
Summary: license components for the po4a package.
Group: Default

%description license
license components for the po4a package.


%package locales
Summary: locales components for the po4a package.
Group: Default

%description locales
locales components for the po4a package.


%package man
Summary: man components for the po4a package.
Group: Default

%description man
man components for the po4a package.


%package perl
Summary: perl components for the po4a package.
Group: Default
Requires: po4a = %{version}-%{release}

%description perl
perl components for the po4a package.


%prep
%setup -q -n po4a-0.57
cd %{_builddir}/po4a-0.57

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

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/po4a
cp %{_builddir}/po4a-0.57/COPYING %{buildroot}/usr/share/package-licenses/po4a/90322fd3c48fa996e2b0e59d99a045e3388d643a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
%find_lang po4a

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/msguntypot
/usr/bin/po4a
/usr/bin/po4a-gettextize
/usr/bin/po4a-normalize
/usr/bin/po4a-translate
/usr/bin/po4a-updatepo
/usr/bin/po4aman-display-po
/usr/bin/po4apod-display-po

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Locale::Po4a::AsciiDoc.3pm.gz
/usr/share/man/man3/Locale::Po4a::BibTeX.3pm.gz
/usr/share/man/man3/Locale::Po4a::Chooser.3pm.gz
/usr/share/man/man3/Locale::Po4a::Common.3pm.gz
/usr/share/man/man3/Locale::Po4a::Debconf.3pm.gz
/usr/share/man/man3/Locale::Po4a::Dia.3pm.gz
/usr/share/man/man3/Locale::Po4a::Docbook.3pm.gz
/usr/share/man/man3/Locale::Po4a::Guide.3pm.gz
/usr/share/man/man3/Locale::Po4a::Halibut.3pm.gz
/usr/share/man/man3/Locale::Po4a::Ini.3pm.gz
/usr/share/man/man3/Locale::Po4a::KernelHelp.3pm.gz
/usr/share/man/man3/Locale::Po4a::LaTeX.3pm.gz
/usr/share/man/man3/Locale::Po4a::Man.3pm.gz
/usr/share/man/man3/Locale::Po4a::NewsDebian.3pm.gz
/usr/share/man/man3/Locale::Po4a::Po.3pm.gz
/usr/share/man/man3/Locale::Po4a::Pod.3pm.gz
/usr/share/man/man3/Locale::Po4a::RubyDoc.3pm.gz
/usr/share/man/man3/Locale::Po4a::Sgml.3pm.gz
/usr/share/man/man3/Locale::Po4a::TeX.3pm.gz
/usr/share/man/man3/Locale::Po4a::Texinfo.3pm.gz
/usr/share/man/man3/Locale::Po4a::Text.3pm.gz
/usr/share/man/man3/Locale::Po4a::TransTractor.3pm.gz
/usr/share/man/man3/Locale::Po4a::Wml.3pm.gz
/usr/share/man/man3/Locale::Po4a::Xhtml.3pm.gz
/usr/share/man/man3/Locale::Po4a::Xml.3pm.gz
/usr/share/man/man3/Locale::Po4a::Yaml.3pm.gz

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/po4a/90322fd3c48fa996e2b0e59d99a045e3388d643a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/po4a-normalize.1p.gz
/usr/share/man/ca/man1/po4a-translate.1p.gz
/usr/share/man/ca/man3/Locale::Po4a::Dia.3pm.gz
/usr/share/man/ca/man3/Locale::Po4a::Guide.3pm.gz
/usr/share/man/ca/man3/Locale::Po4a::KernelHelp.3pm.gz
/usr/share/man/ca/man3/Locale::Po4a::LaTeX.3pm.gz
/usr/share/man/ca/man3/Locale::Po4a::Pod.3pm.gz
/usr/share/man/ca/man3/Locale::Po4a::Texinfo.3pm.gz
/usr/share/man/ca/man3/Locale::Po4a::TransTractor.3pm.gz
/usr/share/man/de/man1/msguntypot.1p.gz
/usr/share/man/de/man1/po4a-gettextize.1p.gz
/usr/share/man/de/man1/po4a-normalize.1p.gz
/usr/share/man/de/man1/po4a-translate.1p.gz
/usr/share/man/de/man1/po4a-updatepo.1p.gz
/usr/share/man/de/man1/po4a.1p.gz
/usr/share/man/de/man1/po4aman-display-po.1.gz
/usr/share/man/de/man1/po4apod-display-po.1.gz
/usr/share/man/de/man3/Locale::Po4a::AsciiDoc.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::BibTeX.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Chooser.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Common.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Dia.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Docbook.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Guide.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Halibut.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Ini.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::KernelHelp.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::LaTeX.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Man.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Po.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Pod.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Sgml.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::TeX.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Texinfo.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Text.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::TransTractor.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Wml.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Xhtml.3pm.gz
/usr/share/man/de/man3/Locale::Po4a::Xml.3pm.gz
/usr/share/man/de/man7/po4a.7.gz
/usr/share/man/es/man1/msguntypot.1p.gz
/usr/share/man/es/man1/po4a-gettextize.1p.gz
/usr/share/man/es/man1/po4a-normalize.1p.gz
/usr/share/man/es/man1/po4a-translate.1p.gz
/usr/share/man/es/man1/po4a-updatepo.1p.gz
/usr/share/man/es/man1/po4a.1p.gz
/usr/share/man/es/man1/po4aman-display-po.1.gz
/usr/share/man/es/man1/po4apod-display-po.1.gz
/usr/share/man/es/man3/Locale::Po4a::AsciiDoc.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::BibTeX.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Chooser.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Common.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Dia.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Docbook.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Guide.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Halibut.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Ini.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::KernelHelp.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::LaTeX.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Man.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Po.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Pod.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Sgml.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::TeX.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Texinfo.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Text.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::TransTractor.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Wml.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Xhtml.3pm.gz
/usr/share/man/es/man3/Locale::Po4a::Xml.3pm.gz
/usr/share/man/es/man7/po4a.7.gz
/usr/share/man/fr/man1/msguntypot.1p.gz
/usr/share/man/fr/man1/po4a-gettextize.1p.gz
/usr/share/man/fr/man1/po4a-normalize.1p.gz
/usr/share/man/fr/man1/po4a-translate.1p.gz
/usr/share/man/fr/man1/po4a-updatepo.1p.gz
/usr/share/man/fr/man1/po4a.1p.gz
/usr/share/man/fr/man1/po4aman-display-po.1.gz
/usr/share/man/fr/man1/po4apod-display-po.1.gz
/usr/share/man/fr/man3/Locale::Po4a::AsciiDoc.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::BibTeX.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Chooser.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Common.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Dia.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Guide.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Halibut.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Ini.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::KernelHelp.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::LaTeX.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Man.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Po.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Pod.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Sgml.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::TeX.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Texinfo.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Text.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::TransTractor.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Wml.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Xhtml.3pm.gz
/usr/share/man/fr/man3/Locale::Po4a::Xml.3pm.gz
/usr/share/man/fr/man7/po4a.7.gz
/usr/share/man/it/man1/msguntypot.1p.gz
/usr/share/man/it/man1/po4a-gettextize.1p.gz
/usr/share/man/it/man1/po4a-normalize.1p.gz
/usr/share/man/it/man1/po4a-translate.1p.gz
/usr/share/man/it/man1/po4a-updatepo.1p.gz
/usr/share/man/it/man1/po4a.1p.gz
/usr/share/man/it/man1/po4aman-display-po.1.gz
/usr/share/man/it/man1/po4apod-display-po.1.gz
/usr/share/man/it/man3/Locale::Po4a::AsciiDoc.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::BibTeX.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::Chooser.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::Common.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::Dia.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::Docbook.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::Guide.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::Halibut.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::Ini.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::KernelHelp.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::LaTeX.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::Pod.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::Sgml.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::Texinfo.3pm.gz
/usr/share/man/it/man3/Locale::Po4a::Wml.3pm.gz
/usr/share/man/ja/man1/msguntypot.1p.gz
/usr/share/man/ja/man1/po4a-gettextize.1p.gz
/usr/share/man/ja/man1/po4a-normalize.1p.gz
/usr/share/man/ja/man1/po4a-translate.1p.gz
/usr/share/man/ja/man1/po4a-updatepo.1p.gz
/usr/share/man/ja/man1/po4a.1p.gz
/usr/share/man/ja/man1/po4aman-display-po.1.gz
/usr/share/man/ja/man1/po4apod-display-po.1.gz
/usr/share/man/ja/man3/Locale::Po4a::AsciiDoc.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::BibTeX.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Chooser.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Common.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Dia.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Guide.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Halibut.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Ini.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::KernelHelp.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::LaTeX.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Man.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Po.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Pod.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Sgml.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::TeX.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Texinfo.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Text.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::TransTractor.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Wml.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Xhtml.3pm.gz
/usr/share/man/ja/man3/Locale::Po4a::Xml.3pm.gz
/usr/share/man/ja/man7/po4a.7.gz
/usr/share/man/man1/msguntypot.1p.gz
/usr/share/man/man1/po4a-gettextize.1p.gz
/usr/share/man/man1/po4a-normalize.1p.gz
/usr/share/man/man1/po4a-translate.1p.gz
/usr/share/man/man1/po4a-updatepo.1p.gz
/usr/share/man/man1/po4a.1p.gz
/usr/share/man/man1/po4aman-display-po.1.gz
/usr/share/man/man1/po4apod-display-po.1.gz
/usr/share/man/man7/po4a.7.gz
/usr/share/man/nl/man1/po4aman-display-po.1.gz
/usr/share/man/nl/man1/po4apod-display-po.1.gz
/usr/share/man/pl/man1/msguntypot.1p.gz
/usr/share/man/pl/man1/po4a-gettextize.1p.gz
/usr/share/man/pl/man1/po4a-normalize.1p.gz
/usr/share/man/pl/man1/po4a-translate.1p.gz
/usr/share/man/pl/man1/po4a-updatepo.1p.gz
/usr/share/man/pl/man1/po4a.1p.gz
/usr/share/man/pl/man1/po4aman-display-po.1.gz
/usr/share/man/pl/man1/po4apod-display-po.1.gz
/usr/share/man/pl/man3/Locale::Po4a::BibTeX.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Chooser.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Common.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Dia.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Guide.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Halibut.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Ini.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::KernelHelp.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::LaTeX.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Man.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Po.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Pod.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Sgml.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::TeX.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Texinfo.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Text.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::TransTractor.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Wml.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Xhtml.3pm.gz
/usr/share/man/pl/man3/Locale::Po4a::Xml.3pm.gz
/usr/share/man/pl/man7/po4a.7.gz
/usr/share/man/pt/man1/msguntypot.1p.gz
/usr/share/man/pt/man1/po4a-gettextize.1p.gz
/usr/share/man/pt/man1/po4a-normalize.1p.gz
/usr/share/man/pt/man1/po4a-translate.1p.gz
/usr/share/man/pt/man1/po4a-updatepo.1p.gz
/usr/share/man/pt/man1/po4a.1p.gz
/usr/share/man/pt/man1/po4aman-display-po.1.gz
/usr/share/man/pt/man1/po4apod-display-po.1.gz
/usr/share/man/pt/man3/Locale::Po4a::AsciiDoc.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::BibTeX.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Chooser.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Common.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Dia.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Docbook.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Guide.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Halibut.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Ini.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::KernelHelp.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::LaTeX.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Man.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Po.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Pod.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Sgml.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::TeX.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Texinfo.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Text.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::TransTractor.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Wml.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Xhtml.3pm.gz
/usr/share/man/pt/man3/Locale::Po4a::Xml.3pm.gz
/usr/share/man/pt/man7/po4a.7.gz
/usr/share/man/pt_BR/man1/msguntypot.1p.gz
/usr/share/man/pt_BR/man1/po4a-gettextize.1p.gz
/usr/share/man/pt_BR/man1/po4a-normalize.1p.gz
/usr/share/man/pt_BR/man1/po4a-translate.1p.gz
/usr/share/man/pt_BR/man1/po4a-updatepo.1p.gz
/usr/share/man/pt_BR/man1/po4a.1p.gz
/usr/share/man/pt_BR/man1/po4aman-display-po.1.gz
/usr/share/man/pt_BR/man1/po4apod-display-po.1.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::AsciiDoc.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::BibTeX.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Chooser.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Common.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Dia.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Docbook.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Guide.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Halibut.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Ini.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::KernelHelp.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::LaTeX.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Man.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Po.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Pod.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Sgml.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::TeX.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Texinfo.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Text.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::TransTractor.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Wml.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Xhtml.3pm.gz
/usr/share/man/pt_BR/man3/Locale::Po4a::Xml.3pm.gz
/usr/share/man/pt_BR/man7/po4a.7.gz
/usr/share/man/ru/man1/msguntypot.1p.gz
/usr/share/man/ru/man1/po4a-gettextize.1p.gz
/usr/share/man/ru/man1/po4a-normalize.1p.gz
/usr/share/man/ru/man1/po4a-translate.1p.gz
/usr/share/man/ru/man1/po4a-updatepo.1p.gz
/usr/share/man/ru/man1/po4aman-display-po.1.gz
/usr/share/man/ru/man1/po4apod-display-po.1.gz
/usr/share/man/ru/man3/Locale::Po4a::Man.3pm.gz
/usr/share/man/uk/man1/msguntypot.1p.gz
/usr/share/man/uk/man1/po4a-gettextize.1p.gz
/usr/share/man/uk/man1/po4a-normalize.1p.gz
/usr/share/man/uk/man1/po4a-translate.1p.gz
/usr/share/man/uk/man1/po4a-updatepo.1p.gz
/usr/share/man/uk/man1/po4a.1p.gz
/usr/share/man/uk/man1/po4aman-display-po.1.gz
/usr/share/man/uk/man1/po4apod-display-po.1.gz
/usr/share/man/uk/man3/Locale::Po4a::AsciiDoc.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::BibTeX.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Chooser.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Common.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Dia.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Docbook.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Guide.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Halibut.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Ini.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::KernelHelp.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::LaTeX.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Man.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Po.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Pod.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Sgml.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::TeX.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Texinfo.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Text.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::TransTractor.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Wml.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Xhtml.3pm.gz
/usr/share/man/uk/man3/Locale::Po4a::Xml.3pm.gz
/usr/share/man/uk/man7/po4a.7.gz
/usr/share/man/zh_CHS/man1/po4aman-display-po.1.gz

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/AsciiDoc.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/BibTeX.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Chooser.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Common.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Dia.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Docbook.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Guide.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Halibut.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/InProgress/Debconf.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/InProgress/NewsDebian.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Ini.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/KernelHelp.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/LaTeX.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Man.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Po.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Pod.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/RubyDoc.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Sgml.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/TeX.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Texinfo.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Text.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/TransTractor.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Wml.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Xhtml.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Xml.pm
/usr/lib/perl5/vendor_perl/5.30.1/Locale/Po4a/Yaml.pm

%files locales -f po4a.lang
%defattr(-,root,root,-)

