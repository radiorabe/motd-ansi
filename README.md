# RaBe ANSI art
RaBe logos in beautiful ANSI format to use as motd. The ANSI files are optimized for a 80 character wide terminal, motd files are either stored in `/etc/motd`or `/etc/update-motd.d`.

Used tool: https://github.com/maandree/util-say

Tutorial: https://tylercipriani.com/blog/2014/05/22/creating-baller-useful-motd-ascii-art/

## Installing

We provide prebuilt rpm packages at the [home:radiorabe:branding OBS subproject](http://build.opensuse.org/project/show/home:radiorabe:branding)
courtesy of the [openSUSE Build Service](https://build.opensuse.org). They install the 
motd files and set up rabe_motd.txt as `/etc/motd` on systems that have an untouched 
motd. If a kickstart motd is detected it is preserved to `/etc/motd.kickstart`. Though
it would be silly to remove the package again, the changes are reversed upon removal.

```bash
curl -o /etc/yum.repos.d/home:radiorabe:branding.repo \
     http://download.opensuse.org/repositories/home:/radiorabe:/branding/CentOS_7/home:radiorabe:branding.repo

yum install -y rabe-motd-ansi
```

## Releasing

New RPMs get built for all tags with a valid version. New releases are created through git.

* Bump the version in rabe-motd-ansi.spec and add a new commit to master with the version bump
* Tag this commit with the same version you used in the specfile
* Push master and the tag to github
* The openSUSE Build Service should get triggered and build a new package automagically

## License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

# Copyright

Copyright (c) 2017 [Radio Bern RaBe](http://rabe.ch)
