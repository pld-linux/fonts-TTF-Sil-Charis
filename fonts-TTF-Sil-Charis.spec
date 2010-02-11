Summary:	Charis SIL - TrueType Fonts
Summary(pl.UTF-8):	Charis SIL - fonty TrueType
Name:		fonts-TTF-CharisSIL
Version:	4.106
Release:	1
License:	SIL OFL
Group:		Fonts
# Source0Download:	http://scripts.sil.org/cms/scripts/render_download.php?site_id=nrsi&format=file&media_id=CharisSIL4.106b.zip&filename=CharisSIL4.106.zip
Source0:	CharisSIL%{version}.zip
# Source0-md5:	045aea5116c6c20e5b84e165d9727f0c
URL:		http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=CharisSILfont
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Charis is similar to Bitstream Charter, one of the first fonts
designed specifically for laser printers. It is highly readable and
holds up well in less-than-ideal reproduction environments. It also
has a full set of styles - regular, italic, bold, bold italic - and so
is more useful in general publishing than Doulos SIL. Charis is a
serif, proportionally-spaced font optimized for readability in long
printed documents.

The goal for this product was to provide a single Unicode-based font
family that would contain a comprehensive inventory of glyphs needed
for almost any Roman- or Cyrillic-based writing system, whether used
for phonetic or orthographic needs. In addition, there is provision
for other characters and symbols useful to linguists. This font makes
use of state-of-the-art font technologies to support complex
typographic issues, such as the need to position arbitrary
combinations of base glyphs and diacritics optimally.

%description -l pl.UTF-8
Charis jest podobny do Bitstream Charter, jednego z pierwszych fontów
zaprojektowanych specjalnie dla drukarek laserowych. Jest bardzo
czytelny i sprawdza się również w gorszych warunkach druku. Oferuje
pełen zestaw stylów: zwykły, kursywę, pogrubiony, pogrubioną kursywę -
jest więc bardziej użyteczny w wydawaniu tekstów niż Doulos SIL.
Charis jest fontem szeryfowym, proporcjonalnym, zoptymalizowanym pod
względem czytelności długich drukowanych dokumentów.

Przeznaczeniem niniejszego produktu jest zaoferowanie jednej
unikodowej rodziny fontów, która zawiera obszerny inwentarz glifów
potrzebnych do niemal każdego systemu pisma opartego na alfabecie
łacińskim bądź cyrylicy, zarówno dla potrzeb fonetycznych, jak i
ortograficznych. Dodatkowo dostarczone są znaki i symbole użyteczne
dla językoznawców. Font ten używa najnowszych technik fontów
wspierających złożone zagadnienia typograficzne, takie jak optymalne
pozycjonowanie dowolnych kombinacji glifów bazowych i diakrytyków.

%prep
%setup -q -n CharisSIL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc *.txt
%{ttffontsdir}/CharisSIL*.ttf
