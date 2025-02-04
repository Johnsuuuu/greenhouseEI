# GreenhouseEI Documentation
## Dependencies
* numpy
* opencv

## Functionality
1. info(plant_ID, date, path)
* input: plant_ID, date, path
* output: print types of images that are available
* example: ```tools.info("JS39-65", "2018-04-11", "/Users/john/PycharmProjects/Library_SD/output")```
2. unzip(plant_ID, date, image_type, path):
* input: plant_ID, date, image_type, path
* output: the folder of images that match plant ID, date, and image type.
* example: ```tools.unzip("JS39-65", "2018-04-11", "Nir", "/Users/john/PycharmProjects/Library_SD/output")```
3. preprocess(plant_ID, date, path):
* input: plant_ID, date, path
* output: numpy arrays of Hyperspectral images
* example: ```tools.preprocess("JS39-65", "2018-04-11", "/Users/john/PycharmProjects/Library_SD/output")```
4. zip2np(plant_ID, date, path)
* input: plant_ID, date, path
* output: numpy arrays of Hyperspectral images from zip files.
* example: ```tools.zip2np("JS39-65", "2018-04-11", "/Users/john/PycharmProjects/Library_SD/output")```



## Running the library
1. Warnings
* There are two types of dataset. 
    1. The folder name of the old dataset contains "Schnable", such as "4-9-18_Schnable_49-281-JS39-65_2018-04-11_12-09-35_9968800.zip". The plant_ID of the old dataset should be in a format like "JS39-65", and the date should be in a format like "2018-04-11". 
    2. The folder name of the new dataset is like "71-001-Sesame-D-1.zip". The plant_ID of the new dataset should be in a format like "71-001-Sesame-D-1", and the date should be in a format like "2019-07-03".
* the possible image types are Hyp, Nir, Vis, Fluo, IR
* Hyperspectral images should be reconstructed first, before running the "preprocess" to produce the numpy array
2. import the module as a Python package
* `from greenhouseEI import tools`
* `tools.info([plant_ID], [date], [path])` 
* `tools.unzip([plant name], [date], [image type], [path])`
* `tools.preprocess([plant name], [date], [path])`
* `tools.zip2np([plant name], [date], [path])`
3. running the module in terminal 
* `python3 -m greenhouseEI.tools info -n JS39-65 -d 2018-04-11 -p /Users/john/PycharmProjects/Library_SD/output`
* `python3 -m greenhouseEI.tools unzip -n JS39-65 -d 2018-04-11 -t Hyp -p /Users/john/PycharmProjects/Library_SD/output`
* `python3 -m greenhouseEI.tools preprocess -n JS39-65 -d 2018-04-11 -p /Users/john/PycharmProjects/Library_SD`
* `python3 -m greenhouseEI.tools zip2np -n JS39-65 -d 2018-04-11 -p /Users/john/PycharmProjects/Library_SD/output`

## Demonstration
![](https://github.com/collincornman/greenhouseEI/blob/master/illustrations/greenhouseEI_guide.png)





