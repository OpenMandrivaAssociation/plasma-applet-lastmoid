Name:           plasma-applet-lastmoid
Summary:        Lastmoid is a plasmoid for LastFm users
Version:        0.6.5
Release:        %mkrel 1
Url:            http://kde-look.org/content/show.php/Lastmoid?content=98117
License:        GPLv2+
Group:          Graphical desktop/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:      	http://kde-look.org/CONTENT/content-files/98117-vavrusa-lastmoid-2041bf6.tar.gz
BuildRequires:  plasma-devel

%description
Lastmoid is a plasmoid for LastFm users. It displays your weekly, 
3 months, 12 month or your overall charts (albums/tracks/artists) 
easily on your favorite desktop

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_lastmoid.so
%_kde_appsdir/desktoptheme/default/widgets/lastmoid.svg
%_kde_datadir/kde4/services/plasma-applet-lastmoid.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n vavrusa-lastmoid-2041bf6

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot

