#!/bin/bash
# build-rpms.sh: This script is a runnable version of the rpm builder github action.
# It is only tested on Fedora 42.
PACKAGE_NAME="tt-topology"
VERSION="1.2.8"
PACKAGE_VERSIONED_NAME="$PACKAGE_NAME-$VERSION"
SPEC_FILE="packaging/python-tt-topology.spec"

# Run from repository root, assuming that the script is in REPO_ROOT/packaging.
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)
cd $SCRIPT_DIR/..

sudo dnf install --assumeyes dnf-plugins-core rpm-build rpmdevtools
mkdir -pv rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
spectool --all --get-files --sourcedir "$SPEC_FILE"
mkdir $PACKAGE_VERSIONED_NAME

# Copy relevant source/files to $PACKAGE_VERSIONED_NAME.
cp pyproject.toml $PACKAGE_VERSIONED_NAME
cp LICENSE $PACKAGE_VERSIONED_NAME
cp README.md $PACKAGE_VERSIONED_NAME
cp -r tt_topology $PACKAGE_VERSIONED_NAME
# End of copy section.

tar -czf "$PACKAGE_NAME.tar.gz" $PACKAGE_VERSIONED_NAME
rm -rf $PACKAGE_VERSIONED_NAME
mv "$PACKAGE_NAME.tar.gz" "rpmbuild/SOURCES/$PACKAGE_VERSIONED_NAME.tar.gz"
rpmbuild --define "_topdir `pwd`/rpmbuild" -br "$SPEC_FILE"