from . import sqlconnection
from . import us_states_table,StateRecordBase,StateRecord
import sqlalchemy as db
import logging
from util.logutil import logstartenddef
logger = logging.getLogger()

class us_states_dao:
    """ a class that encapsulates all data operations for us_states table """
    @logstartenddef
    def read(self):
        """reads all records and returns a list

        :rtype: list
        """
        connection,engine = sqlconnection().getAlchemyConnection()
        query = us_states_table.select()
        proxy = connection.execute(query)
        resultSet = proxy.fetchall()
        
        return resultSet
    
    @logstartenddef
    def update(self,id: int, baserecord: StateRecordBase):
        """updates record and return code,
        0 = sucess , 1 = failure, 2 = record not found
        :id arg: id of record to update
        :type arg: int
        :baserecord arg: json dict of record to update
        :type arg: StateRecordBase
        :rtype: tuple
        """
        try:
            connection,engine = sqlconnection().getAlchemyConnection()
        
            query = us_states_table.select().where(id == us_states_table.c.id)
            result = connection.execute(query)
            row = result.fetchone()

            if row is not None:
                # if item is found in database update
                query = (
                us_states_table
                .update()
                .where(id == us_states_table.c.id)
                .values(
                    record_date = baserecord.record_date,
                    state = baserecord.state,
                    fips = baserecord.fips,
                    cases = baserecord.cases,
                    deaths = baserecord.deaths,
                    confirmed_cases = baserecord.confirmed_cases,
                    confirmed_deaths = baserecord.confirmed_deaths,
                    probable_cases = baserecord.probable_cases,
                    probable_deaths = baserecord.probable_deaths
                )
        
                )
                result = connection.execute(query)
        
                output = baserecord
            
            else: 
                # if record not found in database then return 2
                return None,2
            
        except Exception as e:
            # in case of error return 1 as code
            logger.error("error while deleting",exc_info=1)
            return None,1

        return output,0

    
    @logstartenddef
    def insert(self,baserecord: StateRecord):
        """inserts record and returns inserted record with id,
        s
        :baserecord arg: json dict of record to update
        :type arg: StateRecordBase
        :rtype: StateRecord
        """
        connection,engine = sqlconnection().getAlchemyConnection()
        query = us_states_table.insert().values(
            record_date = baserecord.record_date,
            state = baserecord.state,
            fips = baserecord.fips,
            cases = baserecord.cases,
            deaths = baserecord.deaths,
            confirmed_cases = baserecord.confirmed_cases,
            confirmed_deaths = baserecord.confirmed_deaths,
            probable_cases = baserecord.probable_cases,
            probable_deaths = baserecord.probable_deaths)
        result = connection.execute(query)
        logger.debug(f'primary key{result.inserted_primary_key}')
        output = {
            'id':int(result.inserted_primary_key[0]),
            'record_date' : baserecord.record_date,
            'state' : baserecord.state,
            'fips' : baserecord.fips,
            'cases' : baserecord.cases,
            'deaths' : baserecord.deaths,
            'confirmed_cases' : baserecord.confirmed_cases,
            'confirmed_deaths' : baserecord.confirmed_deaths,
            'probable_cases' : baserecord.probable_cases,
            'probable_deaths' : baserecord.probable_deaths
        }
        
        return output
    
    @logstartenddef
    def delete(self,recordId: int):
        """deletes record and return code,
        0 = sucess , 1 = failure, 2 = record not found
        :id arg: id of record to update
        :type arg: int

        :rtype: int
        """
        try:
            connection,engine = sqlconnection().getAlchemyConnection()
        
            query = us_states_table.select().where(recordId == us_states_table.c.id)
            result = connection.execute(query)
            row = result.fetchone()

            if row is not None:
                query = us_states_table.delete().where(recordId == us_states_table.c.id)
                result = connection.execute(query)
            
            else: 
                return 2
            
        except Exception as e:
            logger.error("error while deleting",exc_info=1)
            return 1
            

        
        return 0
    
    
        

        

