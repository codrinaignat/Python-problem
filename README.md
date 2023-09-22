# Python-problem

1. Open and read the information from Database.txt
2. Create 5 lists for each basic function (the prefix of the Parameter_name value indicates the basic function PpDae – DAE (DriverActivityEstimation), Ada – ADA (ActionDecisionAsil), PpRpa – RPA (ReferencePointAdjustment), PpLv – LV (LaneVerification), Asq – ASQ (ActionSuppressionQM)), where the list elements are the lines from the text file (e.g [„string line1“, „string lineX“])
3. Define a function to create a list of dictionaries where the key and value pairs are obtain from the equality (there should be 6 pairs) (e.g. [{key1:value1, key2:value3}, {key1:value2, key2:value4}])
4. With the defined function create a single dictionary having the keys the names of the basic functions and the value the list of dictionaries (previously obtained) (e.g. {RPA:[{}, {}], DAE:[{}, {}]})
5. Using the obtained dictionary, print the Parameter_name value where the key „value“ has array (the type is defined as: type=„type[]“)
6. Using the obtained dictionary, print the Parameter_name where the key „lib:fusi “ is 1
7. Using the obtained dictionary, for the parameters of type Uint16, replace the „dd:MaxRange“ value which is different than the maximum value allowed by the data type (65 535)
8. Write the dictionary in a Output.txt file
![grafik](https://github.com/codrinaignat/Python-problem/assets/94629883/b90560df-ff6c-430b-b65c-15a6b84ff5b8)
