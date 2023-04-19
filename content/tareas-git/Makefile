#!/usr/bin/make -f
#	= ^ . ^ =

SHELL=/bin/bash

PANDOC_CFG=../pandoc.cfg
THIS_DIR=$(shell basename $(CURDIR))
CONTENT_DIR=.
PUBLIC_DIR=../../public/${THIS_DIR}
PANDOC_FLAGS=--defaults ${PANDOC_CFG}

default:	build

build:	${INPUT}
	test -d "${PUBLIC_DIR}" || mkdir -vp "${PUBLIC_DIR}"
	pandoc ${PANDOC_FLAGS} -o ${PUBLIC_DIR}/index.html ${CONTENT_DIR}/index.md
