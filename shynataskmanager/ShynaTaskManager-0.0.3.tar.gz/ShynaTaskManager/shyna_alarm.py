from ShynaDatabase import Shdatabase
from Shynatime import ShTime
from ShynaTelegramBotNotification import BotNotify
import os


class ShynaAlarm:
    s_data = Shdatabase.ShynaDatabase()
    s_time = ShTime.ClassTime()
    s_bot = BotNotify.BotShynaTelegram()
    result = False
    wakeup_sentence = str("It is time, please wake up|It is late please wake up|Wake up Boss|Wake up it is "
                          + str(int(s_time.string_to_time(s_time.now_time).hour)-12) +
                          " pm" if int(s_time.string_to_time(s_time.now_time).hour) > 12
                          else "Morning!.Wake up it is " + str(s_time.string_to_time(s_time.now_time).hour))

    def get_time_table(self):
        try:
            self.s_data.default_database = os.environ.get('alarm_db')
            self.s_data.query = "Select * from alarm where alarm_status='True' and alarm_date='" \
                                + str(self.s_time.now_date) + "' order by count DESC"
            self.result = self.s_data.select_from_table()
            # print(self.result)
            if str(self.result[0]).lower().__eq__('empty'):
                print("No Alarm to set")
            else:
                for item in self.result:
                    print("Processing for", item)
                    alarm_count = item[0]
                    alarm_title = item[3]
                    alarm_date = item[4]
                    alarm_time = item[5]
                    alarm_snooze_status = item[6]
                    alarm_snooze = item[7]
                    alarm_repeat_status = item[8]
                    alarm_repeat = item[9]
                    self.process_upcoming_alarm(alarm_count, alarm_title, alarm_date, alarm_time, alarm_snooze_status,
                                                alarm_snooze, alarm_repeat_status, alarm_repeat)
        except Exception as e:
            self.s_bot.message = "Exception at get time from alarm table: " + str(e)
            self.s_bot.bot_send_msg_to_master()
            print(e)

    def process_upcoming_alarm(self, alarm_count, alarm_title, alarm_date, alarm_time, alarm_snooze_status,
                               alarm_snooze, alarm_repeat_status, alarm_repeat):
        try:
            new_date = self.s_time.now_date
            if self.is_it_time(alarm_date=str(alarm_date), alarm_time=str(alarm_time),
                               standard_time=str(self.s_time.now_time)):
                print("creating task for ", alarm_count)
                if str(alarm_title).lower().__contains__('alarm'):
                    self.s_data.default_database = os.environ.get('taskmanager_db')
                    self.s_data.query = "Insert into Task_Manager (new_date, new_time, task_id, task_date, task_time, "\
                                        "task_type, Speak, snooze_status, snooze_duration) VALUES('" \
                                        + str(self.s_time.now_date) + "','" + str(self.s_time.now_time) + "','" \
                                        + str(alarm_count) + "','" + str(self.s_time.now_date) + "','" \
                                        + str(alarm_time) + "','" + str("Alarm") + "','" + str(self.wakeup_sentence) + \
                                        "','" + str(alarm_snooze_status) + "','" + str(alarm_snooze) + "') "
                    self.s_data.create_insert_update_or_delete()
                    if str(alarm_repeat_status).lower().__eq__('true'):
                        if str(alarm_repeat).lower().__eq__('daily'):
                            new_date = self.s_time.daily()
                        elif str(alarm_repeat).lower().__eq__('weekend'):
                            new_date = self.s_time.weekends()
                        elif str(alarm_repeat).lower().__eq__('weekdays'):
                            new_date = self.s_time.get_weekdays()
                        elif str(alarm_repeat).lower().__eq__('alternative'):
                            new_date = self.s_time.alternative()
                        else:
                            new_date = self.s_time.now_date
                        self.s_data.default_database = os.environ.get('alarm_db')
                        self.s_data.query = "Update alarm set alarm_date='"+str(new_date)+"' where count='"\
                                            + str(alarm_count)+"'"
                        self.s_data.create_insert_update_or_delete()
                    else:
                        self.s_data.default_database = os.environ.get('alarm_db')
                        self.s_data.query = "Update alarm set alarm_status='False' where count='" \
                                            + str(alarm_count) + "'"
                        self.s_data.create_insert_update_or_delete()
                else:
                    print("Not an alarm")
            else:
                print("It is not the time")
        except Exception as e:
            print(e)

    def is_it_time(self, alarm_date, alarm_time, standard_time):
        time_diff = False
        try:
            if self.s_time.string_to_date(str(alarm_date)) == self.s_time.string_to_date(str(self.s_time.now_date)):
                if self.s_time.string_to_time_with_date(str(alarm_time)) > \
                        self.s_time.string_to_time_with_date(str(standard_time)):
                    time_diff = True if 0 <= self.s_time.string_to_time_with_date(str(
                        self.s_time.string_to_time_with_date(str(alarm_time)) - self.s_time.string_to_time_with_date(
                            str(standard_time)))).minute < 1 else False
                    if time_diff:
                        time_diff = True
                        print(time_diff)
                    else:
                        time_diff = False
                else:
                    time_diff = False
            else:
                time_diff = False
            return time_diff
        except Exception as e:
            print(e)


if __name__ == '__main__':
    ShynaAlarm().get_time_table()
