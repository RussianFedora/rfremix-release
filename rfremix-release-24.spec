%define release_name Rawhide
%define dist_version 24
# validate at 20101017. only increase rfremix_version
%define rfremix_version 24
%define bug_version Rawhide

Summary:        RFRemix release files
Name:           rfremix-release
Version:        24
Release:        0.1.1.R
Epoch:		2
License:        MIT
Group:          System Environment/Base
URL:            http://fedoraproject.org
Source:         %{name}-%{version}.tar.bz2
Obsoletes:      redhat-release
Provides:       redhat-release
Obsoletes:      fedora-release
Provides:       fedora-release
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
Requires:       cockpit
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
cp -p $RPM_BUILD_ROOT/etc/rfremix-release $RPM_BUILD_ROOT/etc/issue
echo "Kernel \r on an \m (\l)" >> $RPM_BUILD_ROOT/etc/issue
cp -p $RPM_BUILD_ROOT/etc/issue $RPM_BUILD_ROOT/etc/issue.net
echo >> $RPM_BUILD_ROOT/etc/issue
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

# Create os-release files for the different editions
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

# Workstation
cp -p $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-fedora \
      $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-workstation
echo "VARIANT=\"Workstation Edition\"" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-workstation
echo "VARIANT_ID=workstation" >> $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-workstation
sed -i -e "s|(%{release_name})|(Workstation Edition)|g" $RPM_BUILD_ROOT/usr/lib/os.release.d/os-release-workstation

# Create the symlink for /etc/os-release
# This will be standard until %post when the
# release packages will link the appropriate one into
# /usr/lib/os-release
ln -s ../usr/lib/os-release $RPM_BUILD_ROOT/etc/os-release
ln -s os.release.d/os-release-fedora $RPM_BUILD_ROOT/usr/lib/os-release

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
# Default system wide
install -m 0644 85-display-manager.preset $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/
install -m 0644 90-default.preset $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/
install -m 0644 99-default-disable.preset $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/
# RFRemix Server
install -m 0644 80-server.preset $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/
# RFRemix Workstation
install -m 0644 80-workstation.preset $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/

# Override the list of enabled gnome-shell extensions for Workstation
mkdir -p $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/
install -m 0644 org.gnome.shell.gschema.override $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/

%posttrans
# Only on installation
if [ $1 = 0 ]; then
    # If no fedora-release-$edition subpackage was installed,
    # make sure to link /etc/os-release to the standard version
    test -e /usr/lib/os-release || \
        ln -sf ./os-release.d/os-release-fedora /usr/lib/os-release
fi

%post cloud
# Run every time
    # If there is no link to os-release yet from some other
    # release package, create it
    test -e /usr/lib/os-release || \
        ln -sf ./os.release.d/os-release-cloud /usr/lib/os-release

    # If os-release isn't a link or it exists but it points to a
    # non-productized version, replace it with this one
    if [ \! -h /usr/lib/os-release -o "x$(readlink /usr/lib/os-release)" = "xos.release.d/os-release-fedora" ]; then
        ln -sf ./os.release.d/os-release-cloud /usr/lib/os-release || :
    fi

%postun cloud
# Uninstall
if [ $1 = 0 ]; then
    # If os-release is now a broken symlink or missing replace it
    # with a symlink to basic version
    test -e /usr/lib/os-release || \
        ln -sf ./os.release.d/os-release-fedora /usr/lib/os-release || :
fi


%post server
# Run every time
    # If there is no link to os-release yet from some other
    # release package, create it
    test -e /usr/lib/os-release || \
        ln -sf ./os.release.d/os-release-server /usr/lib/os-release

    # If os-release isn't a link or it exists but it points to a
    # non-productized version, replace it with this one
    if [ \! -h /usr/lib/os-release -o "x$(readlink /usr/lib/os-release)" = "xos.release.d/os-release-fedora" ]; then
        ln -sf ./os.release.d/os-release-server /usr/lib/os-release || :
    fi

if [ $1 -eq 1 ] ; then
    # Initial installation

    # fix up after %%systemd_post in packages
    # possibly installed before our preset file was added
    units=$(sed -n 's/^enable//p' \
        < %{_prefix}/lib/systemd/system-preset/80-server.preset)
        /usr/bin/systemctl preset $units >/dev/null 2>&1 || :
fi

%postun server
# Uninstall
if [ $1 = 0 ]; then
    # If os-release is now a broken symlink or missing replace it
    # with a symlink to basic version
    test -e /usr/lib/os-release || \
        ln -sf ./os.release.d/os-release-fedora /usr/lib/os-release || :
fi

%post workstation
# Run every time
    # If there is no link to os-release yet from some other
    # release package, create it
    test -e /usr/lib/os-release || \
        ln -sf ./os.release.d/os-release-workstation /usr/lib/os-release

    # If os-release isn't a link or it exists but it points to a
    # non-productized version, replace it with this one
    if [ \! -h /usr/lib/os-release -o "x$(readlink /usr/lib/os-release)" = "xos.release.d/os-release-fedora" ]; then
        ln -sf ./os.release.d/os-release-workstation /usr/lib/os-release || :
    fi

if [ $1 -eq 1 ] ; then
    # Initial installation

    # fix up after %%systemd_post in packages
    # possibly installed before our preset file was added
    units=$(sed -n 's/^disable//p' \
        < %{_prefix}/lib/systemd/system-preset/80-workstation.preset)
    /usr/bin/systemctl preset $units >/dev/null 2>&1 || :
fi

%postun workstation
if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

    # If os-release is now a broken symlink or missing replace it
    # with a symlink to basic version
    test -e /usr/lib/os-release || \
        ln -sf ./os.release.d/os-release-fedora /usr/lib/os-release || :
fi

%posttrans workstation
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license LICENSE Fedora-Legal-README.txt
%dir /usr/lib/os.release.d
%config %attr(0644,root,root) /usr/lib/os.release.d/os-release-fedora
/usr/lib/os-release
/etc/os-release
%config %attr(0644,root,root) /etc/fedora-release
%config %attr(0644,root,root) /etc/rfremix-release
/etc/redhat-release
/etc/system-release
%config %attr(0644,root,root) /etc/system-release-cpe
%config(noreplace) %attr(0644,root,root) /etc/issue
%config(noreplace) %attr(0644,root,root) /etc/issue.net
%attr(0644,root,root) %{_rpmconfigdir}/macros.d/macros.dist
%dir /usr/lib/systemd/user-preset/
%dir %{_prefix}/lib/systemd/system-preset/
%{_prefix}/lib/systemd/system-preset/85-display-manager.preset
%{_prefix}/lib/systemd/system-preset/90-default.preset
%{_prefix}/lib/systemd/system-preset/99-default-disable.preset

%files cloud
%{!?_licensedir:%global license %%doc}
%license LICENSE
%config %attr(0644,root,root) /usr/lib/os.release.d/os-release-cloud


%files server
%{!?_licensedir:%global license %%doc}
%license LICENSE
%config %attr(0644,root,root) /usr/lib/os.release.d/os-release-server
%{_prefix}/lib/systemd/system-preset/80-server.preset

%files workstation
%{!?_licensedir:%global license %%doc}
%license LICENSE
%config %attr(0644,root,root) /usr/lib/os.release.d/os-release-workstation
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.override
%{_prefix}/lib/systemd/system-preset/80-workstation.preset

%changelog
* Mon Jul 20 2015 Arkady L. Shane <ashejn@russianfedora.pro> - 24-0.1.R
- initial build for RFRemix 24

* Tue Jul 14 2015 Dennis Gilmore <dennis@ausil.us> - 24-0.1
- setup for rawhide being f24
