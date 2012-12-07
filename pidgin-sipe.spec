Summary:	Pidgin protocol plugin to connect to MS Office Communicator
Name:		pidgin-sipe
Version:	1.13.3
Release:	1
License:	GPL v2+
Group:		Applications/Networking
URL:		http://sipe.sourceforge.net/
Source0:	http://downloads.sourceforge.net/sipe/%{name}-%{version}.tar.bz2
# Source0-md5:	7d115de9d9029c9eebd0a3647dbf27d5
BuildRequires:	e2fsprogs-devel
BuildRequires:	gettext
BuildRequires:	glib2-devel >= 2.28.0
BuildRequires:	gstreamer-devel
BuildRequires:	heimdal-devel
BuildRequires:	intltool
BuildRequires:	libnice-devel >= 0.1.0
BuildRequires:	libpurple-devel >= 2.8.0
BuildRequires:	libxml2-devel
BuildRequires:	nss-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	libpurple-sipe = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A third-party plugin for the Pidgin multi-protocol instant messenger.
It implements the extended version of SIP/SIMPLE used by various
products:

- Microsoft Lync Server 2010
- Microsoft Office Communications Server (OCS 2007/2007 R2 and newer)
- Microsoft Live Communications Server (LCS 2003/2005)
- Reuters Messaging

With this plugin you should be able to replace your Microsoft Office
Communicator client with Pidgin.

This package provides the icon set for Pidgin.

%package -n libpurple-sipe
Summary:	Libpurple protocol plugin to connect to MS Office Communicator
License:	GPL v2+
Group:		Applications/Networking

%description -n libpurple-sipe
A third-party plugin for the Pidgin multi-protocol instant messenger.
It implements the extended version of SIP/SIMPLE used by various
products:

- Microsoft Lync Server 2010
- Microsoft Office Communications Server (OCS 2007/2007 R2 and newer)
- Microsoft Live Communications Server (LCS 2003/2005)
- Reuters Messaging

This package provides the protocol plugin for libpurple clients.

%prep
%setup -q

%build
%configure \
	--with-krb5 \
	--enable-purple \
	--disable-telepathy
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name "*.la" -delete -print

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n libpurple-sipe -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/purple-2/libsipe.so

%files
%defattr(644,root,root,755)
%doc AUTHORS
%{_pixmapsdir}/pidgin/protocols/*/sipe.*
