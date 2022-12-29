from datetime import datetime, timezone
import os
import csv
from collections import namedtuple
import json
import time
import sys
import traceback
import getopt
import argparse

from pymongo import MongoClient, ASCENDING, DESCENDING
from utils import decode_ft_flag,  decode_exchange_id
from logger import Logger


class FtTool(object): 
    
    def __init__(self, config_filename, update_trade_date, sync_pos, sync_trade, sync_add):
        self.load_ft_setting(config_filename)
        self.logger = Logger.get_logger(self.logname, self.log_file_path)
        self.update_trade_date = update_trade_date
        self.sync_pos = sync_pos
        self.sync_trade = sync_trade
        self.sync_add = sync_add
        
        try:
            self.db_client = {}
            self.order_info_db = {}
            self.tradelog_db = {}
            for acc in self.accounts_run:
                self.db_client[acc] = MongoClient(
                    self.mongo_host[acc], self.mongo_port[acc], connectTimeoutMS=10000, socketTimeoutMS = 3000)
                db_client = self.db_client[acc]
                if self.tradingaccount_user[acc] != '' and self.tradingaccount_pwd[acc] != '':
                    db_client["tradingAccount"].authenticate(
                        self.tradingaccount_user[acc], self.tradingaccount_pwd[acc], mechanism='SCRAM-SHA-1')
                self.order_info_db[acc] = db_client["tradingAccount"]
                
                if self.tradinglog_user[acc] != '' and self.tradinglog_pwd[acc] != '':
                    db_client["tradingLog"].authenticate(
                        self.tradinglog_user[acc], self.tradinglog_pwd[acc], mechanism='SCRAM-SHA-1')
                db_client.server_info()
                self.tradelog_db[acc] = db_client["tradingLog"] 
                
            #for test
            #self.db_client = MongoClient()
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[init] DB_connect_failed! (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
            exit()

        
        #test for req_position
        self.db_client_test = MongoClient("127.0.0.1", 27017, connectTimeoutMS=10000)
        self.test_trading_account = self.db_client_test['tradingAccount']

        self.get_acccount_info()
    
    def load_ft_setting(self, config_filename):
        try:
            #f = open(config_filename, encoding="utf-8")
            f = open(config_filename)
            setting = json.load(f)
            
            
            self.socket_url = setting['websocket_url']
            self.login_url = setting['login_url']
            path = setting['log_filepath']
            self.log_file_path = path.replace('/', '\\')
            self.ft_tradecsv_path = setting['ft_tradecsv_path'].replace('/', '\\')
            self.upload_mudan_url = setting['upload_mudan_url']
            self.feishu_url = setting.get('feishu_url')
            self.cancel_url = setting['cancel_url']
            # self.log_accountname = setting['ACCOUNT_NAME'] #用于tradinglog数据库,order/trade
            # 产品名称，用于获取tg_name和account_name
            self.sync_position_open = setting['sync_position_open'] #设置同步持仓的时间
            self.sync_position_close = setting['sync_position_close']
            #self.tgname = setting['tg_name']
            # self.target_accountname = self.tgname + '@' + self.log_accountname #下单时用

            self.logname = setting['logname']
            self.scan_interval = setting['scan_interval']
            
            #get config by product
            self.accounts_config = setting['accounts']
            self.accounts_run = setting['run'] #0 zhongxincats1 1 huaxin ...
            
            self.config = {}
            self.account_id = {}
            self.product_names = {}
            self.log_account_names = {}
            self.tgnames = {}
            self.mongo_host = {}
            self.mongo_port = {}
            self.tradingaccount_user = {}
            self.tradingaccount_pwd = {}
            self.tradinglog_user = {}
            self.tradinglog_pwd = {}
            self.target_account_names = {}
            self.target_account_names_to_acc = {}
            for acc in self.accounts_run:
                self.config[acc] = setting['accounts'][acc]
                config = self.config[acc]
                self.account_id[acc] = config['account_id']
                self.product_names[acc] = config['product_name']
                self.log_account_names[acc] = config['account_name']
                self.tgnames[acc] = config['equity_tg_name']
                self.target_account_names[acc] = config['equity_tg_name'] + "@" + config['account_name']
                self.target_account_names_to_acc[self.target_account_names[acc]] = acc
                self.mongo_host[acc] = config['mongoHost']
                self.mongo_port[acc] = config['mongoPort']
                datadbuser = config['databaseUser']
                self.tradingaccount_user[acc] = datadbuser['tradingAccount']['user']
                self.tradingaccount_pwd[acc] = datadbuser['tradingAccount']['password']
                self.tradinglog_user[acc] = datadbuser['tradingLog']['user']
                self.tradinglog_pwd[acc] = datadbuser['tradingLog']['password']
            
        except Exception as e:
            err = traceback.format_exc()
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
            print(f"load config failed! (exception){err}")
            exit(0)

    def get_acccount_info(self):
        try:
            for acc in self.accounts_run:
                product_name = self.product_names[acc]
                query = {"product_name": product_name}
                account_info_collection = self.order_info_db[acc]['account_info']
                account_info = account_info_collection.find_one(query)
                if account_info == None:
                    self.logger.error(
                        f"[get_account_info] can't_find_account_info (product_name){product_name}")
                    continue
                tgname = account_info['equity_tg_name']
                self.tgnames[acc] = tgname
                log_accountname = account_info['account_name']
                self.log_account_names[acc] = log_accountname
                target_accountname = tgname + '@' + log_accountname
                self.target_account_names[acc] = target_accountname # 下单时用self
                self.logger.info(
                    f"[get_account_info] (tg_name){self.tgnames} (logacc_name){self.log_account_names} (target_accountnames){self.target_account_names}")
        except Exception as e:
            err = traceback.format_exc()
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger.error(f'[get_account_info] (exception){err}')
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)

    def start(self):
        
        #trade_export_path = r'C:\Users\Administrator\Downloads\ft_client_win_1.6.4\ft_client_win\export\20221201\20221201_326000024361_trade.csv'
        if self.sync_trade == True:
            self.logger.info(f"in get_trade")
            self.get_trade_from_csv()
        
        if self.sync_pos == True:
            self.date_change()
        
        if self.sync_add == True:
            self.sync_position_add()            
        
    def get_trade_from_csv(self):
        try:
            #trade_collection = self.test_trading_log['trade'] #测试数据库
            for acc in self.accounts_run:
                
                dt = datetime.now()
                date = dt.strftime("%Y%m%d")
                if not self.update_trade_date == date:
                    date = self.update_trade_date
                    filter_time_array = datetime(year=2022,month=12,day=29)
                else:
                    filter_time_array = datetime.today().replace(hour=0,minute=0,second=0)
                account_id = self.account_id[acc]
                path = self.ft_tradecsv_path + f'{date}\\{date}_{account_id}_trade.csv'
                #path = f"C:\\Users\\Administrator\\Downloads\\ft_client_win_1.8.0\\ft_client_win\\export\\{date}\\{date}_{account_id}_trade.csv"
                trade_collection = self.tradelog_db[acc]['trade']
                ft_order_collection = self.order_info_db[acc]['ft_order']
                ft_sync_trade_collection = self.order_info_db[acc]['ft_sync_trade']
                del_res = ft_sync_trade_collection.delete_many({})
                self.logger.info(f"deleted {del_res.deleted_count}tf_sync_trade_msg")
                self.logger.info(f"[get_trade_from_csv] get_trade_msg_from(path){path}")
                with open(path, encoding='gbk')as f:
                    reader = csv.reader(f)
                    headers = next(reader)
                    Row = namedtuple('Row', headers)
                    for row in reader:
                        row = Row(*row)
                        traded_vol = int(row.成交数量)
                        traded_price = float(row.成交价格)
                        int_ticker = int(row.股票代码)
                        ticker = f'{int_ticker:06d}'
                        mudan_id = int(row.母单编号)
                        query_for_exchange = {"ticker": ticker}
                        exchange = 0
                        target = self.order_info_db[acc]['ft_position'].find_one(query_for_exchange)
                        #self.logger.info(f"(target){target}")
                        if not target == None:
                            exchange = target['exchange']
                        if traded_vol > 0:
                            local_id = str(row.本地编号)
                            origin_order_query = {"mudan_id" : mudan_id}
                            target = ft_order_collection.find_one(origin_order_query)
                            oid = 0
                            sid = "" # f"[PR_Ver_1_0_1_HX]{row.股票代码}T20221125"
                            entrust_vol = 0
                            side = 0
                            accountName = ""
                            order_type = 215
                            if not target == None:
                                oid = target['oid']
                                sid = target['sid']
                                entrust_vol =  int(target['order_msg']['order_vol'])
                                bs_flag = target['order_msg']['bs_flag']
                                if bs_flag == 'buy':
                                    side = 1
                                elif bs_flag == 'sell':
                                    side = 2
                                accountName = target['order_msg']['log_accountname']
                                #order_type = target['order_msg']['order_type']
                            timerow = row.委托时间
                            timearray = time.strptime(timerow, "%Y-%m-%d %H:%M:%S")
                            dt = datetime.fromtimestamp(time.mktime(timearray), timezone.utc)
                            
                            trade_msg = {
                                "trade_ref": local_id, # broker 端的交易回报 id
                                "oid": oid,
                                "ticker": ticker,
                                "exchange" : exchange,
                                "traded_vol": traded_vol, 
                                "traded_price": traded_price,
                                "order_type": order_type, 
                                "side": side,  # 对应 tlclient.trader.constant 包 Side 
                                "entrust_vol": entrust_vol,
                                "entrust_price": 0,
                                "dbTime":datetime.now(timezone.utc),
                                "sid": sid, # 对应订单中的 sid
                                "commission": 0,
                                "trade_time": dt,
                                "accountName": accountName, # 对应 account_info.account_name
                                }
                            
                            query = {"trade_ref" : local_id , "accountName" : accountName, "trade_time": { "$gt": filter_time_array}}

                            if trade_collection.find_one(query) == None:
                                res = trade_collection.replace_one(query, trade_msg, True)
                                self.logger.info(f"[get_trade_from_csv] (res){res} (trade_msg){trade_msg}")
                                if ft_sync_trade_collection.find_one(query) == None:
                                    res = ft_sync_trade_collection.replace_one(query, trade_msg, True)
                                    self.logger.info(f"[get_trade_from_csv] ft_sync_trade(res){res} (trade_msg){trade_msg}")
                            else:
                                self.logger.info(f"[get_trade_from_csv] (trade_ref){local_id}exist (trade_msg){trade_msg}")                                
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[get_trade_from_csv] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
                    
    def date_change(self):
        try:
                dt = datetime.now()
                self.logger.info(f"(dt){dt.hour}")
                if dt.hour <= self.sync_position_open and self.sync_pos == True:
                    self.logger.info("[date_change] date_change_open")
                    self.sync_position()
                    self.update_position_date_open()
                elif dt.hour < self.sync_position_close:
                    self.logger.info("[date_change] date_not_change")
                    time.sleep(600)
                elif dt.hour >= self.sync_position_close and self.sync_pos == True:
                    self.logger.info("[date_change] date_change_close")
                    self.sync_position()
                    self.update_position_date_close()
                                            
                else:
                    self.logger.info("[date_change] date_not_change")
                    return 
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[date_change] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)

    def sync_position_add(self):
        try:
            for acc in self.accounts_run:
                trade_today_collection = self.order_info_db[acc]['ft_sync_trade']
                equity_position_collection = self.order_info_db[acc]['EquityPosition']
                account_name = self.target_account_names[acc]
                positions_query = {'accountName': account_name}
                equity_positions = equity_position_collection.find(positions_query)
                if equity_positions.count() == 0:
                    self.logger.error("[sync_position_add] find_nothing_in_equityposition")
                else:
                    for position in equity_positions:
                        sid = position['sid']
                        if sid.startswith('[ADD]'):
                            ticker = position['ticker']
                            sync_trade_query = {'ticker' : ticker}
                            sid_to_traded_vol = {}
                            sync_trades = trade_today_collection.find(sync_trade_query)
                            if not sync_trades.count() == 0:
                                for sync_trade in sync_trades:
                                    trade_sid = sync_trade['sid']
                                    sid_to_traded_vol[trade_sid] = 0
                                    vol = sid_to_traded_vol[trade_sid]
                                    if sync_trade['side'] == 1:
                                        vol += sync_trade['traded_vol']
                                    elif sync_trade['side'] == 2:
                                        vol -= sync_trade['traded_vol']
                            else:
                                self.logger.info("[sync_position_add] nothing")
                            for key,value in sid_to_traded_vol.items():
                                position_sid = key
                                position_yd_vol = value
                                query_by_sid = {'sid': position_sid}
                                one_trade = trade_today_collection.find_one(query_by_sid)
                                exchange = one_trade['exchange']
                                position_for_update = equity_position_collection.find_one(query_by_sid)
                                if position_for_update is not None:
                                    yd_pos_long = position_for_update['yd_pos_long'] + position_yd_vol
                                    actual_yd_pos_long = position_for_update['actual_yd_pos_long'] + position_yd_vol
                                    data_to_update ={
                                        'yd_pos_long' : yd_pos_long,
                                        'actual_yd_pos_long' : actual_yd_pos_long
                                    }
                                    new_data = {"$set": data_to_update}
                                    res = equity_position_collection.update_one(query_by_sid, new_data)
                                else:
                                    self.add_position_for_add(acc, exchange = exchange, ticker = ticker, td_vol = 0, yd_vol = position_yd_vol, accountName = account_name, sid = position_sid)
                            query_for_delete_add = {'sid' : sid}
                            equity_position_collection.delete_one(query_for_delete_add)
                            self.logger.info(f"delete_position (sid){sid}")
                            
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[sync_position_for_add] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)                      
                            
            
    def add_position_for_add(self, acc, exchange, ticker, td_vol, yd_vol, accountName, sid):
        try:
            collection = self.order_info_db[acc]['EquityPosition']
            #collection = self.test_trading_account['EquityPosition']
            #exchange = int(pos['exchange'])
            order_collection = self.order_info_db[acc]['ft_order']
    
            total_vol = td_vol + yd_vol
            self.logger.warning(
                f'[add_position_for_debug] add_position (ticker){ticker} (total_vol){total_vol}')
            record = {}
            record['accountName'] = accountName
            record['ticker'] = ticker
            record['yd_pos_long'] = yd_vol
            record['yd_pos_short'] = 0
            record['td_pos_long'] = td_vol
            record['td_pos_short'] = 0
            record['actual_td_pos_long'] = td_vol
            record['actual_yd_pos_long'] = yd_vol
            # 持仓平均成本 非凸只返回仓位,无法计算cost,和market_value
            record['cost'] = 0
            record['mkt_value'] = 0
            record['enter_date'] = datetime.now(timezone.utc)
            record['holding_days'] = 0 
            record['sid'] = sid
            record['exchange'] = exchange
            filter = {'sid' : record['sid']}
            res = collection.replace_one(filter, record, True) 
            self.logger.info(f"[add_position_for_debug] (res){res} (msg){record}")
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[add_position_for_add] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)          

    def update_position_date_open(self):
        for acc in self.accounts_run:
            collection = self.order_info_db[acc]['EquityPosition']
            target_accountname = self.target_account_names[acc]
            targets_query = {'accountName' : target_accountname}
            targets = collection.find(targets_query)
            self.logger.info(f"now (target_account_name){target_accountname}")
            if targets.count() == 0:
                continue
            for position in targets:
                        self.logger.info(f"goes in (position){position}")
                        sid = position['sid']
                        query = {'sid' : sid}
                        holdingdays = position['holding_days']
                        yd_pos = position['actual_td_pos_long'] + position['actual_yd_pos_long']
                        td_pos = 0
                        change = {
                                        'holding_days': holdingdays,
                                        'yd_pos_long': yd_pos,
                                        'td_pos_long': td_pos,
                                        'actual_yd_pos_long': yd_pos,
                                        'actual_td_pos_long': td_pos
                                    }
                        new_data = {"$set": change}
                        res = collection.update_one(
                                                query, new_data, True)
                        self.logger.info(f"[date_change_open] (res){res} (change){change}")
    
    def update_position_date_close(self):
        for acc in self.accounts_run:
            collection = self.order_info_db[acc]['EquityPosition']
            target_accountname = self.target_account_names[acc]
            targets_query = {'accountName' : target_accountname}
            targets = collection.find(targets_query)
            if targets.count() == 0:
                continue
            for position in targets:
                    sid = position['sid']
                    query = {'sid' : sid}
                    holdingdays = position['holding_days'] + 1
                    yd_pos = position['actual_td_pos_long'] + position['actual_yd_pos_long']
                    td_pos = 0
                            
                    change = {
                                        'holding_days': holdingdays,
                                        'yd_pos_long': yd_pos,
                                        'td_pos_long': td_pos,
                                        'actual_yd_pos_long': yd_pos,
                                        'actual_td_pos_long': td_pos
                                    }
                    new_data = {"$set": change}
                    res = collection.update_one(
                                                query, new_data, True)
                    self.logger.info(f"[date_change_close] (res){res} (sid){sid} (change){change}")              

    def sync_position(self):
        try:
            for acc in self.accounts_run:
                ft_position_collection =  self.order_info_db[acc]['ft_position']
                account_id = self.account_id[acc]
                all_position_query = {"trade_acc": account_id}
                targets = ft_position_collection.find(all_position_query)
            
                if targets.count() > 0:
                    for pos in targets:
                        ticker = pos['ticker']
                        total_vol = pos['total_vol']
                        yd_vol = pos['avail_vol']
                        td_vol = total_vol - yd_vol
                        lock_vol = pos['lock_vol']
                        accountName = self.target_account_names[acc]
                        query = {'ticker': ticker, 'accountName': accountName}
                        EquityPosition_targets = self.order_info_db[acc]['EquityPosition'].find(query)
                        if EquityPosition_targets.count() == 0 and not pos['ticker'] == '' and not total_vol == 0:
                            self.add_position_for_debug(acc, pos, ticker, td_vol, yd_vol, accountName)
                        elif not pos['ticker'] == '':
                            td_vol_indb = 0
                            yd_vol_indb = 0
                            if EquityPosition_targets.count() == 1: #在同一ticker只有一单时可自动处理，否则需要前往数据库手动处理 
                                target_to_update = self.order_info_db[acc]['EquityPosition'].find_one(query)
                                td_vol_indb = target_to_update['actual_td_pos_long']
                                yd_vol_indb = target_to_update['actual_yd_pos_long']
                                total_vol_indb = td_vol_indb + yd_vol_indb
                                if  not total_vol == total_vol_indb:
                                        self.update_position(target_to_update ,acc, pos, ticker, td_vol, yd_vol, accountName)
                            else:
                                for target in EquityPosition_targets:
                                    sid = target['sid']
                                    td_vol_indb += target['actual_td_pos_long']
                                    yd_vol_indb += target['actual_yd_pos_long']
                                    self.logger.info(f"[sync_position] (ticker){ticker} (yd_vol_indb){yd_vol_indb} (td_vol_indb){td_vol_indb}")
                                total_vol_indb = td_vol_indb + yd_vol_indb
                                if  not total_vol == total_vol_indb: #在同一ticker只有一单时可自动处理，否则需要前往数据库手动处理
                                    sync_td_vol = td_vol - td_vol_indb
                                    sync_yd_vol = yd_vol - yd_vol_indb 
                                    self.add_position_for_debug(acc, pos, ticker, sync_td_vol, sync_yd_vol ,accountName)
                else:
                    self.logger.warning("[sync_position]can't_find_positions")
                                
                self.logger.info("[sync_position] sync_position_finished")
            
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[sync_position] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)

    def update_position(self, target, acc, pos, ticker, td_vol, yd_vol,accountName):
        try:
            collection = self.order_info_db[acc]['EquityPosition']
            sid = target['sid']
            update_filter = {'sid': sid}
            update_record = {
                'td_pos_long': td_vol,
                "yd_pos_long": yd_vol,
                'actual_td_pos_long' : td_vol,
                'actual_yd_pos_long' : yd_vol
            }
            new_data = {"$set": update_record}
            res = collection.update_one(update_filter, new_data)
            self.logger.info(f"[update_position] (res){res} (sid){sid} (msg){update_record}")
            
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[update_position] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)

    def add_position_for_debug(self, acc, pos, ticker, td_vol, yd_vol, accountName):
        try:
            collection = self.order_info_db[acc]['EquityPosition']
            #collection = self.test_trading_account['EquityPosition']
            exchange = int(pos['exchange'])
            order_collection = self.order_info_db[acc]['ft_order']
    
            total_vol = td_vol + yd_vol
            self.logger.warning(
                f'[add_position_for_debug] add_position (ticker){ticker} (total_vol){total_vol}')
            record = {}
            record['accountName'] = accountName
            record['ticker'] = ticker
            record['yd_pos_long'] = yd_vol
            record['yd_pos_short'] = 0
            record['td_pos_long'] = td_vol
            record['td_pos_short'] = 0
            record['actual_td_pos_long'] = td_vol
            record['actual_yd_pos_long'] = yd_vol
            # 持仓平均成本 非凸只返回仓位,无法计算cost,和market_value
            record['cost'] = 0
            record['mkt_value'] = 0
            record['enter_date'] = datetime.now(timezone.utc)
            record['holding_days'] = 0 
            record['sid'] = '[ADD]' + self.generate_sid(ticker)
            record['exchange'] = exchange
            filter = {'sid' : record['sid']}
            res = collection.replace_one(filter, record, True) 
            self.logger.info(f"[add_position_for_debug] (res){res} (msg){record}")
        except Exception as e:
            err = traceback.format_exc()
            self.logger.error(f'[add_position_for_debug] (exception){err}')
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)

    def generate_sid(self, ticker, exchange=None) -> str:
        sid = str(int(datetime.today().timestamp())) + '[T]' + ticker
        if exchange is not None:
            sid += '[E]' + str(exchange)
        return sid


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.') 

if __name__ == "__main__":

    description = "sync trade,pos,add for ftsever"    
    parser = argparse.ArgumentParser(description=description)
    
    _file_name = "C:\\Users\\Administrator\\Desktop\\ft_batandjson\\ft_fix_setting.json"
    _date = datetime.now().strftime("%Y%m%d")
    parser.add_argument('-m', '--config_filename', dest='config_filename', type=str, default=_file_name)
    parser.add_argument('-e', '--trade_date', dest='update_trade_date', type=str, default=_date)
    parser.add_argument('-t', '--sync_trade', dest='sync_trade', type=str2bool, default='T')
    parser.add_argument('-p', '--sync_pos', dest='sync_pos', type=str2bool, default='T')
    parser.add_argument('-a', '--sync_add', dest='sync_add', type=str2bool, default='F')
    
    args = parser.parse_args()
    print (f"(args){args}")

    td = FtTool(args.config_filename, args.update_trade_date, args.sync_pos, args.sync_trade, args.sync_add)
    
    td.start()  
