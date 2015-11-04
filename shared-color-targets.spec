Summary:	Color targets from vendors for color calibration
Summary(pl.UTF-8):	Dane kolorów urządzeń na potrzeby kalibracji kolorów
Name:		shared-color-targets
Version:	0.1.6
Release:	1
License:	CC-BY-SA v3.0
Group:		Libraries
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
# Source0-md5:	96717436448c85477acded66a28c30c7
URL:		http://github.com/hughsie/shared-color-targets
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains target files for popular scanner calibration
targets.

%description -l pl.UTF-8
Ten pakiet zawiera pliki danych do kalibracji kolorów popularnych
skanerów.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%dir %{_datadir}/color/targets
%{_datadir}/color/targets/test.it8
%{_datadir}/color/targets/wolf_faust
%{_datadir}/shared-color-targets
