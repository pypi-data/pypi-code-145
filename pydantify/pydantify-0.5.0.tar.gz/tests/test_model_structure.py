import ast
import logging
import os
import sys
from pathlib import Path
from typing import List
from unittest.mock import patch

import pytest
from pydantic import validate_arguments
from pytest import param
from typing_extensions import Self

LOGGER = logging.getLogger(__name__)


class ParsedAST:
    def __init__(self, file: Path) -> None:
        self.file: Path = file
        with file.open() as f:
            self.ast = ast.parse(f.read())
        self.body: list[ast.stmt] = self.ast.body
        self.classes: dict[str, ast.ClassDef] = dict()
        for c in self.body:
            if isinstance(c, ast.ClassDef):
                bases = ", ".join([b.id for b in c.bases])
                self.classes[f"{c.name}({bases})"] = c

    @validate_arguments
    @staticmethod
    def assert_python_sources_equal(generated: Path, expected: Path):
        LOGGER.info(f"Output path: {generated}")
        ast1 = ParsedAST(generated)
        ast2 = ParsedAST(expected)
        LOGGER.info(
            f'"Comparing:\n{"Expected":9}: {ast2.classes.keys()}\n{"Got":9}: {ast1.classes.keys()}'
        )
        for a, b in zip(ast1.classes.keys(), ast2.classes.keys()):
            assert (
                a == b
            ), f'Missmatch {a} vs {b}\nGot: "{ast1.classes}"\nExpected: "{ast2.classes}"'
        for a, b in zip(ast1.classes.values(), ast2.classes.values()):
            # Compare classes
            assert len(a.body) == len(b.body)
            for a2, b2 in zip(a.body, b.body):
                # Compare class members
                annotation_a: ast.Name = getattr(a2, "annotation", None)
                annotation_b: ast.Name = getattr(b2, "annotation", None)
                # Compare annotation
                assert (annotation_a is None) == (annotation_b is None)
                if annotation_a is not None:
                    # Compare annotated type
                    assert getattr(annotation_a, "id", None) == getattr(
                        annotation_b, "id", None
                    )
        assert len(ast1.body) == len(ast2.body)


def run_pydantify(input_file: Path, output_folder: Path, args: List[str] = []):
    args = [
        sys.argv[0],
        *args,
        f"-i={input_file.parent}",
        f"-o={output_folder}",
        str(input_file),
    ]
    with patch.object(sys, "argv", args):
        from pydantify.main import main

        try:
            main()
        except SystemExit as e:
            assert e.code == 0, f"Pyang exited with errors:\n{e}"


@pytest.fixture(autouse=True)
def reset_optparse():
    from pyang import plugin
    from pydantify.models.base import Node

    # Reset plugins. Otherwise pyang creates cross-test side-effects. TODO: Better way?
    plugin.plugins = []
    Node._name_count = dict()


@pytest.mark.parametrize(
    ("input_dir", "expected_file", "args"),
    [
        param(
            "examples/minimal/interfaces.yang",
            "examples/minimal/expected.py",
            [],
            id="minimal",
        ),
        param(
            "examples/minimal/interfaces.yang",
            "examples/minimal/expected_trimmed.py",
            ["-t=/interfaces/interfaces/address"],
            id="minimal_trimmed",
        ),
        param(
            "examples/minimal/interfaces.yang",
            "examples/minimal/expected_standalone.py",
            ["--standalone"],
            id="minimal_standalone",
        ),
        param(
            "examples/minimal/interfaces.yang",
            "examples/minimal/expected_trimmed.py",
            ["-t=interfaces/interfaces/address"],
            id="minimal_trimmed without leading /",
        ),
        param(
            "examples/with_typedef/interfaces.yang",
            "examples/with_typedef/expected.py",
            [],
            id="typedef",
        ),
        param(
            "examples/with_leafref/interfaces.yang",
            "examples/with_leafref/expected.py",
            [],
            id="leafref",
        ),
        param(
            "examples/with_restrictions/interfaces.yang",
            "examples/with_restrictions/expected.py",
            [],
            id="restrictions",
        ),
        param(
            "examples/with_uses/interfaces.yang",
            "examples/with_uses/expected.py",
            [],
            id="uses",
        ),
        param(
            "examples/with_case/interfaces.yang",
            "examples/with_case/expected.py",
            [],
            id="case",
        ),
        param(
            "examples/with_complex_case/interfaces.yang",
            "examples/with_complex_case/expected.py",
            [],
            id="complex case",
        ),
        param(
            "examples/turing-machine/turing-machine.yang",
            "examples/turing-machine/expected.py",
            [],
            id="turing machine",
        ),
        param(
            "examples/openconfig/openconfig-interfaces.yang",
            "examples/openconfig/expected.py",
            [
                "-t=openconfig-interfaces/interfaces/interface/config",
                "-i=examples/cisco",
            ],
            id="openconfig",
        ),
    ],
)
def test_model(input_dir: str, expected_file: str, args: List[str], tmp_path: Path):
    input_folder = Path(__package__) / input_dir
    expected = Path(__package__) / expected_file
    run_pydantify(
        input_file=input_folder,
        output_folder=tmp_path,
        args=args,
    )
    print("Temp file: " + str(tmp_path / "out.py"))
    ParsedAST.assert_python_sources_equal(tmp_path / "out.py", expected)
