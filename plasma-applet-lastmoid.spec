Name:           plasma-applet-lastmoid
Summary:        Lastmoid is a plasmoid for LastFm users
Version:        0.6.5
Release:        4
Url:            https://kde-look.org/content/show.php/Lastmoid?content=98117
License:        GPLv2+
Group:          Graphical desktop/KDE
Source0:      	http://kde-look.org/CONTENT/content-files/98117-vavrusa-lastmoid-2041bf6.tar.gz
BuildRequires:	kdebase4-workspace-devel

%description
Lastmoid is a plasmoid for LastFm users. It displays your weekly, 
3 months, 12 month or your overall charts (albums/tracks/artists) 
easily on your favorite desktop

%files
%{_kde_libdir}/kde4/plasma_applet_lastmoid.so
%{_kde_appsdir}/desktoptheme/default/widgets/lastmoid.svg
%{_kde_services}/plasma-applet-lastmoid.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n vavrusa-lastmoid-2041bf6

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.5-2mdv2011.0
+ Revision: 614567
- the mass rebuild of 2010.1 packages

* Mon Dec 21 2009 Rémy Clouard <shikamaru@mandriva.org> 0.6.5-1mdv2010.1
+ Revision: 481061
- bump release

* Fri May 08 2009 Funda Wang <fwang@mandriva.org> 0.5-1mdv2010.0
+ Revision: 373399
- New version 0.5

* Wed Mar 18 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.4-1mdv2009.1
+ Revision: 357235
- Initial Mandriva package, from R?\195?\169my Clouard


