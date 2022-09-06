Name:           python-pyclipper
Version:        1.3.0.post2
Release:        0
Summary:        Cython wrapper for the Clipper library for clipping lines and polygons
License:        MIT
URL:            https://github.com/fonttools/pyclipper
Source:         https://files.pythonhosted.org/packages/source/p/pyclipper/pyclipper-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm_git_archive}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
%python_subpackages

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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pyclipper
%{python_sitearch}/pyclipper-%{version}*-info
