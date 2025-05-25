# This is largely based on https://src.fedoraproject.org/rpms/pyproject-rpm-macros/
Name:          tt-topology
Summary:       tt-topology
Version:       1.0
Release:       2025
License:       Apache
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

%description   tt-topology
%generate_buildrequires
%pyproject_buildrequires
%build
%pyproject_wheel
%install
%pyproject_install