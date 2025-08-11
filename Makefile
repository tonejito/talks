#!/usr/bin/make -f
#	= ^ . ^ =

SHELL=/bin/bash

HOST?=localhost
PORT?=8001
PANDOC_CFG=pandoc.cfg
CONTENT_DIR=content
PUBLIC_DIR=public
PANDOC_FLAGS=--defaults ${PANDOC_CFG}

DIRS=$(shell find ${CONTENT_DIR} -mindepth 1 -maxdepth 1 -type d \( ! -name '.*' \) -print | awk -F / '{print $$(NF)}')

default:	index build patch list

all:	default serve

check:
	pre-commit run --all-files

index:
	test -d "${PUBLIC_DIR}" || mkdir -vp "${PUBLIC_DIR}"
	pandoc ${PANDOC_FLAGS} -o ${PUBLIC_DIR}/index.html ${CONTENT_DIR}/index.md

build:
	touch ${PUBLIC_DIR}/favicon.ico
	for DIR in $(DIRS) ; \
	do \
	  echo $${DIR} ; \
	  test -d ${PUBLIC_DIR}/$${DIR} || mkdir -vp ${PUBLIC_DIR}/$${DIR} ; \
	  $(MAKE) -f ../Makefile.content -C ${CONTENT_DIR}/$${DIR} ; \
	done ;

patch:
	find ${PUBLIC_DIR} -iname '*.html' -exec sed -i'' -e 's|4//|4/|g' {} +

list:
	# find ${PUBLIC_DIR} -mindepth 1 -maxdepth 2 -type f \( ! -name '.*' \) -print
	find ${PUBLIC_DIR} -mindepth 1 -maxdepth 2 -type f ! \( -name '*.png' -o -name '*.svg' -o -name '.DS_Store' -o -name '.gitkeep' \) -print

watch:
	python3 watch.py

serve:
	python3 -m http.server \
	  --bind ${HOST} ${PORT} \
	  --directory "${PUBLIC_DIR}" \
	;
