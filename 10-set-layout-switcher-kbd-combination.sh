#!/bin/sh

LANG_LINE="ru ua bg in ara gur mkd dev kz(kazrus) kz am ge by"

if [ -f /etc/sysconfig/keyboard ]; then
  . /etc/sysconfig/keyboard

  /sbin/pidof gdm-binary > /dev/null 2>&1

  if [ $? -eq 0 ]; then
    GDM_CURRENT_LANG=$(setxkbmap -print | grep "xkb_symbols" | awk -F+ '{ print $2 }')

    if [ "$GDM_CURRENT_LANG" == "us" ]; then
      echo $LAYOUT | grep "$GDM_CURRENT_LANG" > /dev/null 2>&1
      if [ $? -eq 0 ]; then
        if [ -z $OPTIONS ]; then
          setxkbmap -layout $LAYOUT
        else
          setxkbmap -layout $LAYOUT -option $OPTIONS
        fi
      else
        if [ -z $OPTIONS ]; then
          setxkbmap -layout $GDM_CURRENT_LANG
        else
          setxkbmap -layout $GDM_CURRENT_LANG -option $OPTIONS
        fi
      fi
    else
      echo $LANG_LINE | grep "$GDM_CURRENT_LANG" > /dev/null 2>&1

      if [ $? -eq 0 ]; then
        if [ -z $OPTIONS ]; then
          OPTIONS="grp:alt_shift_toggle,grp_led:scroll"
        fi

        setxkbmap -layout us,$GDM_CURRENT_LANG -option $OPTIONS
      else
        if [ -z $OPTIONS ]; then
          setxkbmap -layout $GDM_CURRENT_LANG
        else
          setxkbmap -layout $GDM_CURRENT_LANG -option $OPTIONS
        fi
      fi
    fi
  else
    if [ -z $OPTIONS ]; then
      setxkbmap -layout $LAYOUT
    else
      setxkbmap -layout $LAYOUT -option $OPTIONS
    fi
  fi
fi
