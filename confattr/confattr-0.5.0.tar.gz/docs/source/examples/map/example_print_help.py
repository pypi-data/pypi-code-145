#!../../../../venv/bin/python3
import typing
if typing.TYPE_CHECKING:
	from .example import Map
	from confattr import ConfigFile
else:
	from example import Map, ConfigFile

# ------- start -------
print(Map.get_help())
