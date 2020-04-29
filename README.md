# African Parks Python Toolbox

An ArcGIS Python Toolbox for fetching remote data and automated analysis.

## About

Python Toolboxes are an interface for developing and distributing geoprocessing tools for ArcGIS Pro. This toolbox facilitates common data management and analysis tasks. Python Toolboxes are identified by the *.pyt* file format.

## Installing

#### 1. Clone or download this repository
#### 2. Place output/African Parks Toolbox.pyt somewhere convenient
> A good option is: Documents\ArcGIS\Projects\YOUR_PROJECT\

#### 2. In ArcGIS Pro, open the Catalog
> View > Catalog Pane

#### 3. Add the new Toolbox
> Right-click Toolboxes then select *Add Toolbox*

> Find and select *African Parks Toolbox.pyt*

## Tools

### Get Positions
The *Get Positions* tool is used to fetch remote data from EarthRanger. You can specify parameters such as EarthRanger credentials, source and a date range. The tool outputs a new Feature Class and Layer in the current workspace.

## Development
One of the limitations with Python Toolboxes is that ArcGIS Pro expects a .pyt file which is probably not supported by any code editor.
Furthermore, there are import issues when using packages, an important feature of any Python project!

We can get around these limitations by developing in Python as one normally would, then generating a *.pyt* as needed. The *setup.py* script does exactly this and outputs the *.pyt* file in the *outputs* directory.

To add a new tool, simply create a new file in the *src/tools* directory then declare the tool in *toolbox.py* under `# Tool names` like so `ToolName = object`.

To see changes in ArcGIS Pro close the toolbox, right-click the toolbox and select *Refresh*.