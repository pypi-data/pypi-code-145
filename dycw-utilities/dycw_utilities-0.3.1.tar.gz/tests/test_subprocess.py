from pathlib import Path
from subprocess import CalledProcessError  # noqa: S404
from subprocess import check_call  # noqa: S404

from pytest import raises

from utilities.subprocess import MultipleActivate
from utilities.subprocess import NoActivate
from utilities.subprocess import get_shell_output
from utilities.subprocess import tabulate_called_process_error
from utilities.text import strip_and_dedent


class TestGetShellOutput:
    def test_main(self) -> None:
        output = get_shell_output("ls")
        assert any(line == "pyproject.toml" for line in output.splitlines())

    def test_activate(self, tmp_path: Path) -> None:
        venv = tmp_path.joinpath(".venv")
        activate = venv.joinpath("activate")
        activate.parent.mkdir(parents=True)
        activate.touch()
        _ = get_shell_output("ls", cwd=venv, activate=venv)

    def test_no_activate(self, tmp_path: Path) -> None:
        venv = tmp_path.joinpath(".venv")
        with raises(NoActivate):
            _ = get_shell_output("ls", cwd=venv, activate=venv)

    def test_multiple_activates(self, tmp_path: Path) -> None:
        venv = tmp_path.joinpath(".venv")
        for i in range(2):
            activate = venv.joinpath(str(i), "activate")
            activate.parent.mkdir(parents=True)
            activate.touch()
        with raises(MultipleActivate):
            _ = get_shell_output("ls", cwd=venv, activate=venv)


class TestTabulateCalledProcessError:
    def test_main(self) -> None:
        def which() -> None:
            _ = check_call(["which"], text=True)  # noqa: S603, S607

        try:
            which()
        except CalledProcessError as error:
            result = tabulate_called_process_error(error)
            expected = """
                cmd        ['which']
                returncode 1
                stdout     None
                stderr     None
            """
            assert result == strip_and_dedent(expected)
        else:
            with raises(CalledProcessError):
                which()
