#!/usr/bin/env python3

import os
import shutil
import subprocess
import re

HTML = 'docs/build/html'
ARTIFACT = 'public'
LATEST = 'latest'


def get_tags() -> 'list[str]':
	return subprocess.run(['git', 'tag', '--sort=version:refname'], capture_output=True, text=True).stdout.rstrip().splitlines()

def is_tracked_by_git(path: str) -> bool:
	cmd = ['git', 'ls-files', '--error-unmatch', path]
	p = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
	return p.returncode == 0

def export_html(tag: str) -> bool:
	subprocess.run(['git', 'checkout', tag])
	if os.path.isdir(HTML) and is_tracked_by_git(HTML):
		shutil.copytree(HTML, os.path.join(ARTIFACT, tag))
		return True
	else:
		print('no HTML documentation found in %s' % tag)
		return False

def create_latest(last_tag: str) -> None:
	src = os.path.join(ARTIFACT, last_tag)
	dst = os.path.join(ARTIFACT, LATEST)
	shutil.copytree(src, dst)

def inject_links_to_other_versions(versions: 'list[str]', this_version: str) -> None:
	SECTION_NAME = 'Versions'
	INSERT_AFTER = '</section>'
	PATTERN_BEGIN = '''\
<section id="{section}">
<h1>{Section}<a class="headerlink" href="#{section}" title="Permalink to this heading">¶</a></h1>

This project uses <a class="reference external" href="https://semver.org/">semantic versioning</a>.
The differences between the different versions are documented in the <a class="reference external" href="{bugtracker}">tag descriptions</a>.

<div class="toctree-wrapper compound">
<ul>\
'''
	PATTERN_BODY = '<li class="toctree-l1">{version}</li>'
	PATTERN_END = '''\
</ul>
</div>
</section>\
'''
	PATTERN_OTHER_VERSION = '<a class="reference internal" href="{target}">{version}</a>'
	PATTERN_THIS_VERSION = '{version}'
	PATTERN_LATEST = '{version} / {latest}'

	fn = os.path.join(ARTIFACT, this_version, 'index.html')
	with open(fn, 'rt') as f:
		html = f.read()

	html_begin, html_end = html.rsplit(INSERT_AFTER, 1)

	out = [
		html_begin,
		PATTERN_BEGIN.format(Section=SECTION_NAME, section=SECTION_NAME.lower(), bugtracker=get_bug_tracker()),
	]

	for v in reversed(versions):
		p = PATTERN_THIS_VERSION if v == this_version else PATTERN_OTHER_VERSION
		target = '../%s/index.html' % v
		item = p.format(version=v, target=target)

		if v == versions[-1]:
			v = LATEST
			p = PATTERN_THIS_VERSION if v == this_version else PATTERN_OTHER_VERSION
			target = '../%s/index.html' % v
			item = PATTERN_LATEST.format(version=item, latest=p.format(version=v, target=target))

		out.append(PATTERN_BODY.format(version=item))

	out.append(PATTERN_END)
	out.append(html_end)

	with open(fn, 'wt') as f:
		for block in out:
			f.write(block)
			f.write('\n')

def get_bug_tracker() -> str:
	# I cannot use tomllib yet because it requires python 3.11
	# and using non-standard libraries is not worth the effort
	reo_group = re.compile(r'\[(?P<name>[^]]+)\]')
	reo_setting = re.compile(r'''["']?(?P<key>[^'"=]+)["']?\s*=\s*["']?(?P<val>[^'"]+)["']?''')
	in_urls_section = False

	with open('pyproject.toml', 'rt') as f:
		for ln in f.readlines():
			m = reo_group.match(ln)
			if m:
				in_urls_section = m.group('name') == 'project.urls'
				continue

			m = reo_setting.match(ln)
			if m and m.group('key').strip().lower().startswith('bug'):
				return m.group('val')

	raise ValueError('Failed to find bug tracker url in pyproject.toml')


def main() -> None:
	os.mkdir(ARTIFACT)
	html_versions = []
	for tag in get_tags():
		if export_html(tag):
			html_versions.append(tag)
	create_latest(html_versions[-1])

	for tag in html_versions:
		inject_links_to_other_versions(html_versions, tag)
	inject_links_to_other_versions(html_versions, LATEST)


if __name__ == '__main__':
	main()
