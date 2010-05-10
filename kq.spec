Summary:	Classic RPG game with castles and magic
Summary(pl.UTF-8):	Klasyczna gra RPG z zamkami i magią
Name:		kq
Version:	0.99
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/kqlives/20091214/%{name}-%{version}.tar.gz
# Source0-md5:	0bf9614e3be3d02795fe476227ab7330
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://kqlives.sourceforge.net/
BuildRequires:	allegro-devel >= 4.2.1
BuildRequires:	dumb-devel
BuildRequires:	lua50-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KQ is a open source CRPG, with eight playable characters, over twenty
maps, countless item, spells and enemies, all accompanied by music and
sound effects.

%description -l pl.UTF-8
KQ jest CRPG o otwartym kodzie źródłowym, cechującą się ośmioma
grywalnymi postaciami oraz ponad dwudziestoma mapami. Posiada
niezliczoną ilość rzeczy, czarów i wrogów. Wszystkiemu towarzyszy
wspaniała muzyka i efekty dźwiękowe.

%prep
%setup -q
%{__sed} 's/luac/luac50/g' -i scripts/Makefile.{am,in}

%build
CFLAGS="-I/usr/include/lua50 %{rpmcflags}"
%{configure}
%{__aclocal} -I m4
%{__autoconf}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/scripts
%attr(755,root,root) %{_libdir}/%{name}/scripts/*.lob
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%{_datadir}/%{name}/data/*
%dir %{_datadir}/%{name}/maps
%{_datadir}/%{name}/maps/*
%dir %{_datadir}/%{name}/music
%{_datadir}/%{name}/music/*
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/%{name}.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/%{name}.mo
%{_mandir}/man6/%{name}.6*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm