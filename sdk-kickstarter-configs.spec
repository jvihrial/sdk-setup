# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       sdk-kickstarter-configs

# >> macros
# << macros

Summary:    Kickstarter configs for Mer SDK
Version:    0.9
Release:    1
Group:      System/Base
License:    Public Domain
BuildArch:  noarch
URL:        https://github.com/lbt/sdk-kickstarter-configs
Source0:    sdk-kickstarter-scripts.tgz
Source100:  sdk-kickstarter-configs.yaml
Requires:   mer-kickstarter-configs
Requires(pre): rpm
Requires(pre): /bin/rm
BuildRequires:  mer-kickstarter-configs
BuildRequires:  mer-kickstarter

%description
Configuration files to build Mer SDK and variants

%package -n sdk-kickstarter-ks
Summary:    Kickstarts for the Mer SDK and variants
Group:      System/Base
Requires:   %{name} = %{version}-%{release}

%description -n sdk-kickstarter-ks
Kickstart files to build Mer SDK and variants

%package -n sdk-chroot
Summary:    Mer SDK files for the chroot variant
Group:      System/Base
Requires:   %{name} = %{version}-%{release}

%description -n sdk-chroot
Contains the mer_sdk_chroot script and supporting configs

%package -n sdk-vm
Summary:    Mer SDK files for the VM variant
Group:      System/Base
Requires:   %{name} = %{version}-%{release}

%description -n sdk-vm
Contains the supporting configs for VMs

%package -n sdk-sb2-config
Summary:    Mer SDK files to configure sb2
Group:      System/Base
Requires:   %{name} = %{version}-%{release}
Requires:   scratchbox2

%description -n sdk-sb2-config
Contains the sdk build and install modes used by scratchbox2 in the SDK


%prep
%setup -q -n src

# >> setup
# << setup

%build
# >> build pre
mkdir kickstarts
mer-kickstarter -c 00sdk.yaml -o kickstarts/
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre

# sdk-kickstarter-configs
mkdir -p %{buildroot}%{_datadir}/kickstarts/
cp -ar kickstarts/* %{buildroot}%{_datadir}/kickstarts/

# sdk-kickstarter-ks
mkdir -p %{buildroot}%{_datadir}/kickstarter-configs/sdk/
cp -ar *.yaml %{buildroot}%{_datadir}/kickstarter-configs/sdk/

# sdk-chroot
mkdir -p %{buildroot}%{_bindir}/
cp sdk-version %{buildroot}%{_bindir}/

cp mer-sdk-chroot %{buildroot}/
cp mer-bash-setup %{buildroot}/

# sdk-vm

# sdk-sb2-config
mkdir -p %{buildroot}/usr/share/scratchbox2/modes/
cp -ar modes/* %{buildroot}/usr/share/scratchbox2/modes/


# << install pre

# >> install post
# << install post


%pre
# >> pre
%pre -n sdk-chroot
if ! rpm --quiet -q ca-certificates && [ -d /etc/ssl/certs ] ; then echo "Cleaning up copied ssl certs. ca-certificates should now install"; rm -rf /etc/ssl/certs ;fi

# << pre

%files
%defattr(-,root,root,-)
%{_datadir}/kickstarter-configs/sdk/*
# >> files
# << files

%files -n sdk-kickstarter-ks
%defattr(-,root,root,-)
%{_datadir}/kickstarts/*
# >> files sdk-kickstarter-ks
# << files sdk-kickstarter-ks

%files -n sdk-chroot
%defattr(-,root,root,-)
/mer-sdk-chroot
/mer-bash-setup
%{_bindir}/sdk-version
# >> files sdk-chroot
# << files sdk-chroot

%files -n sdk-vm
%defattr(-,root,root,-)
%{_bindir}/sdk-version
# >> files sdk-vm
# << files sdk-vm

%files -n sdk-sb2-config
%defattr(-,root,root,-)
%{_datadir}/scratchbox2/modes/*
# >> files sdk-sb2-config
# << files sdk-sb2-config
