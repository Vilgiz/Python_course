from sqlalchemy import create_engine, select, asc
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from parser_cvs_to_bd import Market


class Sorter:
    
    def __init__(self) -> None:
        load_dotenv()
        engine = create_engine(f"postgresql+psycopg2://{os.getenv('USER')}:{os.getenv('PASSWORD')}@{os.getenv('IP')}:{os.getenv('PORT')}/{os.getenv('DBNAME')}",
            echo=False)
        
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.results = self.session.query(Market).all()
        stmt = select(Market.FMID, Market.MarketName, Market.Facebook)
        self.table_rows_2 = self.session.execute(stmt)

        self.table_rows = self.session.query(Market).all()
        self.field_names = Market.__table__.columns.keys()

        self.columns = self.session.execute(stmt).keys()
        
        
        
        self.dict_data = []
        self.list_data = []
        self.list_data_2 = []
        
        self.list_format_data()
        self.dict_format_data()
        self.list_format_data_2()


    def dict_format_data(self):
        for item in self.table_rows:
            temp_dict = {}
            for field in self.field_names:
                temp_dict[field] = str(getattr(item, field))
            self.dict_data.append(temp_dict)
            
    def list_format_data(self):
        for item in self.table_rows:
            temp_dict = []
            for field in self.field_names:
                temp_dict.append(str(getattr(item, field)))
            self.list_data.append(temp_dict)
            
    def list_format_data_2(self):
        for item in self.table_rows_2:
            temp_dict = []
            for field in self.columns:
                temp_dict.append(str(getattr(item, field)))
            self.list_data_2.append(temp_dict)


    def sort_by_marketname(self):
        test = select(Market).order_by(Market.MarketName).limit(10)
        self.result = self.session.execute(test)
    
        for result in self.result:
            #print(result.MarketName)
            print(result)

if __name__ == '__main__':
    sorter = Sorter()
    sorter.list_format_data()  
    sorter.dict_format_data()
    sorter.list_format_data_2()
    # print("####################################################################################")
    # print(sorter.dict_data[0])
    # print("####################################################################################")
    # print("####################################################################################")
    # print(sorter.list_data[0])
    # print("####################################################################################")
    # print("####################################################################################")
    # print(sorter.list_data_2[0])
    print("####################################################################################")
    sorter.sort_by_marketname()
    sorter.session.close()








""" print("############################################################")
for field_name in field_names:
    print(field_name)
print("############################################################")

results = session.query(Market.MarketName).all()
print("############################################################")
for result in results:
    print(result)
print("############################################################") """

# sorter = Sorter()

# print("############################################################")
# for result in results:
#     print(result)
# print("############################################################")