import arcpy
from datetime import datetime, timedelta


class FetchPositions(object):
    def __init__(self):
        self.label = "Fetch Positions!"
        self.description = "Fetches positions from a number of EarthRanger data sources."
        self.canRunInBackground = False
        self.maxDayRange = 30

    def getParameterInfo(self):

        source = arcpy.Parameter(
            displayName="Source",
            name="source",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        source.filter.type = "ValueList"
        source.filter.list = ['Elephants', 'Delormes']
        source.value = "Elephants"

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
            source,
            start_date,
            end_date,
        ]

    def updateParameters(self, parameters):
        pass

    def updateMessages(self, parameters):

        source, start_date, end_date = parameters[0], parameters[1], parameters[2]

        # make sure start is before end and difference does not exceed max_day_range
        if start_date.value and end_date.value:
            if end_date.value <= start_date.value:
                start_date.setErrorMessage("Start Date must be before End Date")
                end_date.setErrorMessage("End Date must be after Start Date")
            elif (end_date.value-start_date.value).days >= self.maxDayRange:
                start_date.setErrorMessage(f"Start Date must be less than {self.maxDayRange} days before End Date")
                end_date.setErrorMessage(f"End Date must be less than {self.maxDayRange} days after Start Date")
            else:
                start_date.clearMessage()
                end_date.clearMessage()
        else:
            start_date.clearMessage()
            end_date.clearMessage()

    def execute(self, parameters, messages):

        source, start_date, end_date = (
            parameters[0].valueAsText,
            parameters[1].value,
            parameters[2].value,
        )

        messages.addMessage(f'source = {source}')
        messages.addMessage(f'start_date = {start_date}')
        messages.addMessage(f'end_date = {end_date}')

        fc = self._create_feature_class(source)
        layer = self._create_feature_layer(source, fc)

        aprx = arcpy.mp.ArcGISProject('CURRENT')
        mxd = aprx.activeMap
        mxd.addLayer(layer)

        messages.addMessage('All done. Goodbye!')


    def _create_feature_class(self, source: str):

        fc = arcpy.CreateFeatureclass_management(
            out_path=arcpy.env.workspace,
            out_name=f'{source}_Positions_Feature_Class',
            geometry_type='Point',
            spatial_reference=4326
        )[0]

        arcpy.AddField_management(fc, "DatetimeRecorded", "DATE")
        return fc

    def _create_feature_layer(self, source: str, feature_class: str):
        return arcpy.MakeFeatureLayer_management(
            in_features=feature_class,
            out_layer=f'{source} Positions Feature Layer'
        )[0]



