#!/usr/bin/make -f
#
# This file is part of the Radio RaBe motd collection
#
# Copyright (c) 2017 Radio Bern RaBe
#                    http://www.rabe.ch
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 

PN        = rabe-motd-ansi

PREFIX   ?= /usr/local
BINDIR    = $(PREFIX)/bin
LIBDIR    = $(PREFIX)/lib
ETCDIR   ?= $(PREFIX)/etc
SHAREDIR  = $(PREFIX)/share
DOCDIR    = $(PREFIX)/share/doc/$(PN)
MAN1DIR   = $(PREFIX)/share/man/man1
UNITDIR   = $(LIBDIR)/systemd/system

all:

test:

clean:

install-bin:

install-man:

install-doc:

install-share:
	@echo installing ansi files...
	install -Dm755 -d $(SHAREDIR)/$(PN)
	install -Dm755 ansi/* $(SHAREDIR)/$(PN)/
	@echo done.

install: all install-bin install-man install-doc install-share
