#!/bin/bash

for a in worldclim mid lgm; do
  mkdir -p "$a"
  for b in $(find . -type f -name "*.$a"); do
    mv "$b" "$a/${b%.$a}.asc"
  done
done

exit 0
