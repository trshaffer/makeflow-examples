#!/bin/bash

for a in worldclim mid lgm; do
  mkdir -p "$a"
  for b in $(find . -type f -name "*.$a"); do
    T=$(mktemp -p "$a")
    cp "$b" "$T"
    mv "$T" "$a/${b%.$a}.asc"
  done
done

exit 0
