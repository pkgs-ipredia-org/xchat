# Makefile for source rpm: xchat
# $Id$
NAME := xchat
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
