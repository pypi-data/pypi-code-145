"""
Copyright 2021 Objectiv B.V.
"""
import bach
from bach.series import Series, SeriesString, SeriesInt64, SeriesFloat64

from sql_models.constants import NotSet, not_set
from typing import cast, List, Union, TYPE_CHECKING

from modelhub.decorators import use_only_required_objectiv_series
from modelhub.series import SeriesLocationStack
from modelhub.util import check_groupby

if TYPE_CHECKING:
    from modelhub import ModelHub
    from modelhub.series import SeriesLocationStack

GroupByType = Union[List[Union[str, Series]], str, Series, NotSet]
LocationStackType = Union[str, SeriesString, SeriesLocationStack, SeriesInt64]


class Aggregate:
    """
    Models that return aggregated data in some form from the original DataFrame with Objectiv data.
    """

    def __init__(self, mh: 'ModelHub'):
        self._mh = mh

    def _generic_aggregation(self,
                             data: bach.DataFrame,
                             groupby: Union[List[Union[str, Series]], str, Series],
                             column: str,
                             name: str):

        data = check_groupby(data=data,
                             groupby=groupby,
                             not_allowed_in_groupby=column)

        series = data[column].nunique()
        return series.copy_override(name=name)

    @use_only_required_objectiv_series(
        required_series=['user_id', 'moment'], include_series_from_params=['groupby'],
    )
    def unique_users(self,
                     data: bach.DataFrame,
                     groupby: GroupByType = not_set) -> bach.SeriesInt64:
        """
        Calculate the unique users in the Objectiv ``data``.

        :param data: :py:class:`bach.DataFrame` to apply the method on.
        :param groupby: sets the column(s) to group by.

            - if not_set it defaults to using :py:attr:`ModelHub.time_agg`.
            - if None it aggregates over all data.
        :returns: series with results.
        """

        groupby = [self._mh.time_agg(data)] if groupby is not_set else groupby

        return self._generic_aggregation(data=data,
                                         groupby=groupby,
                                         column='user_id',
                                         name='unique_users')

    @use_only_required_objectiv_series(
        required_series=['session_id', 'moment'], include_series_from_params=['groupby'],
    )
    def unique_sessions(self,
                        data: bach.DataFrame,
                        groupby: GroupByType = not_set) -> bach.SeriesInt64:
        """
        Calculate the unique sessions in the Objectiv ``data``.

        :param data: :py:class:`bach.DataFrame` to apply the method on.
        :param groupby: sets the column(s) to group by.

            - if not_set it defaults to using :py:attr:`ModelHub.time_agg`.
            - if None it aggregates over all data.
        :returns: series with results.
        """

        groupby = [self._mh.time_agg(data)] if groupby is not_set else groupby

        return self._generic_aggregation(data=data,
                                         groupby=groupby,
                                         column='session_id',
                                         name='unique_sessions')

    @use_only_required_objectiv_series(
        required_series=['session_id', 'moment'], include_series_from_params=['groupby']
    )
    def session_duration(self,
                         data: bach.DataFrame,
                         groupby: GroupByType = not_set,
                         exclude_bounces: bool = True,
                         method: 'str' = 'mean') -> bach.SeriesInt64:
        """
        Calculate the duration of sessions.

        With default `method`, it calculates the mean of the session duration over the `groupby`.

        :param data: :py:class:`bach.DataFrame` to apply the method on.
        :param groupby: sets the column(s) to group by.

            - if not_set it defaults to using :py:attr:`ModelHub.time_agg`.
            - if None it aggregates over all data.
        :param exclude_bounces: if True only session durations greater than 0 will be considered
        :param method: 'mean' or 'sum'
        :returns: series with results.
        """

        if groupby is not_set:
            groupby = self._mh.time_agg(data)

        if groupby is None:
            new_groupby = []
        elif not isinstance(groupby, list):
            new_groupby = [groupby]
        else:
            new_groupby = groupby
        new_groupby.append(data.session_id.copy_override(name='__session_id'))

        gdata = check_groupby(data=data, groupby=new_groupby)
        session_duration = gdata.aggregate({'moment': ['min', 'max']})
        session_duration['session_duration'] = session_duration['moment_max'] - session_duration['moment_min']

        if exclude_bounces:
            session_duration = session_duration[(session_duration['session_duration'].dt.total_seconds > 0)]

        if method not in ['sum', 'mean']:
            raise ValueError("only 'sum and 'mean' are supported for `method`")

        grouped_data = session_duration.groupby(session_duration.index_columns[:-1]).session_duration
        if method == 'sum':
            return grouped_data.sum()
        return grouped_data.mean()

    @use_only_required_objectiv_series(required_series=['user_id', 'session_id'])
    def frequency(self, data: bach.DataFrame) -> bach.SeriesInt64:
        """
        Calculate a frequency table for the number of users by number of sessions.

        :param data: :py:class:`bach.DataFrame` to apply the method on.
        :returns: series with results.
        """
        total_sessions_user = data.groupby(['user_id']).aggregate({'session_id': 'nunique'}).reset_index()
        frequency = total_sessions_user.groupby(['session_id_nunique']).aggregate({'user_id': 'nunique'})

        return frequency.user_id_nunique

    @use_only_required_objectiv_series(
        required_series=['location_stack', 'user_id', 'stack_event_types', 'event_type'],
        required_global_contexts=['application']
    )
    def top_product_features(self,
                             data: bach.DataFrame,
                             location_stack: 'SeriesLocationStack' = None,
                             event_type: str = 'InteractiveEvent') -> bach.DataFrame:
        """
        Calculate the top used features in the product.

        :param data: :py:class:`bach.DataFrame` to apply the method on.
        :param location_stack: the location stack

            - can be any slice of a :py:class:`modelhub.SeriesLocationStack` type column
            - if None - the whole location stack is taken.
        :param event_type: event type. Must be a valid event_type (either parent or child).
        :returns: bach DataFrame with results.
        """

        data = data.copy()

        # the following columns have to be in the data
        data['__application'] = data.application.context.id

        if location_stack is not None:
            data['__feature_nice_name'] = location_stack.ls.nice_name
        else:
            data['__feature_nice_name'] = data.location_stack.ls.nice_name

        groupby_col = ['__application', '__feature_nice_name', 'event_type']

        # selects specific event types, so stack_event_types must be a superset of [event_types]
        interactive_events = data[data.stack_event_types.json.array_contains(event_type)]

        # users by feature
        users_feature = interactive_events.groupby(groupby_col).agg({'user_id': 'nunique'})

        # remove double underscores from the columns name
        columns = {
            col: col[2:] if col.startswith('__') else col
            for col in groupby_col
        }
        _index = list(columns.values())
        users_feature = users_feature.reset_index().rename(columns=columns)
        users_feature = users_feature.dropna().set_index(_index)

        return users_feature.sort_values('user_id_nunique', ascending=False)

    @use_only_required_objectiv_series(
        required_series=[
            'location_stack', 'user_id', 'stack_event_types',
            # required by Map.conversions_in_time and Map.conversions_counter
            'session_id', 'moment', 'event_type',
        ],
        required_global_contexts=['application']
    )
    def top_product_features_before_conversion(self,
                                               data: bach.DataFrame,
                                               name: str,
                                               location_stack: 'SeriesLocationStack' = None,
                                               event_type: str = 'InteractiveEvent') -> bach.DataFrame:
        """
        Calculates what users did before converting by
        combining several models from the model hub.

        :param data: :py:class:`bach.DataFrame` to apply the method on.
        :param name: label of the conversion event.
        :param location_stack: the location stack

            - can be any slice of a :py:class:`modelhub.SeriesLocationStack` type column
            - if None - the whole location stack is taken.
        :param event_type: event type. Must be a valid event_type
            (either parent or child).
        :returns: bach DataFrame with results.
        """

        data = data.copy()

        if not name:
            raise ValueError('Conversion event label is not provided.')

        # temporary workaround, we should not call private constants and methods from Map
        # replace this after having a better solution

        from modelhub.map import _CalculatedConversionSeries
        # get conversion information
        # conversions_counter, is_conversion_event, conversions_in_time
        conversions_df = self._mh.map._get_calculated_conversion_df(
            series_to_calculate=_CalculatedConversionSeries.CONVERSIONS_COUNTER,
            data=data,
            name=name,
            partition='session_id',
        )

        # label sessions with a conversion
        converted_users = conversions_df['__converted'] >= 1

        # label hits where at that point in time, there are 0 conversions in the session
        zero_conversions_at_moment = conversions_df['__conversions_in_time'] == 0
        conversions_df = conversions_df[converted_users & zero_conversions_at_moment]

        # select only user interactions
        data = data[data.stack_event_types.json.array_contains(event_type)]

        # merge with filtered conversion interactive events
        converted_users_filtered = data.merge(conversions_df, on='event_id')
        converted_users_filtered['__application'] = converted_users_filtered.application.context.id

        if location_stack is not None:
            converted_users_filtered['__feature_nice_name'] = location_stack.ls.nice_name
        else:
            converted_users_filtered['__feature_nice_name'] = (
                converted_users_filtered.location_stack.ls.nice_name
            )

        converted_users_filtered.materialize(
            node_name='extract_application_and_feature_nice_name', inplace=True,
        )

        groupby_col = ['__application', '__feature_nice_name', 'event_type']
        converted_users_features = self._mh.agg.unique_users(converted_users_filtered,
                                                             groupby=groupby_col)

        # remove double underscores from the columns name
        columns = {
            col: col[2:] if col.startswith('__') else col
            for col in groupby_col
        }
        _index = list(columns.values())
        converted_users_features = converted_users_features.reset_index().rename(columns=columns)
        converted_users_features = converted_users_features.dropna().set_index(_index)

        return converted_users_features.sort_values('unique_users', ascending=False)

    @use_only_required_objectiv_series(required_series=['user_id', 'moment', 'event_type'])
    def retention_matrix(self,
                         data: bach.DataFrame,
                         time_period: str = 'monthly',
                         event_type: str = None,
                         start_date: str = None,
                         end_date: str = None,
                         percentage=False,
                         display=True) -> bach.DataFrame:

        """
        Finds the number of users in a given cohort who are active at a given time
        period, where time is computed with respect to the beginning of each cohort.
        The "active user" is the user who made an action that we are interested in
        that time period.
        Users are divided into mutually exclusive cohorts, which are then
        tracked over time. In our case users are assigned to a cohort based on
        when they made their first action that we are interested in.

        Returns the retention matrix dataframe, it represents users retained across cohorts:

        - index value represents the cohort
        - columns represent the number of given date period since the current cohort
        - values represent number (or percentage) of unique active users of a given cohort

        One can calculate the retention matrix for a given time range, for that
        one can specify start_date a/o end_date.
        N.B. the users' activity starts to be traced from the first date the user is seen in the `data`.


        :param data: :py:class:`bach.DataFrame` to apply the method on.
        :param time_period: can be 'daily', 'weekly', 'monthly' or 'yearly'.
        :param event_type: the event/action that we are interested in.
            Must be a valid event_type (either parent or child).
            if None we take all the events generated by the user.
        :param start_date: start date of the retention matrix, e.g. '2022-04-01'
            if None take all the data.
        :param end_date: end date of the retention matrix, e.g. '2022-05-01'
            if None take all the data.
        :param percentage: if True calculate percentage with respect to the number of a users
            in the cohort, otherwise it leaves the absolute values.
        :param display: if display==True visualize the retention matrix as a heat map

        :returns: retention matrix bach DataFrame.

        .. vimeoplayer::
            :videoid: 723381969
            :trackingid: product-demo-retention-matrix
            :paddingbottom: 58.25%
        """

        available_formats = {'daily', 'weekly', 'monthly', 'yearly'}

        if time_period not in available_formats:
            raise ValueError(f'{time_period} time_period is not available.')

        from datetime import datetime

        _start_date = None
        if start_date is not None:
            try:
                _start_date = datetime.strptime(start_date, '%Y-%m-%d')
            except Exception as e:
                print('Please provide correct start_date formatted as "YYYY-MM-DD".')
                raise e

        _end_date = None
        if end_date is not None:
            try:
                _end_date = datetime.strptime(end_date, '%Y-%m-%d')
            except Exception as e:
                print('Please provide correct end_date formatted as "YYYY-MM-DD".')
                raise e

        data = data.copy()

        # filtering data with the event that we are interested in
        if event_type is not None:
            data = data[data['event_type'] == event_type]

        # for retention matrix calculation we need only event date and user_id
        columns = ['user_id', 'moment']
        data = data[columns]

        # get the first cohort
        cohorts = cast(
            bach.DataFrame, data.groupby('user_id')['moment'].min().reset_index()
        )
        cohorts = cohorts.rename(columns={'moment': 'first_cohort_ts'})

        # add first cohort to our data DataFrame
        data = data.merge(cohorts, on='user_id')

        # help mypy
        from bach import SeriesTimestamp, SeriesTimedelta
        moment = cast(SeriesTimestamp, data['moment'])
        first_cohort_ts = cast(SeriesTimestamp, data['first_cohort_ts'])

        # calculate cohort distance
        if time_period == 'yearly':
            data['cohort'] = moment.dt.strftime('%Y').astype(dtype=int)
            data['first_cohort_yearly'] = first_cohort_ts.dt.strftime('%Y').astype(dtype=int)
            data['cohort_distance'] = data['cohort'] - data['first_cohort_yearly']

            data['first_cohort'] = first_cohort_ts.dt.strftime('%Y')
        elif time_period == 'monthly':
            data['cohort_year'] = moment.dt.strftime('%Y').astype(dtype=int)
            data['first_cohort_year'] = first_cohort_ts.dt.strftime('%Y').astype(dtype=int)
            data['cohort_year_diff'] = data['cohort_year'] - data['first_cohort_year']

            data['cohort_month'] = moment.dt.strftime('%m').astype(dtype=int)
            data['first_cohort_month'] = first_cohort_ts.dt.strftime('%m').astype(dtype=int)
            data['cohort_month_diff'] = data['cohort_month'] - data['first_cohort_month']

            n_months = 12
            data['cohort_distance'] = data['cohort_year_diff'] * n_months + data['cohort_month_diff']

            data['first_cohort'] = first_cohort_ts.dt.strftime('%Y-%m')
        elif time_period == 'weekly':
            n_days = 7.0

            data['cohort'] = moment.dt.date_trunc('week').astype('timestamp')
            data['first_cohort_weekly'] = first_cohort_ts.dt.date_trunc('week')
            cohort_distance = cast(SeriesTimedelta, data['cohort'] - data['first_cohort_weekly'])
            data['cohort_distance'] = cohort_distance.dt.days
            data['cohort_distance'] = data['cohort_distance'] / n_days

            pretty_name = cast(SeriesTimestamp, data['first_cohort_weekly']).dt.strftime('%Y-%m-%d')
            data['first_cohort'] = pretty_name
        else:
            # daily
            data['cohort_distance'] = data['moment'] - data['first_cohort_ts']
            data['cohort_distance'] = cast(SeriesTimedelta, data['cohort_distance']).dt.days
            data['first_cohort'] = first_cohort_ts.dt.strftime('%Y-%m-%d')

        # applying start date filter
        if _start_date is not None:
            data = data[data['first_cohort_ts'] >= _start_date]

        # applying end date filter
        if _end_date is not None:
            data = data[data['moment'] < _end_date]

        cd_series = data['cohort_distance'].copy_override_type(bach.SeriesFloat64).round()
        formatted_cd_series = (
            cd_series.astype(dtype=bach.SeriesString.dtype).copy_override_type(bach.SeriesString)
        )
        data['cohort_distance_prefix'] = '_'
        data['cohort_distance'] = data['cohort_distance_prefix'] + formatted_cd_series

        retention_matrix = data.groupby(['first_cohort',
                                         'cohort_distance']).agg({'user_id': 'nunique'}).unstack(
            level='cohort_distance')

        # renaming columns, removing string attached after unstacking
        column_name_map = {col: col.replace('__user_id_nunique', '')
                           for col in retention_matrix.data_columns}
        retention_matrix = retention_matrix.rename(columns=column_name_map)

        # 'sort' with column names (numerical sorting, even though the columns are strings)
        columns = [f'_{j}' for j in sorted([int(i.replace('_', ''))
                                            for i in retention_matrix.data_columns])]
        retention_matrix = retention_matrix[columns]
        # for BigQuery we need sorting
        retention_matrix = retention_matrix.sort_index()

        if percentage and len(columns):
            first_column = retention_matrix[columns[0]]
            for col in columns:
                retention_matrix[col] = (retention_matrix[col] / first_column) * 100

        if display and len(columns):
            import matplotlib.pyplot as plt
            import seaborn as sns
            fig, ax = plt.subplots(figsize=(20, 8))
            sns.heatmap(retention_matrix.to_pandas(), annot=True, square=True, ax=ax,
                        linewidths=.5, cmap=sns.cubehelix_palette(rot=-.4), fmt='.1f')
            if percentage:
                [t.set_text(f'{t.get_text()}%') for t in ax.texts]

            plt.title('Cohort Analysis')

            nice_name = {
                'daily': 'Days',
                'weekly': 'Weeks',
                'monthly': 'Months',
                'yearly': 'Years'
            }

            plt.xlabel(f'{nice_name[time_period]} After First Event')
            plt.ylabel('First Event Cohort')
            plt.show()

        return retention_matrix

    @staticmethod
    def drop_off_locations(data: bach.DataFrame,
                           location_stack: LocationStackType = None,
                           groupby: Union[List[Union[str, Series]], str, Series] = 'user_id',
                           percentage=False) -> bach.DataFrame:
        """
        Find the locations/features where users drop off, and their usage/share.

        :param data: :py:class:`bach.DataFrame` to apply the method on.
        :param location_stack: the column of which to create the drop-off locations.
            Can be a string of the name of the column in data, or a Series with the
            same base node as `data`. If None the default location stack is taken.

            - can be any slice of a :py:class:`modelhub.SeriesLocationStack` type column.
            - if `None`, the whole location stack is taken.
        :param groupby: sets the column(s) to group by.
        :param percentage: if True calculate the percentage.

        :returns: :py:class:`bach.DataFrame` with the location where users drop off, and the count/percentage.
        """

        data = data.copy()

        column = location_stack or data['location_stack']
        if type(column) == str:
            column = data[column]

        data['location'] = column
        if type(column) == SeriesLocationStack:
            # extract the nice name per event
            data['location'] = column.ls.nice_name

        # need to drop missing values because we don't
        # want to get as a last step None value
        data = data.dropna(subset='location')

        window = data.sort_values(by='moment', ascending=True).groupby(groupby).window(
            end_boundary=bach.partitioning.WindowFrameBoundary.FOLLOWING,
        )
        drop_loc = window['location'].window_last_value()
        drop_loc = drop_loc.materialize(distinct=True)

        result = drop_loc.value_counts(normalize=percentage).to_frame()
        if percentage:
            result = result.rename(columns={'value_counts': 'percentage'})
            result['percentage'] *= 100
            result = result.sort_values(by='percentage', ascending=False)
        return result

    def funnel_conversion(self,
                          data: bach.DataFrame,
                          location_stack: LocationStackType = None,
                          groupby: Union[List[str], str] = None
                          ) -> bach.DataFrame:
        """
        Calculates conversion numbers for all locations stacks in the `data`.
        N.B. Filter the dataframe beforehand to filter down to the funnel locations.


        For each step in a funnel, calculates the number of unique users who started it,
        the number of unique users who completed the step (defined as whether the user
        went to any other step in the funnel),
        the conversion rate to completing the step, the conversion rate to completing the step
        when looking at all users who started the funnel (= the 'full' conversion rate),
        and the fraction of the users in the funnel dropping out at the given step.

        N.B. We assumed that the funnel direction is always the same.
        The implementation of VisibleEvents makes for the most accurate calculation
        of the conversion numbers, as the number of users as well as the conversion rate
        is based on events on each location stack.

        :param data: The :py:class:`bach.DataFrame` to apply the operation on.
        :param location_stack: The column that holds the steps in the funnel. Can be:

            - A string of the name of the column in `data`.
            - Any slice of a :py:class:`modelhub.SeriesLocationStack` type column.
            - A Series with the same base node as `data`.

            If its value is `None`, the whole location stack is taken.
        :param groupby: sets the column(s) to group by. It would be also handy later
            for the filtering of the results.

        :returns: :py:class:`bach.DataFrame` with the following columns: `step` (the location considered as a
            step, e.g. a feature or root location), `n_users` (number of unique users starting the step),
            `n_users_completed_step` (number of unique users completing the step),
            `step_conversion_rate` (number of users completing the step / `n_users`), `full_conversion_rate`
            (number of users completing the step / number of users starting the funnel), and `dropoff_share`
            (ratio between the users dropping out at a given step and users at the begging at the funnel).
        """

        if groupby is None:
            new_groupby = []
        elif not isinstance(groupby, list):
            new_groupby = [groupby]
        else:
            new_groupby = groupby

        data = data.copy()

        from modelhub.util import check_objectiv_dataframe
        columns_to_check = ['location_stack', 'user_id', 'session_id',
                            'session_hit_number', 'moment']
        check_objectiv_dataframe(df=data, columns_to_check=columns_to_check)

        column = location_stack or data['location_stack']
        if type(column) == str:
            column = data[column]
        data['location'] = column
        if type(column) == SeriesLocationStack:
            # extract the nice name per event
            data['location'] = column.ls.nice_name
        location = 'location'

        df_root_user = data.sort_values(['session_id', 'session_hit_number']).\
            drop_duplicates(subset=[location, 'user_id'], keep='first')

        gb: Union[str, List] = location
        funnel_by: List = ['user_id']
        merge_gb: Union[str, List] = f'{location}_step_1'
        sorting: Union[str, List] = 'n_users'
        if new_groupby:
            gb = new_groupby + [location]
            funnel_by = new_groupby + ['user_id']
            merge_gb = new_groupby + [f'{location}_step_1']
            sorting = new_groupby + ['n_users']

        funnel = self._mh.get_funnel_discovery()
        df_steps = funnel.get_navigation_paths(df_root_user, location_stack=location,
                                               steps=2, by=funnel_by, sort_by='moment')

        # n_users
        step_visitors_df = df_root_user.groupby(gb)['user_id'].nunique().to_frame().\
            reset_index().rename(columns={'user_id': 'n_users'})

        # n_users_completed_step
        # remove rows where 2nd step is NaN (it means the user left the funnel)
        step_completed_df = df_steps.dropna().reset_index()[funnel_by + [f'{location}_step_1']]
        step_completed_df = step_completed_df.groupby(merge_gb).count()\
            .rename(columns={'user_id_count': 'n_users_completed_step'}).sort_index()

        # merging n_users with n_users completed_step and n_users for drop-offs
        result = step_visitors_df.merge(step_completed_df,
                                        left_on=gb,
                                        right_on=merge_gb,
                                        how='left').reset_index(drop=True)
        result['n_users_completed_step'] = result['n_users_completed_step'].fillna(0)

        if new_groupby:
            result = result.merge(result.groupby(new_groupby)['n_users'].max(),
                                  on=list(new_groupby), suffixes=('', '_max'))
        else:
            result['n_users_max'] = result['n_users'].max()

        # n_users drop-offs
        result['dropoff_share'] = result['n_users'] - result['n_users_completed_step']
        result['dropoff_share'] = cast(SeriesFloat64,
                                       (result['dropoff_share'] / result['n_users_max'])).round(3)

        # step_conversion_rate
        result['step_conversion_rate'] = result['n_users_completed_step'] / result['n_users']
        result['step_conversion_rate'] = cast(SeriesFloat64, result['step_conversion_rate']).round(3)

        # full_conversion_rate
        result['full_conversion_rate'] = result['n_users_completed_step'] / result['n_users_max']
        result['full_conversion_rate'] = cast(SeriesFloat64, result['full_conversion_rate']).round(3)

        columns = [location, 'n_users', 'n_users_completed_step', 'step_conversion_rate',
                   'full_conversion_rate', 'dropoff_share']
        if new_groupby:
            columns = new_groupby + columns

        return result[columns].sort_values(sorting, ascending=False)
