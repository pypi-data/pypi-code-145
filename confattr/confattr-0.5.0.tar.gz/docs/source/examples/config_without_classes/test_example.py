#!../../../../venv/bin/pytest

import os
import sys
import subprocess

def test__output() -> None:
	path = os.path.dirname(__file__)
	fn_script = os.path.join(path, 'example.py')
	fn_expected_output = os.path.join(path, 'output.txt')
	env = {'XDG_CONFIG_HOME' : path}
	p = subprocess.run([sys.executable, fn_script], env=env, stdout=subprocess.PIPE, check=True)

	with open(fn_expected_output, 'rt') as f:
		expected_output = f.read()

	assert p.stdout.decode() == expected_output
