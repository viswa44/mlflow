from flask import Flask, jsonify
import psycopg2
import pandas as pd


class RecModel:
    def __init__(self,conn):
        self.conn = conn
        pass

        
    def connect_to_likes(self):
        if conn:
            try:
                cur = conn.cursor()
                cur.execute('''
                            SELECT * 
                            FROM likes
                ''')
                sql_list = cur.fetchall()
                sql_df = pd.DataFrame(sql_list)
                # print(sql_df.head(15))
                return sql_df
            except Exception as e:
                print("no response ")
                return None
        return("not connected")
    
    def data_clean(self,sql_df):
        cleaned_df = sql_df.dropna()
        
        print(cleaned_df)
        return cleaned_df
    def recommendation_engine(self):
        
        return post_id
    
    
if __name__ == "__main__":
    try:
        conn = psycopg2.connect(database="nxtgovtestdb",
                                host="backup-newdev.cidtw9qpn6wx.ap-south-1.rds.amazonaws.com",
                                user="postgres",
                                password="!pSKPdJ3awx*9J9Xq",
                                port="5432")
        print("Database connected successfully for similar engine")
        cur = conn.cursor()
    except Exception as e:
        conn = None
        print(f"DB connection error for similar Engine: {str(e)}")
        
        
    if conn:
        reco = RecModel(conn)
        conn_attri = reco.connect_to_likes()
        cleaned_df = reco.data_clean(conn_attri)
        
