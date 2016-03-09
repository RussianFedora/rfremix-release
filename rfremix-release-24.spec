%define release_name Rawhide
%define dist_version 24
# validate at 20101017. only increase rfremix_version
%define rfremix_version 24
%define bug_version 24

Summary:        RFRemix release files
Name:           rfremix-release
Version:        24
Release:        0.14.R
Epoch:	        2
License:        MIT
Group:          System Environment/Base
URL:            http://fedoraproject.org
Source:         %{name}-%{version}.tar.bz2
Source1:	convert-to-edition.lua
Obsoletes:      redhat-release
Provides:       redhat-release
Obsoletes:      fedora-release
Provides:       fedora-release = %{epoch}:%{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})

# Kill off the fedora-release-nonproduct package
Provides:       fedora-release-nonproduct = %{epoch}:%{version}
Provides:       rfremix-release-nonproduct = %{epoch}:%{version}
Obsoletes:      fedora-release-nonproduct <= 23-0.3
Obsoletes:      rfremix-release-nonproduct <= 23-0.3
Provides:       fedora-release-standard = 22-0.8
Provides:       rfremix-release-standard = 22-0.8
Obsoletes:      fedora-release-standard < 22-0.8
Obsoletes:      rfremix-release-standard < 22-0.8


Requires:       fedora-repos(%{version})
BuildArch:      noarch

%description
RFRemix release files such as various /etc/ files that define the release.

%package atomichost
Summary:        Base package for Fedora Atomic-specific default configurations
Provides:       system-release-atomichost
Provides:       system-release-atomichost(%{version})
Provides:       system-release-product
Requires:       rfremix-release = %{epoch}:%{version}-%{release}
Obsoletes:      fedora-release-atomichost

%description atomichost
Provides a base package for Fedora Atomic Host-specific configuration files to
depend on.

%package cloud
Summary:        Base package for RFRemix Cloud-specific default configurations
Provides:       system-release-cloud
Provides:       system-release-cloud(%{version})
Provides:       system-release-product
Requires:       rfremix-release = %{epoch}:%{version}-%{release}
Obsoletes:	fedora-release-cloud

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
Requires:       cockpit-bridge
Requires:       cockpit-networkmanager
Requires:       cockpit-shell
Requires:       cockpit-storaged
Requires:       cockpit-ws
Requires:       openssh-server
Requires:       rolekit
Requires(post):	sed
Requires(post):	systemd

%description server
Provides a base package for RFRemix Server-specific configuration files to
depend on.

%package workstation
Summary:        Base package for RFRemix Workstation-specific default configurations
Provides:       system-release-workstation
Provides:       system-release-workstation(%{version})
Provides:       system-release-product
Requires:       rfremix-release = %{epoch}:%{version}-%{release}
Obsoletes:	fedora-release-workstation
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
install -d $RPM_BUILD_ROOT/etc
echo "Fedora release %{version} (%{release_name})" > $RPM_BUILD_ROOT/etc/fedora-release
echo "RFRemix release %{rfremix_version} (%{release_name})" > $RPM_BUILD_ROOT/etc/rfremix-release
echo "cpe:/o:fedoraproject:fedora:%{version}" > $RPM_BUILD_ROOT/etc/system-release-cpe

# Symlink the -release files
ln -s fedora-release $RPM_BUILD_ROOT/etc/redhat-release
ln -s fedora-release $RPM_BUILD_ROOT/etc/system-release

# Create the common os-release file
install -d $RPM_BUILD_ROOT/usr/lib/os.release.d/
cat << EOF >>$RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-fedora
NAME=Fedora
VERSION="%{dist_version} (%{release_name})"
ID=fedora
ID_LIKE=fedora
VERSION="%{rfremix_version} (%{release_name})"
PETTY_NAME="RFRemix %{rfremix_version} (%{release_name})"
VERSION_ID=%{dist_version}
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:fedoraproject:fedora:%{dist_version}"
HOME_URL="https://fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=%{bug_version}
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=%{bug_version}
PRIVACY_POLICY_URL=https://fedoraproject.org/wiki/Legal:PrivacyPolicy
EOF

# Create the common /etc/issue
echo "\S" > $RPM_BUILD_ROOT/usr/lib/os.release.d/issue-fedora
echo "Kernel \r on an \m (\l)" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/issue-fedora
echo >> $RPM_BUILD_ROOT/usr/lib/os.release.d/issue-fedora

# Create /etc/issue.net
echo "\S" > $RPM_BUILD_ROOT/usr/lib/issue.net
echo "Kernel \r on an \m (\l)" >> $RPM_BUILD_ROOT/usr/lib/issue.net
ln -s ../usr/lib/issue.net $RPM_BUILD_ROOT/etc/issue.net

# Create os-release and issue files for the different editions

# Atomic Host - https://bugzilla.redhat.com/show_bug.cgi?id=1200122
cp -p $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-fedora \
      $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-atomichost
echo "VARIANT=\"Atomic Host\"" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-atomichost
echo "VARIANT_ID=atomic.host" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-atomichost
sed -i -e "s|(%{release_name})|(Atomic Host)|g" $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-atomichost

# Cloud
cp -p $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-fedora \
      $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-cloud
echo "VARIANT=\"Cloud Edition\"" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-cloud
echo "VARIANT_ID=cloud" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-cloud
sed -i -e "s|(%{release_name})|(Cloud Edition)|g" $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-cloud

# Server
cp -p $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-fedora \
      $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-server
echo "VARIANT=\"Server Edition\"" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-server
echo "VARIANT_ID=server" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-server
sed -i -e "s|(%{release_name})|(Server Edition)|g" $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-server

cp -p $RPM_BUILD_ROOT/usr/lib/os.release.d/issue-fedora \
      $RPM_BUILD_ROOT/usr/lib/os.release.d/issue-server
echo "Admin Console: https://\4:9090/ or https://[\6]:9090/" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/issue-server
echo >> $RPM_BUILD_ROOT/usr/lib/os.release.d/issue-server

# Workstation
cp -p $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-fedora \
      $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-workstation
echo "VARIANT=\"Workstation Edition\"" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-workstation
echo "VARIANT_ID=workstation" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-workstation
sed -i -e "s|(%{release_name})|(Workstation Edition)|g" $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-workstation

# Create the symlink for /etc/os-release
# We don't create the /usr/lib/os-release symlink until %%post
# so that we can ensure that the right one is referenced.
ln -s ../usr/lib/os-release $RPM_BUILD_ROOT/etc/os-release

# Create the symlink for /etc/issue
# We don't create the /usr/lib/os-release symlink until %%post
# so that we can ensure that the right one is referenced.
ln -s ../usr/lib/issue $RPM_BUILD_ROOT/etc/issue

# Set up the dist tag macros
install -d -m 755 $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d
cat >> $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d/macros.dist << EOF
# dist macros.

%%fedora                %{dist_version}
%%dist                .fc%{dist_version}.R
%%fc%{dist_version}                1
EOF

# Add presets
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/user-preset/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/
mkdir -p $RPM_BUILD_ROOT/usr/lib/os.release.d/presets

# Default system wide
install -m 0644 85-display-manager.preset $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/
install -m 0644 90-default.preset $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/
install -m 0644 99-default-disable.preset $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/
# RFRemix Server
install -m 0644 80-server.preset $RPM_BUILD_ROOT%{_prefix}/lib/os.release.d/presets/
# RFRemix Workstation
install -m 0644 80-workstation.preset $RPM_BUILD_ROOT%{_prefix}/lib/os.release.d/presets/

# Override the list of enabled gnome-shell extensions for Workstation
mkdir -p $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/
install -m 0644 org.gnome.shell.gschema.override $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/

# Copy the make_edition script to /usr/sbin
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/sbin/
install -m 0744 convert-to-edition $RPM_BUILD_ROOT/%{_prefix}/sbin/

%post -p <lua>
%include %{_sourcedir}/convert-to-edition.lua
-- On initial installation, we'll at least temporarily put the non-product
-- symlinks in place. It will be overridden by fedora-release-$EDITION
-- %%post sections because we don't write the /usr/lib/variant file until
-- %%posttrans to avoid trumping the fedora-release-$EDITION packages.
-- This is necessary to avoid breaking systemctl scripts since they rely on
-- /usr/lib/os-release being valid. We can't wait until %%posttrans to default
-- to os-release-fedora.
if arg[2] == "0" then
    set_release(fedora)
    set_issue(fedora)
end

-- We also want to forcibly set these paths on upgrade if we are explicitly
-- set to "nonproduct"
if read_variant() == "nonproduct" then
    convert_to_edition("nonproduct", false)
end

%posttrans -p <lua>
%include %{_sourcedir}/convert-to-edition.lua
-- If we get to %%posttrans and nothing created /usr/lib/variant, set it to
-- nonproduct.
if posix.stat(VARIANT_FILE) == nil then
    convert_to_edition("nonproduct", true)
end

%post atomichost -p <lua>
%include %{_sourcedir}/convert-to-edition.lua
install_edition("atomichost")

%preun atomichost -p <lua>
%include %{_sourcedir}/convert-to-edition.lua
uninstall_edition("atomichost")

%post cloud -p <lua>
%include %{_sourcedir}/convert-to-edition.lua
install_edition("cloud")

%preun cloud -p <lua>
%include %{_sourcedir}/convert-to-edition.lua
uninstall_edition("cloud")

%post server -p <lua>
%include %{_sourcedir}/convert-to-edition.lua
install_edition("server")

%preun server -p <lua>
%include %{_sourcedir}/convert-to-edition.lua
uninstall_edition("server")

%post workstation -p <lua>
%include %{_sourcedir}/convert-to-edition.lua
install_edition("workstation")

%preun workstation -p <lua>
%include %{_sourcedir}/convert-to-edition.lua
uninstall_edition("workstation")

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
%ghost /usr/lib/variant
%dir /usr/lib/os.release.d
%dir /usr/lib/os.release.d/presets
%config %attr(0644,root,root) /usr/lib/os.release.d/os-release-fedora
%ghost /usr/lib/os-release
/etc/os-release
%config %attr(0644,root,root) /etc/fedora-release
%config %attr(0644,root,root) /etc/rfremix-release
/etc/redhat-release
/etc/system-release
%config %attr(0644,root,root) /etc/system-release-cpe
%config %attr(0644,root,root) /usr/lib/os.release.d/issue-fedora
%ghost /usr/lib/issue
%config(noreplace) /etc/issue
%config %attr(0644,root,root) /usr/lib/issue.net
%config(noreplace) /etc/issue.net
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist
%dir /usr/lib/systemd/user-preset/
%dir %{_prefix}/lib/systemd/system-preset/
%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset
/usr/sbin/convert-to-edition

%files atomichost
%{!?_licensedir:%global license %%doc}
%license LICENSE
%config %attr(0644,root,root) /usr/lib/os.release.d/os-release-atomichost


%files cloud
%{!?_licensedir:%global license %%doc}
%license LICENSE
%config %attr(0644,root,root) /usr/lib/os.release.d/os-release-cloud


%files server
%{!?_licensedir:%global license %%doc}
%license LICENSE
%config %attr(0644,root,root) /usr/lib/os.release.d/os-release-server
%config %attr(0644,root,root) /usr/lib/os.release.d/issue-server
%ghost %{_prefix}/lib/systemd/system-preset/80-server.preset
%config %attr(0644,root,root) /usr/lib/os.release.d/presets/80-server.preset

%files workstation
%{!?_licensedir:%global license %%doc}
%license LICENSE
%config %attr(0644,root,root) /usr/lib/os.release.d/os-release-workstation
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.override
%ghost %{_prefix}/lib/systemd/system-preset/80-workstation.preset
%config %attr(0644,root,root) /usr/lib/os.release.d/presets/80-workstation.preset

%changelog
* Tue Mar 08 2016 Stephen Gallagher <sgallagh@redhat.com> - 24-0.14.R
- Add a subpackage for Atomic Host to provide /usr/lib/os-release differences

* Thu Mar 03 2016 Stephen Gallagher <sgallagh@redhat.com> - 24-0.13.R
- Rewrite scriptlets in Lua to avoid a circular dependency on coreutils
- Be more specific with fedora-release-server's Cockpit requirement
  (Do not pull in all of the optional Cockpit components as mandatory)

* Mon Feb 29 2016 Stephen Gallagher <sgallagh@redhat.com> - 24-0.12.R
- Only run grub2-mkconfig for platforms that support it
- Remove erroneous RPM_BUILD_ROOT variables in convert-to-edition

* Mon Feb 29 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 24-0.11.R
- Fix typo that breaks %post on upgrades of Workstation and Cloud

* Tue Feb 23 2016 Dennis Gilmore <dennis@ausil.us> - 24-0.10.R
- setup for f24 being branched

* Thu Jan 21 2016 Stephen Gallagher <sgallagh@redhat.com> 24-0.9.R
- Install Edition presets only for the configured Edition
- Add script to convert from non-edition to an Edition
- Fix upgrade bugs with non-edition installs
- Explicitly set issue-fedora for cloud installs
- Resolves: rhbz#1288205

* Tue Dec 15 2015 Stephen Gallagher <sgallagh@redhat.com> 24-0.8.R
- Fix copy-paste error for Workstation os-release and issue

* Tue Sep 29 2015 Stephen Gallagher <sgallagh@redhat.com> 24-0.7.R
- Rework os-release and issue mechanism to avoid upgrade issues such as
  competing fedora-release-$EDITION packages
- Make a non-product install persistent (it won't be converted to an Edition
  install if something pulls in a fedora-release-$EDITION package

* Mon Sep 28 2015 Dennis Gilmore <dennis@ausil.us> - 24-0.6.R
- set bug_version to be rawhide rhbz#1259287

* Tue Sep 15 2015 Stephen Gallagher <sgallagh@redhat.com> - 24-0.5.R
- Do not clobber /etc/issue[.net] customizations

* Wed Sep 09 2015 Stephen Gallagher <sgallagh@redhat.com> - 24-0.4.R
- Update preset file with FESCo decisions
- https://fedorahosted.org/fesco/ticket/1472

* Wed Sep 09 2015 Stephen Gallagher <sgallagh@redhat.com> - 24-0.3.R
- Enclose IPv6 addresses in square brackets in /etc/issue

* Mon Aug 24 2015 Stephen Gallagher <sgallagh@redhat.com> - 24-0.2.R
- Make /etc/issue configurable per-edition
- Resolves: RHBZ#1239089

* Mon Jul 20 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 24-0.1.R
- initial build for RFRemix 24

* Tue Jul 14 2015 Dennis Gilmore <dennis@ausil.us> - 24-0.1
- setup for rawhide being f24
