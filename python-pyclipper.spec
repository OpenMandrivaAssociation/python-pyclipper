Name:           python-pyclipper
Version:        1.4.0
Release:        2
Summary:        Cython wrapper for the Clipper library for clipping lines and polygons
License:        MIT
Group:        Development/Python
URL:            https://github.com/fonttools/pyclipper
Source:         https://files.pythonhosted.org/packages/source/p/pyclipper/pyclipper-%{version}.tar.gz
BuildRequires:  python%{pyver}dist(cython)
BuildRequires:  pkgconfig(python)
#BuildRequires:  python3dist(setuptools_scm_git_archive}
BuildRequires:  python%{pyver}dist(setuptools-scm)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)
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
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE
%{python_sitearch}/pyclipper
%{python_sitearch}/pyclipper-%{version}*-info
