# $Revision: 1.2.2.1 $ $Date: 2003-07-11 12:00:49 $
Summary:	File manager using the two-pane design and Gtk+
Summary(pl):	Mened¿er plików oparty na bibliotece GTK+
Name:		emelfm
Version:	0.9.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://emelfm.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-plugin_path.patch
URL:		http://emelfm.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
emelFM is a file manager that implements the popular two-pane design.
It features a simple GTK+ interface, a flexible filetyping scheme, and
a built-in command line for executing commands without opening an
xterm.

%description -l pl
emelFM jest klasycznym, dwupanelowym mened¿erem plików. Ma prosty
interfejs graficzny oparty o bibliotekê GTK+.

%prep
%setup  -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}}

# %{__make} install DESTDIR=$RPM_BUILD_ROOT

install emelfm $RPM_BUILD_ROOT%{_bindir}
install plugins/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}

gzip -9nf README ChangeLog docs/help.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
