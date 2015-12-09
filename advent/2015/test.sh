#!/bin/bash

interpreter_for() {
  case "$1" in
    *.ijs) echo "j8 -c %s" ;;
    *.py)  echo "python %s" ;;
    *.c)   echo "make -q && ./solution # %s" ;;
    *.o)   ;; # ignore
    *)     echo >&2 "error: bad filename $1"; exit 1 ;;
  esac
}

for i in {01..25}; do
  [ ! -d $i ] && break
  pushd $i >/dev/null
  for f in solution.*; do
    interp_fmt=$(interpreter_for $f)
    [ ${#interp_fmt} == 0 ] && continue
    command=$(printf "$interp_fmt" "$f")
    echo "$i $f $(sh -c "$command"' <input | xargs')"
  done
  popd >/dev/null
done

