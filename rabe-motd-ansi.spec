# spec file for package rabe-motd-ansi
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

# Please submit enhancements, bugfixes or comments via GitHub:
# https://github.com/radiorabe/motd-ansi
#

%define _repo_name motd-ansi
%define _prog_name rabe-motd-ansi
# the file to auto-install
%define _install_motd_file rabe_motd.txt

Name:          rabe-motd-ansi
Version:       0.0.0
Release:       0
Summary:       RaBe logos in beautiful ANSI format to use as motd
License:       AGPLv3
Source:        %{_repo_name}-%{version}.tar.gz

BuildArch:     noarch

BuildRequires: make

%description
RaBe logos in beautiful ANSI format to use as motd.

%prep
%setup -q -n %{_repo_name}-%{version}

%build
make -j2

%install
make install PREFIX=%{buildroot}%{_prefix} ETCDIR=%{buildroot}%{_sysconfdir}/%{_prog_name}

%post
if [ -f %{_sysconfdir}/motd ]; then # motd exists and will be blessed with the image of the bird
  # prepare install on kickstarted machines
  if grep '^Kickstarted on' %{_sysconfdir}/motd; then
    echo "Moving Kickstart %{_sysconfdir}/motd to %{_sysconfdir}/motd.kickstart.";
    mv %{_sysconfdir}/motd %{_sysconfdir}/motd.kickstart;
  fi
  # prepare install on machines with empty motd (ie. docker containers and others)
  if [ $(wc -c <%{_sysconfdir}/motd) -eq 0 ]; then
    echo "Removing empty %{_sysconfdir}/motd to install %{name}.";
    rm %{_sysconfdir}/motd
  fi
  # only try installing if we succeeded at removing the original file
  if [ ! -f %{_sysconfdir}/motd ]; then
    echo "Installing %{_install_motd_file} from %{name}."
    ln -s %{_datarootdir}/%{name}/%{_install_motd_file} %{_sysconfdir}/motd
  fi
else 
  echo "Could not find %{_sysconfdir}/motd, aborting post-install.";
fi

%postun
if [ "$1" = "0" ]; then # package removal, bye bye
  # clean up since it looks like we installed also
  if [ "$(readlink %{_sysconfdir}/motd)" = "%{_datarootdir}/%{name}/%{_install_motd_file}" ]; then
    rm %{_sysconfdir}/motd
  fi
  # restore from kickstart as possible
  if [ -f %{_sysconfdir}/motd.kickstart ]; then
    echo "Restoring Kickstart %{_sysconfdir}/motd from %{_sysconfdir}/motd.kickstart.";
    mv %{_sysconfdir}/motd.kickstart %{_sysconfdir}/motd;
  fi
  # recreate empty file if noone here, sane systems should have at least an empty one from base
  if [ ! -f %{_sysconfdir}/motd ]; then
    echo "Restoring empty %{_sysconfdir}/motd.";
    touch %{_sysconfdir}/motd;
  fi
fi

%files
%doc LICENSE README.md
%defattr(-,root,root,0544)
%{_datarootdir}/%{name}/*.txt
