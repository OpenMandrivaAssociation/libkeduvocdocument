%define major 5
%define libname %mklibname KEduVocDocument %{major}
%define devname %mklibname KEduVocDocument -d

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Free Educational Software based on the KDE technologies
Name:		libkeduvocdocument
Version:	18.11.80
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
BuildRequires:	cmake(Qt5Xml)
Requires:	%{libname} = %{EVRD}

%description
Runtime library for KDE Education Application.

%files -f %{name}.lang

#---------------------------------------------

%package -n %{libname}
Summary:	Runtime library for KDE Education Application
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Runtime library for KDE Education Application

%files -n %{libname}
%{_libdir}/libKEduVocDocument.so.%{major}*

#--------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Conflicts:	kdeedu4-devel < 4.6.90
Obsoletes:	libkeduvocdocument-devel < 15.12.0

%description  -n %{devname}
Files needed to build applications based on %{name}.

%files  -n %{devname}
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
%find_lang %{name}
