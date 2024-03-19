from sqlalchemy import create_engine, select, and_
from sqlalchemy.orm import sessionmaker


from models import Airlines, Airports, t_routes


class Sorter:
    """
    The Sorter class is responsible for sorting and filtering data related to airports and airlines.
    """

    def __init__(self) -> None:
        """
        Initializes the Sorter object.

        Loads environment variables, creates a database engine, and sets up a session.
        """
        engine = create_engine(
            "sqlite:///flight.db",
            echo=False
        )
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.field_names_pars = Airports.__table__.columns.keys()
        self.field_names = []

        self.field_names_pars_airlines = Airlines.__table__.columns.keys()
        self.field_names_airlines = []

        query = select([Airports.latitude, Airports.longitude])
        results = self.session.execute(query)

        self.coordinates = [
            (float(result[0]), float(result[1])) for result in results
        ]

        for field in self.field_names_pars:
            self.field_names.append(field)
        self.all_data = []

        for field in self.field_names_pars_airlines:
            self.field_names_airlines.append(field)

        self.sort_table_rows()

        self.all_data = self.list_format_data(
            self.table_rows, self.field_names_pars
        )

    def sort_table_rows(self):
        """
        Fetches all rows from the Airports and Airlines tables and stores them in instance variables.
        """
        self.table_rows = self.session.query(Airports).all()
        self.table_rows_airlines = self.session.query(Airlines).all()

    def list_format_data(self, table_rows, field_names_pars):
        """
        Formats the data from the given table rows and field names.

        Args:
            table_rows: List of table rows.
            field_names_pars: List of field names.

        Returns:
            List: Formatted data.
        """
        all_data = []
        for item in table_rows:
            temp_dict = []
            for field in field_names_pars:
                temp_dict.append(str(getattr(item, field)))
            all_data.append(temp_dict)
        return all_data

    def filter_lat_lon(self, values):
        """
        Filters airports based on latitude and longitude values.

        Args:
            values (dict): Dictionary containing 'min_lat', 'max_lat', 'min_lon', and 'max_lon'.

        Returns:
            List: Filtered data.
        """
        stmt = select(Airports.__table__.columns).\
            where(and_(Airports.latitude.between(values['min_lat'], values['max_lat']),
                       Airports.longitude.between(values['min_lon'], values['max_lon'])))
        result = self.session.execute(stmt)
        result = self.list_format_data(result, self.field_names)
        return result

    def filter_airlines_by_city(self, city_name):
        """
        Filters airlines based on the given city name.

        Args:
            city_name (str): The city name.

        Returns:
            List: Filtered data.
        """
        stmt = select(Airlines.__table__.columns).distinct().join(
            Airports, Airports.city == city_name)
        result = self.session.execute(stmt)
        result_list = [row for row in result]
        result_formatted = self.list_format_data(
            result_list, self.field_names_airlines)
        return result_formatted


if __name__ == '__main__':
    sorter = Sorter()
    airlines_from_city = sorter.filter_airlines_by_city("New York")
    print(airlines_from_city)
