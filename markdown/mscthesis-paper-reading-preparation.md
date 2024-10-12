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


### Topic: data warehouse
#### 5. snowflake the original paper

The main difference of snowflake to other traditional
data warehouse technology is it is design for the benefit for __cloud__.
It's processing engine and most of other part are developed from scratch instead of using existing big data technology like hadoop.

#####  snowflake vs shared-nothing architectures

- Heterogeneous Workload

    In share-nothing architectures, multiple nodes usually have same hardware configuration. There could be two different type of tasks(one is I/O intensive the other is CPU intensive)
    This need the hardware to be configured in a trade-off with low average utilization.
    Platform like Amazon EC2 allow different instance type from which this share-nothing architectures cannot take advantage.

- Membership changes

    In the cloud concept, the node failures are more frequent and performance can vary even in the same type of nodes(EC2 instances). This could be a result of non-virtualized resources like network bandwidth. When it happens, data need to be reshuffled between nodes which will impact the system performance.

Snowflake solution: separates storage and compute. Storage in Amazon S3(blob store). Compute in snowflake shared-nothing engine.

__How SF shored data in S3__

❌ S3: No possible to append data the end of file instead of fully overwritten.

💡 Snowflake: Tables are horizontally partitioned into immutable files.

✅ S3: Support GET requests for parts of a file.

💡 Snowflake: Within each file, the values of same column or attribute are grouped together and heavily compressed. Each table file has a header contain the offsets of each column within the file.

