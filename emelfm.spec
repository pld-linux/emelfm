Summary:	File manager using the two-pane design and Gtk+
Summary(pl):	Zarz±dca plików oparty na bibliotece GTK+
Name:		emelfm
Version:	0.9.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://emelfm.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	7a1c8bd369d94be5bca409439d74da14
Source1:	%{name}.desktop
Patch0:		%{name}-plugin_path.patch
URL:		http://emelfm.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
emelFM is a file manager that implements the popular two-pane design.
It features a simple GTK+ interface, a flexible filetyping scheme, and
a built-in command line for executing commands without opening an
xterm.

%description -l pl
emelFM jest klasycznym, dwupanelowym zarz±dc± plików. Ma prosty
interfejs graficzny oparty o bibliotekê GTK+.

%prep
%setup  -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_desktopdir}}

# %{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

install emelfm $RPM_BUILD_ROOT%{_bindir}
install plugins/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog docs
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
