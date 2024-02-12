from sqlalchemy import create_engine, select, asc
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from parser_cvs_to_bd import Market

class Sorter:
    
    def __init__(self) -> None:
        load_dotenv()
        engine = create_engine(f"postgresql+psycopg2://"
                               f"{os.getenv('USER')}:"
                               f"{os.getenv('PASSWORD')}@"
                               f"{os.getenv('IP')}:"
                               f"{os.getenv('PORT')}/"
                               f"{os.getenv('DBNAME')}",
            echo=False)
        
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.results = self.session.query(Market).all()
        stmt = select(Market.MarketName, Market.Website, Market.Youtube, 
                      Market.street, Market.city, Market.County)
        
        self.table_rows_2 = self.session.execute(stmt)

        self.table_rows = self.session.query(Market).all()
        self.field_names = (Market.__table__.columns.keys())

        self.name_colomns = self.session.execute(stmt).keys()
        
        self.dict_data = []
        self.all_data = []
        self.now_data = []
        
        self.list_format_data()
        self.list_format_data_2()
        
        self.sort_by_city(False)
            
    def list_format_data(self):
        for item in self.table_rows:
            temp_dict = []
            for field in self.field_names:
                temp_dict.append(str(getattr(item, field)))
            self.all_data.append(temp_dict)
            
    def list_format_data_2(self):
        for item in self.table_rows_2:
            temp_dict = []
            for field in self.name_colomns:
                temp_dict.append(str(getattr(item, field)))
            self.now_data.append(temp_dict)

    def sort_by_marketname(self, reverse = False):
        self.dict_data = sorted(self.dict_data, key=lambda x: x['MarketName'], reverse=reverse)
        self.all_data = sorted(self.all_data, key=lambda x: x[self.field_names.index('MarketName')], reverse=reverse)
        name_columns_list = list(self.name_colomns)
        self.now_data = sorted(self.now_data, key=lambda x: x[name_columns_list.index('MarketName')], reverse=reverse)

    def sort_by_city(self, reverse=False):
        self.dict_data = sorted(self.dict_data, key=lambda x: x['city'], reverse=reverse)
        self.all_data = sorted(self.all_data, key=lambda x: x[self.field_names.index('city')], reverse=reverse)
        name_columns_list = list(self.name_colomns)
        self.now_data = sorted(self.now_data, key=lambda x: x[name_columns_list.index('city')], reverse=reverse)
        
    def sort_by_youtube(self, reverse=False):
        self.dict_data = sorted(self.dict_data, key=lambda x: x['Youtube'], reverse=reverse)
        self.all_data = sorted(self.all_data, key=lambda x: x[self.field_names.index('Youtube')], reverse=reverse)
        name_columns_list = list(self.name_colomns)
        self.now_data = sorted(self.now_data, key=lambda x: x[name_columns_list.index('Youtube')], reverse=reverse)
        
    def sort_by_website(self, reverse=False):
        self.dict_data = sorted(self.dict_data, key=lambda x: x['Website'], reverse=reverse)
        self.all_data = sorted(self.all_data, key=lambda x: x[self.field_names.index('Website')], reverse=reverse)
        name_columns_list = list(self.name_colomns)
        self.now_data = sorted(self.now_data, key=lambda x: x[name_columns_list.index('Website')], reverse=reverse)
        
    def sort_by_county(self, reverse=False):
        self.dict_data = sorted(self.dict_data, key=lambda x: x['County'], reverse=reverse)
        self.all_data = sorted(self.all_data, key=lambda x: x[self.field_names.index('County')], reverse=reverse)
        name_columns_list = list(self.name_colomns)
        self.now_data = sorted(self.now_data, key=lambda x: x[name_columns_list.index('County')], reverse=reverse)
        
    def sort_by_street(self, reverse=False):
        self.dict_data = sorted(self.dict_data, key=lambda x: x['street'], reverse=reverse)
        self.all_data = sorted(self.all_data, key=lambda x: x[self.field_names.index('street')], reverse=reverse)
        name_columns_list = list(self.name_colomns)
        self.now_data = sorted(self.now_data, key=lambda x: x[name_columns_list.index('street')], reverse=reverse)   
        
            
if __name__ == '__main__':
    sorter = Sorter()
    
    sorter.list_format_data()  
    sorter.list_format_data_2()

    sorter.session.close()
