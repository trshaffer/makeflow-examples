#!/bin/bash

for a in worldclim mid lgm; do
  mkdir -p $a
  cp *.$a $a
  rename .$a .asc $a/*
done

exit 0
