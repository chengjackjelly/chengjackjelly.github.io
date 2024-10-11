## Master thesis preparation 

### Topic: data quality

#### 1. Automating Large-Scale Data Quality Verification [link](https://www.amazon.science/publications/automating-large-scale-data-quality-verification)



This article defines data quality in to following dimensions:
* completeness
* consistency
* accuracy

The main approach provided in this article is doing "Unit Test" to Data. This tool was then open sourced by Amazon teams, namely, __[deequ](https://github.com/awslabs/deequ?tab=readme-ov-file)__

This approach allow __user__ to define a set of __constraint__ for data quality checks. Then the __computable metrics__ should also be defined which provided a way to measure the current data quality regards to above mentioned three dimension. After these information and the verified data have been set up, the system inspects the checks and their constraints, and collects the metrics required to evaluate the checks. The output of the system will be a report showcase the qualification of the defined metrics on dataset.

The later part of article also mention how to extend this approach for __incrementally__ growing datasets(in the case of __ingestion pipelines__ in a __data warehouse__).

#### 2. Data quality challenges in large-scale cyber-physical systems [Link](https://www.sciencedirect.com/science/article/pii/S0306437921001484):

This article focus on a data quality management solution to detect errors in sensor nodes's measurement in large scale CPS systems.

Cyber-physical systems (CPSs) are integrated systems engineered to combine computational control
algorithms and __physical components__ such as sensors and actuators, effectively using an embedded
communication core.  __Large-scale CPSs__
are vulnerable to enormous technical and operational challenges that may compromise the quality of
data of their applications and accordingly reduce the quality of their services. 

This article defined following data quality dimensions:
- accuracy
- timeliness
- completeness
- consistency

This research use a methodology called SLR(systematic literature review) to understand the data quality main challenges while categorize them into above mentioned dimensions and proposed solution based on the SLR results.

[comment]: <> (TODO ### Topic:data warehouse ### Topic:big data analysts) 
### Topic: Big data, Smart manufacturing, data lifecycle

#### 3. An industrial big data pipeline for data‑driven analytics maintenance applications in large‑scale smart manufacturing facilities

This article provide a system design for an industrial big data pipeline of large-scale smart manufacturing facilities(IoT/CPS for example). Although it's not directly related to data quality, but still provide a through study of an information system model that provides a scalable and fault tolerant big data pipeline for integrating, processing and analyzing industrial equipment data.

#### 4. Data-driven smart manufacturing [link](https://www.sciencedirect.com/science/article/pii/S0278612518300062?casa_token=m2ie8GSzdEMAAAAA:m8AOpj3JMrqMFJ5iJEq4ebZ00c829r6hGGbgc_cOBZI0fHJoAwV88GzfjWwxzIxNm2k5J5NHRA)

This article covered all the aspect regards to the entire Lifecycle of manufacturing data. Could be used as a good start point and reference to understand our current situation.

The lifecycle included:
- Data source
- Data collection
- Data storage
- Data processing
- Data visualization
- Data transmission
- Data application
