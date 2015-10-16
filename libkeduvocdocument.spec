%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Summary:	Free Educational Software based on the KDE technologies
Name:		libkeduvocdocument
Version:	15.08.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5I18n)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Test)

%description
Runtime library for KDE Education Application.

#---------------------------------------------

%define keduvocdocument_major 5
%define libkeduvocdocument %mklibname KEduVocDocument %{keduvocdocument_major}

%package -n %{libkeduvocdocument}
Summary:	Runtime library for KDE Education Application
Group:		System/Libraries

%description -n %{libkeduvocdocument}
Runtime library for KDE Education Application

%files -n %{libkeduvocdocument}
%{_libdir}/libKEduVocDocument.so.%{keduvocdocument_major}*

#--------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libkeduvocdocument} = %{version}-%{release}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_includedir}/libkeduvocdocument
%{_libdir}/libKEduVocDocument.so
%{_libdir}/cmake/libkeduvocdocument

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
