Summary:	MegaTunix Tuning Software
Name:		megatunix
Version:	0.9.23
Release:	1
License:	GPLv2+
Group:		Networking/Other
URL:		http://sourceforge.net/projects/megatunix
Source0:	http://sourceforge.net/projects/megatunix/files/MegaTunix/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf automake libtool
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk2-devel
BuildRequires:	gtkglext-devel
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libxml2-devel

%description
MegaTunix is a cross-platform tuning application for some of the available DIY
Fuel Injection controllers, including the MegaSquirt (MS1, MS1-Extra, MS2 and
MS2-Extra) as well as the FreeEMS EFI system and the JimStim ECU
stimulator/development tool.

%prep

%setup -q

%build
autoreconf -fi

%configure2_5x \
    --disable-rpath \
    --disable-static

%make

%install
rm -rf %{buildroot}

%makeinstall_std

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
%{_datadir}/icons/*.xpm

