\# Project Specific/Third Level Annotations: \### These are the
guidelines for my project-specific annotations, i.e. not included in the
guidelines. These are primarily used for me to effectively sort,
differentiate, and catagorize data in ArcGIS Pro.

\* \*\*river\*\* Used to identify rivers. Gazetteers create reference
points that contain the data for rivers, but when actually mapping, a
river is \_not\_ mapped with \_point data\_ but as a \_polyline\_ (or a
polygon, depending on the scale of the map). Therefore, a river tag is
necessary to separate these reference points from the rest of the point
data, since they need to be manually converted to polyline data.

\* \*\*region\*\* Used to identify geographic regions. Gazetteers create
reference points that contain the data for regions, but when actually
mapping, a region is \_not\_ mapped with \_point data\_ but as a
\_polygon\_. Therefore, a region tag is necessary to separate these
reference points from the rest of the point data, since they need to be
manually converted to polygon data. Regions are not labeled with
.referenced or .visited, since they need to be manually plotted out
regardless, and it should be evident whether or not the journey polyline
passes through them.

\* \*\*town/City/Settlement\*\* \> I will revisit this section and break
it up into multiple tags. Basically, this is a tag for point data to
record how Xenophon talks about a location as he saw it (was it a "large
and prosperous" city? Just a village? Abandoned?)

\* \*\*visited\*\* Used for a city, settlement, landmark, or some other
specific location that is \_point data only\_ (in ArcGIS) that has been
directly visited by the Ten Thousand. These will be used to chart the
journey of the Ten Thousand and will be connected by a polyline.

\* \*\*referenced\*\* Used for a city, settlement, landmark, or some
other specific location that is \_point data only\_ (in ArcGIS) that has
not been directly visited by the Ten Thousand, but nonetheless has
georeferenced data. Often used for ethnonyms, demonyms, or cities
mentioned as context.

\*\*ambiguous\*\* A catch-all tag---typically used for point data---that
denotes if a location is unlocated, has a significantly contested
location, or is otherwise ambiguous in where it is specifically,
geographically supposed to be. Often used for lost cities, which crop up
more than you'd think.

\* \*\*casestudy\*\* A subjective tag used for specific instances or
entities that serve as poignant examples, either because of their
complexity or simplicity, that can illustrate a specific point.

\* \*\*analysis\*\* \_Used in the mapping phase only!\_ A tag used to
denote which points have been created via analysis; often follows an
.ambiguous tag, since visited, ambiguous cities need to be mapped. For
example, if the Ten Thousand pass through a lost city with no clear
modern location (ex. Ceramon-agora), an estimated location has to be
determined via different analyses to properly chart a route for the Ten
Thousand.
