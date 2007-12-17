%define name		vmoconv
%define version		1.0
%define release		%mkrel 1

Name:			%{name}
Version:		%{version}
Release:		%{release}
License:		GPL
Source0:		http://triq.net/obexftp/%name-%version.tar.bz2
Group:			Sound
URL:			http://triq.net/obex/downloads.html
Summary:		VMO/VMI to GSM/WAV audio converter

%description
VMOconv converts Siemens phones VMO and VMI audio files to gsm and wav.

After years of suspecting those files to be plain GSM with just a little
disguise Dmitry Zakharov (http://users.i.com.ua/~dmitry_z/) discovered the
layout and notified me.

This package includes two simple convertes to get from VMO to GSM and vice
versa. Additionally there is a patched GSM audio library contained that
converts to WAV.

It's well tested with Siemens (S/ME45 and SL45) and should work on all
Siemens VMO audio files.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README* THANKS
%{_bindir}/*

