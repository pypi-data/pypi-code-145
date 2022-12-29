#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

from slpkg.checks import Check
from slpkg.upgrade import Upgrade
from slpkg.configs import Configs
from slpkg.tracking import Tracking
from slpkg.queries import SBoQueries
from slpkg.dependees import Dependees
from slpkg.utilities import Utilities
from slpkg.search import SearchPackage
from slpkg.views.cli_menu import Usage
from slpkg.dialog_box import DialogBox
from slpkg.views.version import Version
from slpkg.download_only import Download
from slpkg.slackbuild import Slackbuilds
from slpkg.form_configs import FormConfigs
from slpkg.check_updates import CheckUpdates
from slpkg.find_installed import FindInstalled
from slpkg.views.view_package import ViewPackage
from slpkg.remove_packages import RemovePackages
from slpkg.clean_logs import CleanLogsDependencies
from slpkg.update_repository import UpdateRepository


class Argparse:

    def __init__(self, args: list):
        self.args = args
        self.flags = []
        self.configs = Configs
        self.dialog = DialogBox()
        self.utils = Utilities()
        self.usage = Usage()
        self.check = Check()
        self.form_configs = FormConfigs()

        if len(self.args) == 0:
            self.usage.help_short()

        self.check.blacklist(self.args)

        self.flag_yes = '--yes'
        self.flag_jobs = '--jobs'
        self.flag_resolve_off = '--resolve-off'
        self.flag_reinstall = '--reinstall'
        self.flag_skip_installed = '--skip-installed'
        self.flag_full_reverse = '--full-reverse'
        self.flag_search = '--search'

        if (not self.configs.dialog and self.flag_search in self.args or
                not self.configs.dialog and 'configs' in self.args):
            print("Error: You should enable the dialog "
                  "in the '/etc/slpkg/' folder.\n")
            self.usage.help(1)

        self.options = [self.flag_yes,
                        self.flag_jobs,
                        self.flag_resolve_off,
                        self.flag_reinstall,
                        self.flag_skip_installed,
                        self.flag_full_reverse,
                        self.flag_search]

        # Check for correct flag
        for opt in self.args:
            if opt.startswith('--'):
                if opt not in self.options and opt not in ['--help', '--version']:
                    raise SystemExit(f"\nError: flag '{opt}' does not exist.\n")

        # Remove flags from args
        for opt in self.options:
            if opt in self.args:
                self.args.remove(opt)
                self.flags.append(opt)

    def choose_packages(self, packages, method):
        """ Choose packages with dialog utility and --search flag. """
        height = 10
        width = 70
        list_height = 0
        choices = []
        title = f' Choose packages you want to {method} '
        repo_packages = SBoQueries('').sbos()

        # Grab all the installed packages
        installed = os.listdir(self.configs.log_packages)

        if method in ['remove', 'find']:

            for package in installed:
                name = self.utils.split_installed_pkg(package)[0]
                version = self.utils.split_installed_pkg(package)[1]

                if package.endswith(self.configs.sbo_repo_tag):
                    for pkg in packages:
                        if pkg in name:
                            choices += [(name, version, False)]
        else:
            for package in repo_packages:
                for pkg in packages:

                    if pkg in package:
                        repo_ver = SBoQueries(package).version()

                        if method == 'upgrade':
                            pkg = self.utils.is_installed(package)
                            inst_ver = self.utils.split_installed_pkg(pkg)[1]
                            choices += [(package, f'{inst_ver} -> {repo_ver}', True)]
                        else:
                            choices += [(package, repo_ver, False)]

        if not choices:
            return packages

        text = f'There are {len(choices)} packages:'

        code, tags = self.dialog.checklist(text, title, height, width,
                                           list_height, choices, packages)

        if not code:
            return packages

        os.system('clear')

        if not tags:
            raise SystemExit()

        return tags

    def help(self):
        if len(self.args) == 1 and not self.flags:
            self.usage.help(0)
        self.usage.help(1)

    def version(self):
        if len(self.args) == 1 and not self.flags:
            version = Version()
            version.view()
            raise SystemExit()
        self.usage.help(1)

    def update(self):
        if [f for f in self.flags if f not in [self.flag_yes]]:
            self.usage.help(1)

        if len(self.args) == 1:
            update = UpdateRepository(self.flags)
            update.sbo()
            raise SystemExit()
        self.usage.help(1)

    def upgrade(self):
        if [f for f in self.flags if f not in [self.flag_yes,
                                               self.flag_jobs,
                                               self.flag_resolve_off,
                                               self.flag_reinstall]]:
            self.usage.help(1)

        if len(self.args) == 1:
            self.check.database()

            upgrade = Upgrade()
            packages = list(upgrade.packages())

            packages = self.choose_packages(packages,
                                            Argparse.upgrade.__name__)

            if not packages:
                print('\nEverything is up-to-date.\n')
                raise SystemExit()

            install = Slackbuilds(packages, self.flags, install=True)
            install.execute()
            raise SystemExit()
        self.usage.help(1)

    def check_updates(self):
        if len(self.args) == 1 and not self.flags:
            self.check.database()

            check = CheckUpdates()
            check.updates()
            raise SystemExit()
        self.usage.help(1)

    def edit_configs(self):
        if len(self.args) == 1 and not self.flags:
            self.form_configs.edit()
            raise SystemExit()
        self.usage.help(1)

    def clean_logs(self):
        if [f for f in self.flags if f not in [self.flag_yes]]:
            self.usage.help(1)

        if len(self.args) == 1:
            self.check.database()

            logs = CleanLogsDependencies(self.flags)
            logs.clean()
            raise SystemExit()
        self.usage.help(1)

    def clean_tmp(self):
        if len(self.args) == 1 and not self.flags:
            path = self.configs.tmp_path
            tmp_slpkg = self.configs.tmp_slpkg
            folder = self.configs.prog_name

            self.utils.remove_folder_if_exists(path, folder)
            self.utils.create_folder(tmp_slpkg, 'build')
            raise SystemExit()
        self.usage.help(1)

    def build(self):
        if [f for f in self.flags if f not in [self.flag_yes,
                                               self.flag_jobs,
                                               self.flag_resolve_off,
                                               self.flag_search]]:
            self.usage.help(1)

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if '--search' in self.flags:
                packages = self.choose_packages(packages,
                                                Argparse.build.__name__)

            self.check.database()
            self.check.exists(packages)
            self.check.unsupported(packages)

            build = Slackbuilds(packages, self.flags, install=False)
            build.execute()
            raise SystemExit()
        self.usage.help(1)

    def install(self):
        if [f for f in self.flags if f not in [self.flag_yes,
                                               self.flag_jobs,
                                               self.flag_resolve_off,
                                               self.flag_reinstall,
                                               self.flag_skip_installed,
                                               self.flag_search]]:
            self.usage.help(1)

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if '--search' in self.flags:
                packages = self.choose_packages(packages,
                                                Argparse.install.__name__)

            self.check.database()
            self.check.exists(packages)
            self.check.unsupported(packages)

            install = Slackbuilds(packages, self.flags, install=True)
            install.execute()
            raise SystemExit()
        self.usage.help(1)

    def download(self):
        if [f for f in self.flags if f not in [self.flag_yes,
                                               self.flag_search]]:
            self.usage.help(1)

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if '--search' in self.flags:
                packages = self.choose_packages(packages,
                                                Argparse.download.__name__)

            self.check.database()
            self.check.exists(packages)
            download = Download(self.flags)
            download.packages(packages)
            raise SystemExit()
        self.usage.help(1)

    def remove(self):
        if [f for f in self.flags if f not in [self.flag_yes,
                                               self.flag_resolve_off,
                                               self.flag_search]]:
            self.usage.help(1)

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if '--search' in self.flags:
                packages = self.choose_packages(packages,
                                                Argparse.remove.__name__)

            self.check.database()
            packages = self.check.installed(packages)

            remove = RemovePackages(packages, self.flags)
            remove.remove()
            raise SystemExit()
        self.usage.help(1)

    def find(self):
        if [f for f in self.flags if f not in [self.flag_search]]:
            self.usage.help(1)

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if '--search' in self.flags:
                packages = self.choose_packages(packages,
                                                Argparse.find.__name__)

            self.check.database()

            find = FindInstalled()
            find.find(packages)
            raise SystemExit()
        self.usage.help(1)

    def view(self):
        if [f for f in self.flags if f not in [self.flag_search]]:
            self.usage.help(1)

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if '--search' in self.flags:
                packages = self.choose_packages(packages,
                                                Argparse.view.__name__)

            self.check.database()
            self.check.exists(packages)

            view = ViewPackage()
            view.package(packages)
            raise SystemExit()
        self.usage.help(1)

    def search(self):
        if [f for f in self.flags if f not in [self.flag_search]]:
            self.usage.help(1)

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if '--search' in self.flags:
                packages = self.choose_packages(packages,
                                                Argparse.search.__name__)

            self.check.database()

            search = SearchPackage()
            search.package(packages)
            raise SystemExit()
        self.usage.help(1)

    def dependees(self):
        if [f for f in self.flags if f not in [self.flag_full_reverse,
                                               self.flag_search]]:
            self.usage.help(1)

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if '--search' in self.flags:
                packages = self.choose_packages(packages,
                                                Argparse.dependees.__name__)

            self.check.database()
            self.check.exists(packages)

            dependees = Dependees(packages, self.flags)
            dependees.slackbuilds()
            raise SystemExit()
        self.usage.help(1)

    def tracking(self):
        if [f for f in self.flags if f not in [self.flag_search]]:
            self.usage.help(1)

        if len(self.args) >= 2:
            packages = list(set(self.args[1:]))

            if '--search' in self.flags:
                packages = self.choose_packages(packages,
                                                Argparse.tracking.__name__)

            self.check.database()
            self.check.exists(packages)

            tracking = Tracking()
            tracking.packages(packages)
            raise SystemExit()
        self.usage.help(1)


def main():
    args = sys.argv
    args.pop(0)

    argparse = Argparse(args)

    arguments = {
        '-h': argparse.help,
        '--help': argparse.help,
        '-v': argparse.version,
        '--version': argparse.version,
        'update': argparse.update,
        'upgrade': argparse.upgrade,
        'check-updates': argparse.check_updates,
        'configs': argparse.edit_configs,
        'clean-logs': argparse.clean_logs,
        'clean-tmp': argparse.clean_tmp,
        'build': argparse.build,
        '-b': argparse.build,
        'install': argparse.install,
        '-i': argparse.install,
        'download': argparse.download,
        '-d': argparse.download,
        'remove': argparse.remove,
        '-r': argparse.remove,
        'view': argparse.view,
        '-w': argparse.view,
        'find': argparse.find,
        '-f': argparse.find,
        'search': argparse.search,
        '-s': argparse.search,
        'dependees': argparse.dependees,
        '-e': argparse.dependees,
        'tracking': argparse.tracking,
        '-t': argparse.tracking
    }

    try:
        arguments[args[0]]()
    except KeyError:
        Usage().help(1)


if __name__ == '__main__':
    main()
