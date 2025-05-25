Name:           python-tt-topology
Version:        1.2.8
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        ...

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            ...
Source:         tt-topology-1.2.8.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tt-topology' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-tt-topology
Summary:        %{summary}

%description -n python3-tt-topology %_description


%prep
%autosetup -p1 -n tt-topology-%{version}
%{__python3} -m pip install .

%generate_buildrequires
%pyproject_buildrequires -R


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files tt_topology


%check
%pyproject_check_import


%files -n python3-tt-topology -f %{pyproject_files}


%changelog
%autochangelog