# convert-xml-dbdesigner-legacy-to-mysql
Conversion of the XML of the DER Bank (Entity Relationship Diagram) of SISCon Alberto's Registration (T2Ti Legacy)

## Question
 
 - Due to great difficulties in installing the 32-bit DBDesigner version on Linux (my processor is 64-bit), I found it necessary to convert the XML provided by T2TI to MySQL with the Python script and then perform the conversion with the help of Deepseek to the standard MySQL SQL. 

## Run Python script to generate default SQL based on XML

```shell
  python convert.py
```

 - For those who don't want to convert to SQL, the converted file already exists in this repository.
