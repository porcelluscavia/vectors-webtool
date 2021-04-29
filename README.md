Dr. Fritz's Vector Site
=====

Interface for exploring semantic spaces.  The interface can be run either
locally or as a web server. 

If you wish to modify this code, it's helpful to have a decent understanding of Python, HTML, CSS. A basic understanding of APIs and making websites is also handy. Familiarity with the Python libraries Pandas, Flask, and scikit-learn can be helpful.

You'll probably seek to modify one of the following files:
- **space.py, space_io.py, space_utils.py** - several utility classes that handle taking in and storing a vector space file. Each vector file becomes an object called a Semspace. The Semspace class contains a number of functions to perform our desired distance calculations (e.g. nearest neighbors, pairwise, etc.) and return results as Pandas dataframes. The actual distance calculations are performed with scikit-learn.
- **index.html** - the frontend layout is built here. You can add any new HTML structures you like, but the current page uses Bootstrap v3. So you can add many pre-built, pre-styled HTML components from [their webpage](https://getbootstrap.com/docs/3.3/components/). Through ID tags ("id=...") placed within a components, the javascript can find and make use of the input captured by that component.
- **snaut.js** - javascript file that links the frontend to the Python code. It receives input from the text boxes/selection menus in the frontend, performs any neccessary preprocessing, then stores them as JSON objects (easily interpretable objects consisting of attribute–value pairs) that can be used by the Python code. This is also where the typeahead function for the image search box occurs. The Python code also sends back results through the javascript to be displayed through the frontend.
- **snaut.py** -  receives JSON objects from javascript, loads in Semspaces (in our current site there are 3 vector files/Semspaces: prototypes, images, and both). Then it passes JSON information (chosen metric, words inputted into text box, etc.) to Semspace functions to get desired calculations, then sometimes returns a JSON to be sent back to the javascript (if the result is to be displayed on the webpage, as in nearest neighbors) or prepares a csv for direct download).  All non-helper functions are associated with API (Flask) endpoints.


For more information see [website](http://crr.ugent.be/snaut/).

Snaut uses the `semspaces` module. See
[here](http://github.com/pmandera/semspaces/) for more information.

# Semantic spaces

You can download a set of validated semantic spaces for English and Dutch
[here](http://zipf.ugent.be/snaut/spaces/) (see Mandera, Keuleers, & Brysbaert,
in press). 

# Contribute 

- Issue Tracker: https://github.com/pmandera/snaut/issues
- Source Code: https://github.com/pmandera/snaut

# Authors

The tool was developed at Center for Reading Research, Ghent University by
[Paweł Mandera](http://crr.ugent.be/pawel-mandera).

# License

The project is licensed under the Apache License 2.0.

# References

Mandera, P., Keuleers, E., & Brysbaert, M. (in press). Explaining human
performance in psycholinguistic tasks with models of semantic similarity based
on prediction and counting: A review and empirical validation. *Journal of
Memory and Language*.
