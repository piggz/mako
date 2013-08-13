Name: python-mako
Version: 0.8.1
Release: 1
Summary: Mako template library for Python

Group: Development/Languages
# Mostly MIT, but _ast_util.py is Python licensed.
# The documentation contains javascript for search licensed BSD or GPLv2
License: (MIT and Python) and (BSD or GPLv2)
URL: http://www.makotemplates.org/
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-markupsafe
BuildRequires: python-beaker
Requires: python-markupsafe
Requires: python-beaker

%description
Mako is a template library written in Python. It provides a familiar, non-XML
syntax which compiles into Python modules for maximum performance. Mako's
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded
Python (i.e. Python Server Page) language, which refines the familiar ideas of
componentized layout and inheritance to produce one of the most straightforward
and flexible models available, while also maintaining close ties to Python
calling and scoping semantics.

%prep
%setup -q -n %{name}-%{version}

%build
cd mako
%{__python} setup.py build

%install
cd mako
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

# These are supporting files for building the docs.  No need to ship
rm -rf doc/build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc mako/CHANGES mako/LICENSE mako/README.rst
%{_bindir}/mako-render
%{python_sitelib}/*
