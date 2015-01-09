Summary:	Free Educational Software based on the KDE technologies
Name:		libkeduvocdocument
Version:	14.12.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5I18n)


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
%{_kde_libdir}/libKEduVocDocument.so.%{keduvocdocument_major}*

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
%{_kde_includedir}/libkeduvocdocument
%{_kde_libdir}/libKEduVocDocument.so
%{_kde_libdir}/%{name}

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

