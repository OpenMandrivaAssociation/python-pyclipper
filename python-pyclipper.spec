Name:           python-pyclipper
Version:        1.3.0.post3
Release:        1
Summary:        Cython wrapper for the Clipper library for clipping lines and polygons
License:        MIT
URL:            https://github.com/fonttools/pyclipper
Source:         https://files.pythonhosted.org/packages/source/p/pyclipper/pyclipper-%{version}.tar.gz
BuildRequires:  python3dist(cython)
BuildRequires:  pkgconfig(python)
#BuildRequires:  python3dist(setuptools_scm_git_archive}
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(setuptools)
BuildRequires:  unzip

%description
Pyclipper is a Cython wrapper exposing public functions and classes of
the C++ translation of the `Angus Johnson's Clipper library`, a library
for clipping and offsetting lines and polygons.

The Clipper library performs line & polygon clipping - intersection,
union, difference & exclusive-or, and line & polygon offsetting. The
library is based on Vatti's clipping algorithm.

%prep
%setup -q -n pyclipper-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE
%{python_sitearch}/pyclipper
%{python_sitearch}/pyclipper-%{version}*-info
