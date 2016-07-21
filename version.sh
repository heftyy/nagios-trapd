#!/bin/bash
DESC=($(git describe --tags | sed "s/v//"))
VERSION=($(echo ${DESC[0]} | tr "." " "))
COMMIT=${DESC[1]}
VERSION_MAJ=${VERSION[0]}
VERSION_MIN=${VERSION[1]}
VERSION_REV=${COMMIT}
if [ -z "${VERSION_REV}" ]; then
    VERSION_REV="0"
fi
while getopts "mnr" opt; do
    case $opt in
        m)
            # Major Version 
            echo "${VERSION_MAJ}"
            exit 0
            ;;
        n)
            # Minor Version
            echo "${VERSION_MIN}"
            exit 0
            ;;
        r)
            # Revision Version 
            echo "${VERSION_REV}"
            exit 0
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

VERSION="${VERSION_MAJ}.${VERSION_MIN}.${VERSION_REV}"

echo $VERSION
