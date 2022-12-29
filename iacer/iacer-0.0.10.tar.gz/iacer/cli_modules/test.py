import logging

from iacer.cli import CliCore
from iacer.cli_modules.delete import Delete
from iacer.cli_modules.list import List
from iacer.config import DEFAULT_CONFIG_FILE
from iacer.testing.ros_stack import StackTest

LOG = logging.getLogger(__name__)


class Test:
    '''
    Performs functional tests on IaC templates.
    '''

    @staticmethod
    @CliCore.longform_param_required('no_delete')
    @CliCore.longform_param_required('project_path')
    @CliCore.longform_param_required('test_names')
    @CliCore.longform_param_required('project_path')
    @CliCore.longform_param_required('keep_failed')
    @CliCore.longform_param_required('dont_wait_for_delete')
    @CliCore.longform_param_required('failed')
    async def run(template: str = None,
                  config_file: str = None,
                  output_directory: str = None,
                  regions: str = None,
                  test_names: str = None,
                  no_delete: bool = False,
                  project_path: str = None,
                  keep_failed: bool = False,
                  dont_wait_for_delete: bool = False,
                  failed: bool = False,
                  generate_parameters: bool = False
                  ) -> None:
        '''
        tests whether IaC templates are able to successfully launch
        :param template: path to a template
        :param config_file: path to a config file
        :param output_directory: path to an output directory
        :param regions: comma separated list of regions to test in
        :param test_names: comma separated list of tests to run
        :param no_delete: don't delete stacks after test is complete
        :param project_path: root path of the project relative to config file, template file and output file
        :param keep_failed: do not delete failed stacks
        :param dont_wait_for_delete: exits immediately after calling delete stack
        :param failed: rerun failed stacks
        :return: None
        '''
        # todo --failed param
        tests = await StackTest.from_file(
            template=template,
            project_config_file=config_file,
            no_delete=no_delete,
            regions=regions,
            project_path=project_path,
            keep_failed=keep_failed,
            dont_wait_for_delete=dont_wait_for_delete,
            test_names=test_names
        )
        if generate_parameters:
            all_configs = tests.configs
            parameters = {
                conf.region: conf.parameters for conf in all_configs
            }
            LOG.info(parameters)
            return

        async with tests:
            await tests.report(output_directory, project_path)

    @staticmethod
    async def clean(regions: str = None):
        '''
        Manually clean up the stacks which were created by Iacer
        :param regions: comma separated list of regions to delete from, default will scan all regions
        '''
        await Delete.create(regions)

    @staticmethod
    async def list(regions: str = None):
        '''
        List stacks which were created by Iacer for all regions
        :param regions:  comma separated list of regions to delete from, default will scan all regions
        '''
        await List.create(regions)

    @staticmethod
    async def params(template: str = None,
                     config_file: str = DEFAULT_CONFIG_FILE,
                     regions: str = None):
        '''
        Generate pseudo parameters
        :param template: path to a template
        :param config_file: path to a config file
        :param regions: comma separated list of regions
        '''
        tests = await StackTest.from_file(
            template=template,
            project_config_file=config_file,
            regions=regions
        )
        all_configs = tests.configs
        parameters = {
            conf.region: conf.parameters for conf in all_configs
        }
        LOG.info(parameters)
