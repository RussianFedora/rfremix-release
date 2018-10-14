%define release_name Twenty Nine
%define dist_version 29
# validate at 20101017. only increase rfremix_version
%define rfremix_version 29
%define bug_version 29

# The package can only be built by a very small number of people
# if you are not sure you can build it do not attempt to

Summary:        RFRemix release files
Name:           rfremix-release
Version:        29
Release:        0.17
Epoch:          2
License:        MIT
Group:          System Environment/Base
URL:            http://fedoraproject.org

Source1:        LICENSE
Source2:        Fedora-Legal-README.txt
Source4:        convert-to-edition.lua

Source10:       85-display-manager.preset
Source11:       90-default.preset
Source12:       90-default-user.preset
Source13:       99-default-disable.preset
Source14:       80-server.preset
Source15:       80-workstation.preset
Source16:       org.gnome.shell.gschema.override
Source17:       org.projectatomic.rpmostree1.rules
Source18:       80-iot.preset

Obsoletes:      redhat-release
Obsoletes:      convert-to-edition < 29-0.15
Provides:       redhat-release
Provides:       fedora-release = %{epoch}:%{version}-%{release}
Provides:       system-release
Provides:       system-release(%{version})

Requires:       fedora-repos(%{version})
BuildArch:      noarch

%description
RFRemix release files such as various /etc/ files that define the release.

%package atomichost
Summary:        Base package for RFremix Atomic-specific default configurations
Provides:       system-release-atomichost
Provides:       system-release-atomichost(%{version})
Provides:       system-release-product
Provides:       fedora-release-atomichost = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}

%description atomichost
Provides a base package for RFRemix Atomic Host-specific configuration files to
depend on.

%package cinnamon
Summary:        Base package for RFRemix Cinnamon-specific default configurations
Provides:       system-release-cinnamon
Provides:       system-release-cinnamon(%{version})
Provides:       fedora-release-cinnamon = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}
Obsoletes:      fedora-release-cinnamon

%description cinnamon
Provides a base package for RFRemix Cinnamon-specific configuration files to
depend on as well as Cinnamon system defaults.

%package cloud
Summary:        Base package for RFRemix Cloud-specific default configurations
Provides:       system-release-cloud
Provides:       system-release-cloud(%{version})
Provides:       system-release-product
Provides:       fedora-release-cloud = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}

%description cloud
Provides a base package for RFRemix Cloud-specific configuration files to
depend on.

%package container
Summary:        Base package for RFRemix container specific default configurations
Provides:       system-release-container
Provides:       system-release-container(%{version})
Provides:       fedora-release-container = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}

%description container
Provides a base package for RFRemix container specific configuration files to
depend on as well as container system defaults.

%package coreos
Summary:        Base package for RFRemix CoreOS-specific default configurations
Provides:       system-release-coreos
Provides:       system-release-coreos(%{version})
Provides:       system-release-product
Provides:       fedora-release-coreos = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}

%description coreos
Provides a base package for RFRemix CoreOS Host-specific configuration files to
depend.

%package iot
Summary:        Base package for RFRemix IoT specific default configurations
Provides:       system-release-iot
Provides:       system-release-iot(%{version})
Provides:       system-release-product
Provides:       fedora-release-iot = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}

%description iot
Provides a base package for RFRemix IoT specific configuration files to
depend on as well as IoT system defaults.

%package kde
Summary:        Base package for RFRemix KDE Plasma-specific default configurations
Provides:       system-release-kde
Provides:       system-release-kde(%{version})
Provides:       fedora-release-kde = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}

%description kde
Provides a base package for RFRemix KDE Plasma-specific configuration files to
depend on as well as KDE Plasma system defaults.

%package matecompiz
Summary:        Base package for RFRemix MATE-Compiz-specific default configurations
Provides:       system-release-matecompiz
Provides:       system-release-matecompiz(%{version})
Provides:       fedora-release-matecompiz = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}

%description matecompiz
Provides a base package for RFRemix MATE-compiz-specific configuration files to
depend on as well as MATE-Compiz system defaults.

%package server
Summary:        Base package for RFRemix Server-specific default configurations
Provides:       system-release-server
Provides:       system-release-server(%{version})
Provides:       system-release-product
Provides:       fedora-release-server = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}
Requires:       systemd
Requires:       cockpit-bridge
Requires:       cockpit-networkmanager
Requires:       cockpit-shell
Requires:       cockpit-storaged
Requires:       cockpit-ws
Requires:       openssh-server

Requires(post):	systemd

%description server
Provides a base package for RFRemix Server-specific configuration files to
depend on.

%package silverblue
Summary:        Base package for RFRemix Silverblue-specific default configurations
Provides:       system-release-silverblue
Provides:       system-release-silverblue(%{version})
Provides:       fedora-release-silverblue = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}

%description silverblue
Provides a base package for RFRemix Silverblue-specific configuration files to
depend on as well as Silverblue system defaults.

%package soas
Summary:        Base package for RFRemix Sugar on a Stick-specific default configurations
Provides:       system-release-soas
Provides:       system-release-soas(%{version})
Provides:       fedora-release-soas = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}

%description soas
Provides a base package for RFRemix Sugar on a Stick-specific configuration files to
depend on as well as SoaS system defaults.

%package workstation
Summary:        Base package for RFRemix Workstation-specific default configurations
Provides:       system-release-workstation
Provides:       system-release-workstation(%{version})
Provides:       system-release-product
Provides:       fedora-release-workstation = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}
# needed for captive portal support
Requires:       NetworkManager-config-connectivity-fedora
Requires(post): /usr/bin/glib-compile-schemas
Requires(postun): /usr/bin/glib-compile-schemas

%description workstation
Provides a base package for RFRemix Workstation-specific configuration files to
depend on.

%package xfce
Summary:        Base package for RFRemix Xfce specific default configurations
Provides:       system-release-xfce
Provides:       system-release-xfce(%{version})
Provides:       fedora-release-xfce = %{epoch}:%{version}-%{release}
Requires:       rfremix-release = %{epoch}:%{version}-%{release}

%description xfce
Provides a base package for RFRemix Xfce specific configuration files to
depend on as well as Xfce system defaults.

%package -n convert-to-edition
Summary: Script for converting between Fedora Editions
Requires: fedora-release = %{version}-%{release}

%description -n convert-to-edition
Provides a script to convert the running system between Fedora Editions

%prep
sed -i 's|@@VERSION@@|%{dist_version}|g' %{SOURCE2}

%build

%install
install -d %{buildroot}/etc
echo "Fedora release %{version} (%{release_name})" > %{buildroot}/etc/fedora-release
echo "RFRemix release %{rfremix_version} (%{release_name})" > %{buildroot}/etc/rfremix-release
echo "cpe:/o:fedoraproject:fedora:%{version}" > %{buildroot}/etc/system-release-cpe

# Symlink the -release files
ln -s fedora-release %{buildroot}/etc/redhat-release
ln -s fedora-release %{buildroot}/etc/system-release

# Create the common os-release file
install -d %{buildroot}/usr/lib/os.release.d/
cat << EOF >>%{buildroot}/usr/lib/os.release.d/os-release-fedora
NAME=RFRemix
VERSION="%{rfremix_version} (%{release_name})"
ID=fedora
ID_LIKE=fedora
PRETTY_NAME="RFRemix %{rfremix_version} (%{release_name})"
VERSION_ID=%{dist_version}
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:fedoraproject:fedora:%{dist_version}"
HOME_URL="https://fedoraproject.org/"
SUPPORT_URL="https://fedoraproject.org/wiki/Communicating_and_getting_help"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=%{bug_version}
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=%{bug_version}
PRIVACY_POLICY_URL="https://fedoraproject.org/wiki/Legal:PrivacyPolicy"
EOF

# Create the common /etc/issue
echo "\S" > %{buildroot}/usr/lib/issue
echo "Kernel \r on an \m (\l)" >> %{buildroot}/usr/lib/issue
echo >> %{buildroot}/usr/lib/issue
ln -s ../usr/lib/issue %{buildroot}/etc/issue

# Create /etc/issue.net
echo "\S" > %{buildroot}/usr/lib/issue.net
echo "Kernel \r on an \m (\l)" >> %{buildroot}/usr/lib/issue.net
ln -s ../usr/lib/issue.net %{buildroot}/etc/issue.net

# Create os-release files for the different editions

# Atomic Host - https://bugzilla.redhat.com/show_bug.cgi?id=1200122
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-atomichost
echo "VARIANT=\"Atomic Host\"" >> %{buildroot}/usr/lib/os.release.d/os-release-atomichost
echo "VARIANT_ID=atomic.host" >> %{buildroot}/usr/lib/os.release.d/os-release-atomichost
sed -i -e "s|(%{release_name})|(Atomic Host)|g" %{buildroot}/usr/lib/os.release.d/os-release-atomichost

# Cinnamon
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-cinnamon
echo "VARIANT=\"Cinnamon\"" >> %{buildroot}/usr/lib/os.release.d/os-release-cinnamon
echo "VARIANT_ID=cinnamon" >> %{buildroot}/usr/lib/os.release.d/os-release-cinnamon
sed -i -e "s|(%{release_name})|(Cinnamon)|g" %{buildroot}/usr/lib/os.release.d/os-release-cinnamon

# Cloud
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-cloud
echo "VARIANT=\"Cloud Edition\"" >> %{buildroot}/usr/lib/os.release.d/os-release-cloud
echo "VARIANT_ID=cloud" >> %{buildroot}/usr/lib/os.release.d/os-release-cloud
sed -i -e "s|(%{release_name})|(Cloud Edition)|g" %{buildroot}/usr/lib/os.release.d/os-release-cloud

# Container
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-container
echo "VARIANT=\"Container Image\"" >> %{buildroot}/usr/lib/os.release.d/os-release-container
echo "VARIANT_ID=container" >> %{buildroot}/usr/lib/os.release.d/os-release-container
sed -i -e "s|(%{release_name})|(Container Image)|g" %{buildroot}/usr/lib/os.release.d/os-release-container

# CoreOS
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-coreos
echo "VARIANT=\"CoreOS\"" >> %{buildroot}/usr/lib/os.release.d/os-release-coreos
echo "VARIANT_ID=coreos" >> %{buildroot}/usr/lib/os.release.d/os-release-coreos
sed -i -e "s|(%{release_name})|(CoreOS)|g" %{buildroot}/usr/lib/os.release.d/os-release-coreos

# IoT
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-iot
echo "VARIANT=\"IoT Edition\"" >> %{buildroot}/usr/lib/os.release.d/os-release-iot
echo "VARIANT_ID=iot" >> %{buildroot}/usr/lib/os.release.d/os-release-iot
sed -i -e "s|(%{release_name})|(IoT Edition)|g" %{buildroot}/usr/lib/os.release.d/os-release-iot

# KDE Plasma
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-kde
echo "VARIANT=\"KDE Plasma\"" >> %{buildroot}/usr/lib/os.release.d/os-release-kde
echo "VARIANT_ID=kde" >> %{buildroot}/usr/lib/os.release.d/os-release-kde
sed -i -e "s|(%{release_name})|(KDE Plasma)|g" %{buildroot}/usr/lib/os.release.d/os-release-kde

# MATE-Compiz
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-matecompiz
echo "VARIANT=\"MATE-Compiz\"" >> %{buildroot}/usr/lib/os.release.d/os-release-matecompiz
echo "VARIANT_ID=matecompiz" >> %{buildroot}/usr/lib/os.release.d/os-release-matecompiz
sed -i -e "s|(%{release_name})|(MATE-Compiz)|g" %{buildroot}/usr/lib/os.release.d/os-release-matecompiz

# Server
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-server
echo "VARIANT=\"Server Edition\"" >> %{buildroot}/usr/lib/os.release.d/os-release-server
echo "VARIANT_ID=server" >> %{buildroot}/usr/lib/os.release.d/os-release-server
sed -i -e "s|(%{release_name})|(Server Edition)|g" %{buildroot}/usr/lib/os.release.d/os-release-server

# Silverblue
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-silverblue
echo "VARIANT=\"Silverblue\"" >> %{buildroot}/usr/lib/os.release.d/os-release-silverblue
echo "VARIANT_ID=silverblue" >> %{buildroot}/usr/lib/os.release.d/os-release-silverblue
sed -i -e "s|(%{release_name})|(Silverblue)|g" %{buildroot}/usr/lib/os.release.d/os-release-silverblue

# Sugar on a Stick
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-soas
echo "VARIANT=\"Sugar on a Stick\"" >> %{buildroot}/usr/lib/os.release.d/os-release-soas
echo "VARIANT_ID=soas" >> %{buildroot}/usr/lib/os.release.d/os-release-soas
sed -i -e "s|(%{release_name})|(Sugar on a Stick)|g" %{buildroot}/usr/lib/os.release.d/os-release-soas

# Workstation
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-workstation
echo "VARIANT=\"Workstation Edition\"" >> %{buildroot}/usr/lib/os.release.d/os-release-workstation
echo "VARIANT_ID=workstation" >> %{buildroot}/usr/lib/os.release.d/os-release-workstation
sed -i -e "s|(%{release_name})|(Workstation Edition)|g" %{buildroot}/usr/lib/os.release.d/os-release-workstation

# Xfce
cp -p %{buildroot}/usr/lib/os.release.d/os-release-fedora \
      %{buildroot}/usr/lib/os.release.d/os-release-xfce
echo "VARIANT=\"Xfce\"" >> %{buildroot}/usr/lib/os.release.d/os-release-xfce
echo "VARIANT_ID=xfce" >> %{buildroot}/usr/lib/os.release.d/os-release-xfce
sed -i -e "s|(%{release_name})|(Xfce)|g" %{buildroot}/usr/lib/os.release.d/os-release-xfce

# Create the symlink for /etc/os-release
# We don't create the /usr/lib/os-release symlink until %%post
# so that we can ensure that the right one is referenced.
ln -s ../usr/lib/os-release %{buildroot}/etc/os-release

# Set up the dist tag macros
install -d -m 755 %{buildroot}%{_rpmconfigdir}/macros.d
cat >> %{buildroot}%{_rpmconfigdir}/macros.d/macros.dist << EOF
# dist macros.

%%fedora                %{dist_version}
%%dist                %{?distprefix}.fc%{dist_version}
%%fc%{dist_version}                1
EOF

# Install licenses
install -d %{buildroot}%{_datadir}/licenses/%{name}/
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
install -pm 0644 %{SOURCE2} %{buildroot}%{_datadir}/licenses/%{name}/Fedora-Legal-README.txt

# Default system wide
install -Dm0644 %{SOURCE10} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE11} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -Dm0644 %{SOURCE12} -t %{buildroot}/usr/lib/systemd/user-preset/
install -Dm0644 %{SOURCE13} -t %{buildroot}%{_prefix}/lib/systemd/system-preset/

# RFRemix Server
install -Dm0644 %{SOURCE14} -t %{buildroot}%{_prefix}/lib/os.release.d/presets/

# RFRemix IoT
install -Dm0644 %{SOURCE18} -t %{buildroot}%{_prefix}/lib/os.release.d/presets/

# RFRemix Workstation
install -Dm0644 %{SOURCE15} -t %{buildroot}%{_prefix}/lib/os.release.d/presets/

# Override the list of enabled gnome-shell extensions for Workstation
install -Dm0644 %{SOURCE16} -t %{buildroot}%{_datadir}/glib-2.0/schemas/
install -Dm0644 %{SOURCE17} -t %{buildroot}%{_datadir}/polkit-1/rules.d/

%post -p <lua>
%include %{SOURCE4}
-- On initial installation, we'll at least temporarily put the non-product
-- symlinks in place. It will be overridden by fedora-release-$EDITION
-- %%post sections because we don't write the /usr/lib/variant file until
-- %%posttrans to avoid trumping the fedora-release-$EDITION packages.
-- This is necessary to avoid breaking systemctl scripts since they rely on
-- /usr/lib/os-release being valid. We can't wait until %%posttrans to default
-- to os-release-fedora.
if arg[2] == "0" then
    set_release(fedora)
end

-- We also want to forcibly set these paths on upgrade if we are explicitly
-- set to "nonproduct"
if read_variant() == "nonproduct" then
    convert_to_edition("nonproduct", false)
end

%posttrans -p <lua>
%include %{SOURCE4}
-- If we get to %%posttrans and nothing created /usr/lib/variant, set it to
-- nonproduct.
install_edition("nonproduct")

%post atomichost -p <lua>
%include %{SOURCE4}
install_edition("atomichost")

%preun atomichost -p <lua>
%include %{SOURCE4}
uninstall_edition("atomichost")

%post cinnamon -p <lua>
%include %{SOURCE4}
install_edition("cinnamon")

%preun cinnamon -p <lua>
%include %{SOURCE4}
uninstall_edition("cinnamon")

%post cloud -p <lua>
%include %{SOURCE4}
install_edition("cloud")

%preun cloud -p <lua>
%include %{SOURCE4}
uninstall_edition("cloud")

%post container -p <lua>
%include %{SOURCE4}
install_edition("container")

%preun container -p <lua>
%include %{SOURCE4}
uninstall_edition("container")

%post coreos -p <lua>
%include %{SOURCE4}
install_edition("coreos")

%preun coreos -p <lua>
%include %{SOURCE4}
uninstall_edition("coreos")

%post iot -p <lua>
%include %{SOURCE4}
install_edition("iot")

%preun iot -p <lua>
%include %{SOURCE4}
uninstall_edition("iot")

%post kde -p <lua>
%include %{SOURCE4}
install_edition("kde")

%preun kde -p <lua>
%include %{SOURCE4}
uninstall_edition("kde")

%post matecompiz -p <lua>
%include %{SOURCE4}
install_edition("matecompiz")

%preun matecompiz -p <lua>
%include %{SOURCE4}
uninstall_edition("matecompiz")

%post server -p <lua>
%include %{SOURCE4}
install_edition("server")

%preun server -p <lua>
%include %{SOURCE4}
uninstall_edition("server")

%post silverblue -p <lua>
%include %{SOURCE4}
install_edition("silverblue")

%preun silverblue -p <lua>
%include %{SOURCE4}
uninstall_edition("silverblue")

%post soas -p <lua>
%include %{SOURCE4}
install_edition("soas")

%preun soas -p <lua>
%include %{SOURCE4}
uninstall_edition("soas")

%post workstation -p <lua>
%include %{SOURCE4}
install_edition("workstation")

%preun workstation -p <lua>
%include %{SOURCE4}
uninstall_edition("workstation")

%postun workstation
if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans workstation
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%post xfce -p <lua>
%include %{SOURCE4}
install_edition("xfce")

%preun xfce -p <lua>
%include %{SOURCE4}
uninstall_edition("xfce")

%files
%license LICENSE Fedora-Legal-README.txt
%ghost /usr/lib/variant
%dir /usr/lib/os.release.d
%dir /usr/lib/os.release.d/presets
%attr(0644,root,root) /usr/lib/os.release.d/os-release-fedora
%ghost /usr/lib/os-release
/etc/os-release
%config %attr(0644,root,root) /etc/fedora-release
%config %attr(0644,root,root) /etc/rfremix-release
/etc/redhat-release
/etc/system-release
%config %attr(0644,root,root) /etc/system-release-cpe
%attr(0644,root,root) /usr/lib/issue
%config(noreplace) /etc/issue
%attr(0644,root,root) /usr/lib/issue.net
%config(noreplace) /etc/issue.net
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist
%dir /usr/lib/systemd/user-preset/
%{_prefix}/lib/systemd/user-preset/90-default-user.preset
%dir %{_prefix}/lib/systemd/system-preset/
%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset


%files atomichost
%attr(0644,root,root) /usr/lib/os.release.d/os-release-atomichost

%files cinnamon
%attr(0644,root,root) /usr/lib/os.release.d/os-release-cinnamon

%files cloud
%attr(0644,root,root) /usr/lib/os.release.d/os-release-cloud

%files container
%attr(0644,root,root) /usr/lib/os.release.d/os-release-container

%files coreos
%attr(0644,root,root) /usr/lib/os.release.d/os-release-coreos

%files iot
%attr(0644,root,root) /usr/lib/os.release.d/os-release-iot
%ghost %{_prefix}/lib/systemd/system-preset/80-iot.preset
%attr(0644,root,root) /usr/lib/os.release.d/presets/80-iot.preset

%files kde
%attr(0644,root,root) /usr/lib/os.release.d/os-release-kde

%files matecompiz
%attr(0644,root,root) /usr/lib/os.release.d/os-release-matecompiz

%files server
%attr(0644,root,root) /usr/lib/os.release.d/os-release-server
%ghost %{_prefix}/lib/systemd/system-preset/80-server.preset
%attr(0644,root,root) /usr/lib/os.release.d/presets/80-server.preset

%files silverblue
%attr(0644,root,root) /usr/lib/os.release.d/os-release-silverblue

%files soas
%attr(0644,root,root) /usr/lib/os.release.d/os-release-soas

%files workstation
%attr(0644,root,root) /usr/lib/os.release.d/os-release-workstation
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.override
%ghost %{_prefix}/lib/systemd/system-preset/80-workstation.preset
%attr(0644,root,root) /usr/lib/os.release.d/presets/80-workstation.preset
%attr(0644,root,root) /usr/share/polkit-1/rules.d/org.projectatomic.rpmostree1.rules

%files xfce
%attr(0644,root,root) /usr/lib/os.release.d/os-release-xfce

%changelog
* Fri Sep 14 2018 Mohan Boddu <mboddu@bhujji.com> 29-0.17.R
- Enable the stratis daemon for managing stratis storage

* Fri Sep 14 2018 Mohan Boddu <mboddu@bhujji.com> 29-0.16.R
- Set cpi.service as enabled in the systemd presets
- Set device_cio_free service as enabled

* Mon Aug 27 2018 Stephen Gallagher <sgallagh@redhat.com> - 29-0.15.R
- Drop special issue handling and convert-to-edition script

* Mon Aug 27 2018 Mohan Boddu <mboddu@bhujji.com> 29-0.14.R
- Adding Container sub package
- Adding CoreOS sub package
- Adding Desktop Spin sub packages

* Thu Aug 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 29-0.13.R
- Add Fedora IoT edition components

* Mon Aug 20 2018 Arkady L. Shane <ashejn@russianfedora.pro> - 29-0.12.R
- branch RFRemix 29
