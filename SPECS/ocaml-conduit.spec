%global debug_package %{nil}

Name:           ocaml-conduit
Version:        0.8.2
Release:        2%{?dist}
Summary:        OCaml network conduit library
License:        Unknown 
Group:          Development/Libraries
URL:            https://github.com/mirage/ocaml-conduit
Source0:        https://github.com/mirage/ocaml-conduit/archive/v%{version}/ocaml-conduit-%{version}.tar.gz
Patch0:         ocaml-conduit-acf42817ab5810e040b6481996b8221fa74db1a1.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-async-devel
BuildRequires:  ocaml-stringext-devel
BuildRequires:  ocaml-uri-devel
BuildRequires:  ocaml-cstruct-devel
BuildRequires:  ocaml-ipaddr-devel
BuildRequires:  ocaml-pa-structural-sexp-devel

%description
The conduit library takes care of establishing and listening for TCP and SSL/TLS connections for the Lwt and Async libraries.

The reason this library exists is to provide a degree of abstraction from the precise SSL library used, since there are a variety of ways to bind to a library (e.g. the C FFI, or the Ctypes library), as well as well as which library is used (just OpenSSL for now).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:  ocaml-sexplib-devel
Requires:  ocaml-lwt-devel
Requires:  ocaml-async-devel
Requires:  ocaml-stringext-devel
Requires:  ocaml-uri-devel
Requires:  ocaml-cstruct-devel
Requires:  ocaml-ipaddr-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1

%build
make all

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%{_libdir}/ocaml/conduit
%exclude %{_libdir}/ocaml/conduit/*.a
%exclude %{_libdir}/ocaml/conduit/*.cmxa
%exclude %{_libdir}/ocaml/conduit/*.cmx
%exclude %{_libdir}/ocaml/conduit/*.cmt
%exclude %{_libdir}/ocaml/conduit/*.cmti


%files devel
%{_libdir}/ocaml/conduit/*.a
%{_libdir}/ocaml/conduit/*.cmx
%{_libdir}/ocaml/conduit/*.cmxa

%changelog
* Wed Jul 27 2016 Euan Harris <euan.harris@citrix.com> - 0.8.2-2
- Remove *.cmt, *.cmti and *.annot

* Fri Apr 24 2015 David Scott <dave.scott@citrix.com> - 0.8.2-1
- Update to 0.8.2
- Backport fix for Unix domain sockets

* Thu Apr  2 2015 David Scott <dave.scott@citrix.com> - 0.7.2-1
- Update to 0.7.2

* Tue Oct 14 2014 David Scott <dave.scott@citrix.com> - 0.5.0-2
- Add dependency on core/async

* Fri May 2 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.5.0-1
- Initial package

