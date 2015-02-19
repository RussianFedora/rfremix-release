%define release_name Twenty Two
%define dist_version 22
# validate at 20101017. only increase rfremix_version
%define rfremix_version 22
%define bug_version 22

Summary:	RFRemix release files
Name:		rfremix-release
Version:	22
Release:	0.12.R
Epoch:		2
License:	MIT
Group:		System Environment/Base
URL:		http://russianfedora.pro
Source:		%{name}-%{version}.tar.bz2

Obsoletes:	redhat-release
Provides:	redhat-release
Provides:	system-release = %{epoch}:%{version}-%{release}
Provides:	fedora-release = %{epoch}:%{version}-%{release}
Provides:	generic-release = %{epoch}:%{version}-%{release}
Provides:	system-release(%{version})
Requires:       fedora-repos(%{version})
Requires:	rfremix-config
Obsoletes:	russianfedora-repos < %{version}
Obsoletes:	fedora-release
Obsoletes:	generic-release
BuildArch:	noarch

%description
RFRemix release files such as yum configs and various /etc/ files that
define the release.


%package nonproduct
Summary:        Base package for non-product-specific default configurations
Provides:       system-release-nonproduct
Provides:       system-release-nonproduct(%{version})
Provides:       system-release-product
# turned out to be a bad name
Provides:       fedora-release-standard = 21-0.16
Provides:       rfremix-release-standard = 21-0.16
Obsoletes:      fedora-release-standard < 21-0.16
Obsoletes:      rfremix-release-standard < 21-0.16
Obsoletes:      fedora-release-nonproduct
Requires:       rfremix-release = %{epoch}:%{version}-%{release}
Conflicts:      fedora-release-cloud
Conflicts:      rfremix-release-cloud
Conflicts:      fedora-release-server
Conflicts:      rfremix-release-server
Conflicts:      fedora-release-workstation
Conflicts:      rfremix-release-workstation

%description nonproduct
Provides a base package for non-product-specific configuration files to
depend on.

%package cloud
Summary:        Base package for RFRemix Cloud-specific default configurations
Provides:       system-release-cloud
Provides:       system-release-cloud(%{version})
Provides:       system-release-product
Requires:       rfremix-release = %{epoch}:%{version}-%{release}
Obsoletes:	fedora-release-cloud
Conflicts:      fedora-release-server
Conflicts:      rfremix-release-server
Conflicts:      fedora-release-standard
Conflicts:      rfremix-release-standard
Conflicts:      fedora-release-workstation
Conflicts:      rfremix-release-workstation

%description cloud
Provides a base package for RFRemix Cloud-specific configuration files to
depend on.

%package server
Summary:        Base package for RFRemix Server-specific default configurations
Provides:       system-release-server
Provides:       system-release-server(%{version})
Provides:       system-release-product
Requires:       rfremix-release = %{epoch}:%{version}-%{release}
Obsoletes:	fedora-release-server
Requires:       systemd
Requires:       cockpit
Requires:       rolekit
Requires(post): sed
Requires(post): systemd
Conflicts:      fedora-release-cloud
Conflicts:      rfremix-release-cloud
Conflicts:      fedora-release-standard
Conflicts:      rfremix-release-standard
Conflicts:      fedora-release-workstation
Conflicts:      rfremix-release-workstation

%description server
Provides a base package for RFRemix Server-specific configuration files to
depend on.

%package workstation
Summary:        Base package for RFRemix Workstation-specific default configurations
Provides:       system-release-workstation
Provides:       system-release-workstation(%{version})
Provides:       system-release-product
Requires:       fedora-release = %{epoch}:%{version}-%{release}
Obsoletes:      fedora-release-workstation
Conflicts:      fedora-release-cloud
Conflicts:      rfremix-release-cloud
Conflicts:      fedora-release-server
Conflicts:      rfremix-release-server
Conflicts:      fedora-release-standard
Conflicts:      rfremix-release-standard
# needed for captive portal support
Requires:       NetworkManager-config-connectivity-fedora

Requires(post): /usr/bin/glib-compile-schemas
Requires(postun): /usr/bin/glib-compile-schemas

%description workstation
Provides a base package for RFRemix Workstation-specific configuration files to
depend on.

%prep
%setup -q
sed -i 's|@@VERSION@@|%{dist_version}|g' Fedora-Legal-README.txt

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc
echo "Fedora release %{version} (%{release_name})" > $RPM_BUILD_ROOT/etc/fedora-release
echo "RFRemix release %{rfremix_version} (%{release_name})" > $RPM_BUILD_ROOT/etc/rfremix-release
echo "cpe:/o:fedoraproject:fedora:%{version}" > $RPM_BUILD_ROOT/etc/system-release-cpe
cp -p $RPM_BUILD_ROOT/etc/rfremix-release $RPM_BUILD_ROOT/etc/issue
echo "Kernel \r on an \m (\l)" >> $RPM_BUILD_ROOT/etc/issue
cp -p $RPM_BUILD_ROOT/etc/issue $RPM_BUILD_ROOT/etc/issue.net
echo >> $RPM_BUILD_ROOT/etc/issue
ln -s fedora-release $RPM_BUILD_ROOT/etc/redhat-release
ln -s fedora-release $RPM_BUILD_ROOT/etc/system-release

install -d $RPM_BUILD_ROOT/usr/lib
cat << EOF >>$RPM_BUILD_ROOT/usr/lib/os-release
NAME=Fedora
VERSION="%{rfremix_version} (%{release_name})"
ID=fedora
ID_LIKE=fedora
VERSION_ID=%{rfremix_version}
PRETTY_NAME="RFRemix %{rfremix_version} (%{release_name})"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:fedoraproject:fedora:%{version}"
HOME_URL="https://fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=%{bug_version}
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=%{bug_version}
PRIVACY_POLICY=https://fedoraproject.org/wiki/Legal:PrivacyPolicy
EOF

ln -s /usr/lib/os-release $RPM_BUILD_ROOT/etc/os-release

# Set up the dist tag macros
install -d -m 755 $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d
cat >> $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d/macros.dist << EOF
# dist macros.

%%fedora                %{dist_version}
%%dist                .fc%{dist_version}.R
%%fc%{dist_version}                1
EOF

# Add Product-specific presets
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-preset/
# Fedora Server
install -m 0644 80-server.preset %{buildroot}%{_prefix}/lib/systemd/system-preset/

# Override the list of enabled gnome-shell extensions for Workstation
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -m 0644 org.gnome.shell.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/


%post server
if [ $1 -eq 1 ] ; then
        # Initial installation; fix up after %%systemd_post in packages
        # possibly installed before our preset file was added
        units=$(sed -n 's/^enable//p' \
                < %{_prefix}/lib/systemd/system-preset/80-server.preset)
        /usr/bin/systemctl preset $units >/dev/null 2>&1 || :
fi

%postun workstation
if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans workstation
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license LICENSE Fedora-Legal-README.txt
%config %attr(0644,root,root) /usr/lib/os-release
/etc/os-release
%config %attr(0644,root,root) /etc/fedora-release
%config %attr(0644,root,root) /etc/rfremix-release
/etc/redhat-release
/etc/system-release
%config %attr(0644,root,root) /etc/system-release-cpe
%config(noreplace) %attr(0644,root,root) /etc/issue
%config(noreplace) %attr(0644,root,root) /etc/issue.net
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist

%files nonproduct
%{!?_licensedir:%global license %%doc}
%license LICENSE

%files cloud
%{!?_licensedir:%global license %%doc}
%license LICENSE

%files server
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_prefix}/lib/systemd/system-preset/80-server.preset

%files workstation
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.override

%changelog
* Sun Dec  7 2014 Arkady L. Shane <ashejn@russianfedora.pro> - 21-1.R
- ship an override file to enable the gnome-shell background logo extension
- drop Require on system-release-product rhbz#1156198
- final RFRemix 21

* Wed Nov 12 2014 Arkady L. Shane <ashejn@russianfedora.pro> - 21-0.16.3.R
- use ID=fedora for proper abrt working

* Tue Nov 11 2014 Arkady L. Shane <ashejn@russianfedora.pro> - 21-0.16.2.R
- O: fedora-release-nonproduct for rfremix-release-nonproduct package

* Tue Nov 11 2014 Arkady L. Shane <ashejn@russianfedora.pro> - 21-0.16.1.R
- all packages should P: system-release-product

* Tue Nov 11 2014 Arkady L. Shane <ashejn@russianfedora.pro> - 21-0.16.R
- rename fedora-release-standard to fedora-release-nonproduct
- add requires for captive portal to Workstation

* Thu Aug  7 2014 Arkady L. Shane <ashejn@russianfedora.pro> - 21-0.13.R
- sync with upstream

* Fri Jun 27 2014 Arkady L. Shane <ashejn@russianfedora.pro> - 21-0.7.1.R
- added epoch to require

* Thu Jun 26 2014 Arkady L. Shane <ashejn@russianfedora.pro> - 21-0.7.R
- update Fedora-Legal-README.txt with updates from legal rhbz#1096434
- Change license to MIT to reflect the change in the fedora compilation
- based on reccomendations from Red Hat Legal rhbz#1096434

* Wed Feb 17 2014 Dennis Gilmore <dennis@ausil.us> - 21-0.5.R
- provide system-release(%%version) rhbz#1047058

* Mon Jan 13 2014 Dennis Gilmore <dennis@ausil.us> - 21-0.4.R
- set metadata expiry to 12 hours as dnf defaults to something silly bz#1045678

* Sat Dec 28 2013 Ville Skyttä <ville.skytta@iki.fi> - 21-0.3.R
- Install macros.dist as non-%%config to %%{_rpmconfigdir}/macros.d (#846679).
- Fix bogus date in %%changelog.

* Wed Nov 13 2013 Dennis Gilmore <dennis@ausil.us> - 21-0.2.R
- remove f20 keys add f21
- patch from Will Woods to use a archmap file for linking gpg keys
- add fields to /etc/os-release for rhbz#951119
- set skip_if_unavailable=False for rhbz#985354

* Wed Sep  4 2013 Arkady L. Shane <ashejn@yandex-team.ru> - 21-0.1.R
- sync with new rawhide

* Wed Sep  4 2013 Arkady L. Shane <ashejn@yandex-team.ru> - 20-0.6.R
- sync with upstream

* Wed Mar 13 2013 Arkady L. Shane <ashejn@yandex-team.ru> - 20-0.1.R
- rebase on RFRemix 20

* Mon Jan 14 2013 Arkady L. Shane <ashejn@yandex-team.ru> - 19-0.2.2.R
- sync with rfremix-release 18

* Wed Aug 22 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 19-0.2.1.R
- real fix

* Wed Aug 22 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 19-0.2.R
- fix rfremix version

* Tue Aug 21 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 19-0.1.R
- setup for f/rfr 19

* Wed Mar 20 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 18-0.4.R
- added Fedora-Legal-README.txt
- prepare media repo for Alpha and Beta

* Mon Feb 27 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 18-0.3.R
- %%dist is now with .R

* Sun Feb 12 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 18-0.2.R
- next upstream release

* Thu Dec  8 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 17-0.2.R
- update for rawhide

* Wed Oct 26 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 16-1.R
- enable updates
- disable updates-testing
- set metadate_expire to 7days on the fedora repo

* Fri Sep 16 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 16-0.9.R
- update for RFRemix 16-Beta

* Fri May 13 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 15-1.R
- enable updates
- disable updates-testing
- enable metadata_expire for 7 days for fedora repo
- link system- and redhat-release to rfremix-release again

* Thu Mar 17 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 15-0.8
- system- and redhat-release links to fedora-release

* Thu Mar 17 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 15-0.7
- update to RFRemix 15 Beta

* Wed Mar  9 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 14-3
- update rfremix to 14.1

* Fri Oct 22 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 14-2
- forget epoch in Requires.

* Mon Oct 18 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 14-1
- final release

* Mon Oct 18 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 14-0.11
- fedora-release use Fedora release_name as it was (smolt patched)
- redhat-release links to rfremix-release (for gdm)

* Thu Oct 14 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 14-0.10
- user rfremix version also in fedora-release file
- support 14 version in media-dvd file

* Wed Sep 29 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 14-0.9
- bump epoch to update from RFRemix 13.1

* Tue Sep 21 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 14-0.8
- rfremix-config now separate package
- update to pre release

* Mon Mar 15 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 14-0.4
- update to RFRemix 14

* Thu Nov 12 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 12-2
- fix keys path for rawhide and updates-testing

* Sat Nov  7 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 12-1
- bump to 12 release
- drop old config lines from rfremixconf
- added post to disable rawhide repos

* Tue Oct 27 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11.93-5
- add test for existing /sbin/chkconfig in scripts
- update switch keyboard script (oh, gdm is so buggy and now
  this script is also buggy, but I think you will not see it)

* Mon Oct 19 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11.93-4
- just added 12-Beta in install-dvd repo file

* Thu Oct 15 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11.93-3
- disable some preferences as they present in firstboot now

* Wed Oct 14 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11.93-2

* Wed Oct 14 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11.93-2
- remove version at Obsoletes

* Wed Oct 14 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11.93-1
- bump release
- rename russianfedoraremix to rfremix everywhere

* Thu Sep 24 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11.92-4
- try to use gnome-bluetooth, so disabe hiding icon
- added media installation again

* Tue Sep 22 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11.92-3
- turn on icons in menus

* Fri Sep 18 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11.92-2
- cleanup init script

* Thu Sep 17 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11.92-1
- update for new rawhide

* Mon Jun  8 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11-3
- do not rename distribution in grub.conf
- remove anaconda repos

* Fri Jun  5 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11-2
- changename
- bump epoch

* Tue Jun  2 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11-7rfr
- remix fix

* Tue Jun  2 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11-6rfr
- update special repo file
- remove postun macro
- fucking remix:(

* Tue May 26 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11-5russianfedora
- we do not need to start russianfedoraconf init script every time after
  update. It will start after reboot.

* Mon May 25 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11-4russianfedora
- disable gnome-bluetooth icon if blueman is present

* Mon May 25 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11-3russianfedora
- enable fedora and fedora-update by default as anaconda use only special
  repo file. Disable manipulation in russianfedoraconf with repo files too.
- disable special repos by default

* Tue May 19 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11-2russianfedora
- disable fedora and fedora-update during installation

* Tue May 12 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 11-1russianfedora
- update to 11

* Sat May  2 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.93-2russianfedora
- bump release

* Sun Apr 26 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-18russianfedora
- don't set kdm by default if lxde installed

* Sun Apr 19 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-17russianfedora
- remove rpmnew and rpmsave repo files
- russianfedora-config requires fedora-release
- fix release anaconda repo file

* Sun Apr 19 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-16russianfedora
- fix scripts

* Sun Apr 19 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-15russianfedora
- merge all anaconda repo files in two (for devel and for release)
- remove russianfedora-repos package

* Sat Apr 18 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-14russianfedora
- fix preun script
- fix nonfree repo

* Wed Apr 15 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-13russianfedora
- fix enabling repos at first boot
- add rule for eog

* Sat Apr 11 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-12russianfedora
- remove xfce xkb configure at all
- enable layout (w/o options) set for GNOME.

* Thu Apr  9 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-11russianfedora
- install kxkbrc in /etc/skel again (conflicts with kde-settings)

* Thu Apr  9 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-10russianfedora
- add gdm detection in layout script
- move kxkbrc to kde-settings directory instead of /etc/skel
- remove xfce xkb settings as it works through the time

* Wed Apr  8 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-9russianfedora
- added script for pushing layout and options to session

* Wed Apr  8 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-8russianfedora
- xfce xkb plugin is very buggy
- tey say that X works proper in VirtualBox

* Sun Apr  5 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-7russianfedora
- update XFCE's xkb config for new xfce4-xkb-plugin

* Sun Apr  5 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-6russianfedora
- fix output in init script

* Wed Apr  1 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-5russianfedora
- fix setroubleshoot removing

* Tue Mar 31 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-4russianfedora
- update DVD repo path

* Tue Mar 31 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-3russianfedora
- add sloppy focus for metacity
- remove setroubleshoot packages if SELinux mode is not enforcing

* Thu Mar 26 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-2russianfedora
- fix default xkb config for XFCE
- add default xkb config for KDE

* Wed Mar 25 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-1russianfedora
- for upgrade we need higher release then in Fedora. Bump release
- fix varinat in XFCE xkb

* Tue Mar 24 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-0.5
- XFCE xkb config must be never_modify_config=false
- remove it when package remove

* Tue Mar 24 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-0.4
- added layout switching configuration for GNOME and KDE
- add full config for XFCE including layout switching
- fix enabling fedora-rawhide during first configure
- fix removing anaconda repos

* Tue Mar 18 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-0.3
- update version in media install dvd script
- fix russianfedoraconf for rawhide

* Thu Mar 12 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-0.2
- update media dvd repo file

* Thu Mar 12 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.92-0.1
- russianfedorize

* Mon Mar 09 2009 Jesse Keating <jkeating@redhat.com> - 10.92-1
- Bump for F11 Beta
- Add the (giant) F11 Test key

* Thu Mar 05 2009 Jesse Keating <jkeating@redhat.com> - 10.91-4
- Drop req on fedora-release-notes (#483018)

* Tue Mar 03 2009 Jesse Keating <jkeating@redhat.com> - 10.91-3
- Move metalink urls to mirrorlist for helping anaconda

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Jesse Keating <jkeating@redhat.com> - 10.91-1
- Use the correct CPE name (#481287)

* Wed Jan 21 2009 Jesse Keating <jkeating@redhat.com> - 10.91-1
- Update for Fedora 11 Alpha
- Use metalink urls to get mirror information

* Wed Oct 01 2008 Jesse Keating <jkeating@redhat.com> - 10.90-1
- Initial build for Fedora 11.

* Mon Sep 15 2008 Jesse Keating <jkeating@redhat.com> - 9.91-1
- Update for Fedora 10 beta
- Add the new keys for F10
- Remove F8/9 keys
- Update compose configs
- Clarify rawhide repo definition

* Wed Jun 11 2008 Jesse Keating <jkeating@redhat.com> - 9.90-2
- Package up the ia64 key as the first secondary arch
- Mark config files correctly
- Stop using download.fedora.redhat.com and use download.fedoraproject.org instead

* Mon Mar 31 2008 Jesse Keating <jkeating@redhat.com> - 9.90-1
- Update for Fedora 10 rawhide.

* Thu Mar 13 2008 Jesse Keating <jkeating@redhat.com> - 8.92-1
- Update for 9 Beta
- Update the compose files for 9 Beta
- Add system-release-cpe (from Mark Cox)
- Add terminal to issue (#436387)
- Rename development to rawhide where appropriate.

* Wed Oct 10 2007 Jesse Keating <jkeating@redhat.com> - 8.90-3
- Bump for cvs oopsie

* Wed Oct 10 2007 Jesse Keating <jkeating@redhat.com> - 8.90-2
- Add the gpg info to the devel repo

* Wed Oct 03 2007 Jesse Keating <jkeating@redhat.com> - 8.90-1
- First build for Fedora 9 development.

* Fri Sep 28 2007 Jesse Keating <jkeating@redhat.com> - 7.92-1
- Bump for F8 Test2.
- Package up the compose kickstart files

* Fri Sep 14 2007 Jesse Keating <jkeating@redhat.com> - 7.91-2
- Use failovermethod=priority in yum configs (243698)

* Thu Aug 30 2007 Jesse Keating <jkeating@redhat.com> - 7.91-1
- Provide system-release, useful for spinoffs.
- Also link system-release to fedora-release for file level checks
- Bump for F8 Test2
- Fix license tag

* Thu Jul 27 2007 Jesse Keating <jkeating@redhat.com> - 7.90-1
- Bump for F8 Test1

* Thu Jun 28 2007 Jesse Keating <jkeating@redhat.com> - 7.89-3
- Cleanups from review
- Don't (noreplace) the dist tag macro file

* Tue Jun 19 2007 Jesse Keating <jkeating@redhat.com> - 7.89-2
- Define the dist macros in this package since we define everyting else here

* Wed May 30 2007 Jesse Keating <jkeating@redhat.com> - 7.89-1
- And we're back to rawhide.  Re-enable devel repos

* Thu May 24 2007 Jesse Keating <jkeating@redhat.com> - 7-3
- We have a name!
- Require the newer release notes

* Mon May 21 2007 Jesse Keating <jkeating@redhat.com> - 7-2
- Use Everything in the non-mirror URL to the release tree

* Mon May 21 2007 Jesse Keating <jkeating@redhat.com> - 7-1
- First build for Fedora 7
- Remove Extras repos (YAY!)
- Remove references to "core" in repo files.
- Adjust repo files for new mirror structure
- Remove Legacy repo

* Fri Apr 20 2007 Jesse Keating <jkeating@redhat.com> - 6.93-1
- Bump for Test 4

* Mon Mar 19 2007 Jesse Keating <jkeating@redhat.com> - 6.92-1
- Bump for Test 3
- No more eula in fedora-release, moved to firstboot

* Fri Feb 23 2007 Jesse Keating <jkeating@redhat.com> - 6.91-1
- Bump for Test 2

* Tue Feb 13 2007 Jesse Keating <jkeating@redhat.com> - 6.90-4
- Specfile cleanups

* Mon Feb 05 2007 Jesse Keating <jkeating@redhat.com> - 6.90-3
- Drop the legacy repo file.

* Fri Jan 26 2007 Jesse Keating <jkeating@redhat.com> - 6.90-2
- Core?  What Core?

* Wed Jan 24 2007 Jeremy Katz <katzj@redhat.com> - 6.90-1
- Bump to 6.90.  Keep working with older release notes

* Mon Oct 16 2006 Jesse Keating <jkeating@redhat.com> - 6-89
- Keep version 6, bump release.  Saves from having to rebuild
  release notes all the time

* Sun Oct 15 2006 Jesse Keating <jkeating@redhat.com> - 6.89-1
- Rebuild for rawhide

* Thu Oct 12 2006 Jesse Keating <jkeating@redhat.com> - 6-3
- version has to stay the same, safe to use.

* Thu Oct  5 2006 Jesse Keating <jkeating@redhat.com> - 6-2
- replace old mirror files with new mirrorlist cgi system

* Thu Oct  5 2006 Jesse Keating <jkeating@redhat.com> - 6-1
- Rebuild for Fedora Core 6 release

* Tue Sep  5 2006 Jesse Keating <jkeating@redhat.com> - 5.92-1
- Bump for FC6 Test3

* Thu Jul 27 2006 Jesse Keating <jkeating@redhat.com> - 5.91.1-1
- Convert deprecated gtk calls. (#200242)
- Fix some of the versioning

* Sun Jul 23 2006 Jesse Keating <jkeating@redhat.com> - 5.91-4
- Bump for FC6 Test2
- Remove release-notes content, now standalone package
- Don't replace issue and issue.net if the end user has modified it
- Require fedora-release-notes
- Cleanups

* Mon Jun 19 2006 Jesse Keating <jkeating@redhat.com> - 5.90-3
- Cleanups

* Thu Jun 15 2006 Jesse Keating <jkeating@redhat.com> - 5.90-1
- Update for 5.90

* Wed May 24 2006 Jesse Keating <jkeating@redhat.com> - 5.89-rawhide.2
- Update to get new devel repo file
- merge minor changes from external cvs .spec file

* Wed Apr 19 2006 Jesse Keating <jkeating@redhat.com> - 5.89-rawhide.1
- Look, a changelog!
- Removed duplicate html/css content from doc dir.
- Add lynx as a buildreq

