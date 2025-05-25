# This is largely based on https://src.fedoraproject.org/rpms/pyproject-rpm-macros/
Name: tt-topology
BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros

%generate_buildrequires
%pyproject_buildrequires
%build
%pyproject_wheel
%install
%pyproject_install