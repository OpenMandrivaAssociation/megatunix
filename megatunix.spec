%if %mandriva_branch == Cooker
# Cooker
%define release 2
%else
# Old distros
%define subrel 1
%define release 1
%endif

Summary:	MegaTunix Tuning Software
Name:		megatunix
Version:	0.9.23
Release:	%release
License:	GPLv2+
Group:		Networking/Other
URL:		http://sourceforge.net/projects/megatunix
Source0:	http://sourceforge.net/projects/megatunix/files/MegaTunix/%{version}/%{name}-%{version}.tar.gz
Patch0:		megatunix-0.9.23-glib_fix.diff
Patch1:		megatunix-0.9.23-menu_fixes.diff
BuildRequires:	autoconf automake libtool
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(gdkglext-1.0)
BuildRequires:	pkgconfig(gdkglext-x11-1.0)
BuildRequires:	pkgconfig(gdk-x11-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
BuildRequires:	pkgconfig(gtkglext-x11-1.0)
BuildRequires:	pkgconfig(gtk+-unix-print-2.0)
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
MegaTunix is a cross-platform tuning application for some of the available DIY
Fuel Injection controllers, including the MegaSquirt (MS1, MS1-Extra, MS2 and
MS2-Extra) as well as the FreeEMS EFI system and the JimStim ECU
stimulator/development tool.

%prep

%setup -q
%patch0 -p0
%patch1 -p1

%build
autoreconf -fi

%configure2_5x \
    --disable-rpath \
    --disable-static

%make

%install
rm -rf %{buildroot}

%makeinstall_std

rm -rf %{buildroot}%{_datadir}/icons

install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_liconsdir}

for i in automotive dashdesigner gaugedesigner megatunix mtxloader; do
    convert icons/${i}.xpm -resize 16x16 %{buildroot}%{_miconsdir}/${i}.png
    convert icons/${i}.xpm -resize 32x32 %{buildroot}%{_iconsdir}/${i}.png
    convert icons/${i}.xpm -resize 48x48 %{buildroot}%{_liconsdir}/${i}.png
done

%files
%doc AUTHORS CREDITS LICENSE README TODO
%{_sysconfdir}/xdg/menus/applications-merged/automotive.menu
%{_bindir}/dashdesigner
%{_bindir}/gaugedesigner
%{_bindir}/megatunix
%{_bindir}/msloader
%{_bindir}/mtxloader
%{_datadir}/MegaTunix
%{_datadir}/desktop-directories/Automotive.directory
%{_datadir}/applications/*.desktop
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png


%changelog
* Tue Jan 31 2012 Oden Eriksson <oeriksson@mandriva.com> 0.9.23-0.1mdv2011.0
+ Revision: 770083
- various fixes
- import megatunix


* Sat Jan 28 2012 Oden Eriksson <oeriksson@mandriva.com> 0.9.23-1
- first cut (even though i don't have use for it, yet :-))
