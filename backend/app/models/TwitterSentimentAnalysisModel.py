from app.models import InitModel
from app.models.Connection import Connection


class TwitterSentimentAnalysisModel():

    def __init__(self):
        self.init_model = InitModel()
        self.sql = self.init_model.sql
        is_operation_exists = self.check_existing_operation()
        if (is_operation_exists == False):
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            cursor.execute(self.sql.sql_for_insert_sentiment_analysis_operation)
            conn.commit()
            conn.close()

    def update_twitter_sentiment_analysis_model(
            self,
            operation
    ):
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            query = getattr(self.sql, "sql_for_update_sentiment_analysis_operation").format(operation)
            cursor.execute(query)
            conn.commit()

        except Exception as ex:
            print('Error in TwitterSentimentAnalysisModel.update_twitter_sentiment_analysis_model(): {}'.format(str(ex)))
        finally:
            conn.close()

    def get_twitter_sentiment_analysis_operation_data(self):
        data = []
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            cursor.execute(self.sql.sql_to_get_sentiment_analysis_operation)
            rows = cursor.fetchall()
            for each_row in rows:
                data.append(dict(zip([c[0] for c in cursor.description], each_row)))
            return data

        except Exception as ex:
            print('Error in TwitterSentimentAnalysisModel.get_twitter_sentiment_analysis_operation_data(): {}'.format(str(ex)))
            return data
        finally:
            conn.close()

    def check_existing_operation(self):
        try:
            connection_obj = Connection()
            conn = connection_obj.connection
            cursor = conn.cursor()
            query = getattr(self.sql, "sql_for_check_operation")
            row = cursor.execute(query).fetchone()
            if row[0] < 1:
                return False
            else:
                return True

        except Exception as ex:
            print('Error in TwitterSentimentAnalysisModel.check_existing_operation(): {}'.format(str(ex)))
            return False
        finally:
            conn.close()