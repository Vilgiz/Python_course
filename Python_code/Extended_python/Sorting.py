from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from parser_cvs_to_bd import Market


class Sorter:
    
    def __init__(self) -> None:
        engine = create_engine('postgresql+psycopg2://postgres:cf79db54Q@localhost:6969/test_db', echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.results = self.session.query(Market).all()
    
        self.table_rows = self.session.query(Market).all()
        self.field_names = Market.__table__.columns.keys()
        self.list_rows_table = []
        self.list_1 = []
        self.list_f()
        self.print_results()

    def print_results(self):
        for item in self.table_rows:
            temp_dict = {}
            for field in self.field_names:
                temp_dict[field] = str(getattr(item, field))
            self.list_rows_table.append(temp_dict)
            
    def list_f(self):
        for item in self.table_rows:
            temp_dict = []
            for field in self.field_names:
                temp_dict.append(str(getattr(item, field)))
            self.list_1.append(temp_dict)





if __name__ == '__main__':
    sorter = Sorter()
    sorter.print_results()
    sorter.list_f()
    print("####################################################################################")
    print(sorter.list_rows_table[0])
    print("####################################################################################")
    print("####################################################################################")
    print(sorter.list_1[0])
    print("####################################################################################")
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