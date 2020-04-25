import arcpy
from datetime import datetime, timedelta


class FetchPositions(object):
    def __init__(self):
        self.label = "Fetch Positions"
        self.description = "Fetches positions from a number of EarthRanger data sources."
        self.canRunInBackground = False

    def getParameterInfo(self):

        start_date = arcpy.Parameter(
            displayName="Start Date",
            name="start_date",
            datatype="GPDate",
            parameterType="Required",
            direction="Input")
        start = datetime.now() - timedelta(days=7)
        start_date.value = start.strftime('%Y-%m-%d %H:%M:%S %p')

        end_date = arcpy.Parameter(
            displayName="End Date",
            name="end_date",
            datatype="GPDate",
            parameterType="Required",
            direction="Input")
        end = datetime.now()
        end_date.value = end.strftime('%Y-%m-%d %H:%M:%S %p')

        return [
            start_date,
            end_date,
        ]

    def updateParameters(self, parameters):
        pass

    def updateMessages(self, parameters):
        pass

    def execute(self, parameters, messages):
        pass
