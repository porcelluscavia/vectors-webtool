Dr. Fritz's Vector Site
=====

Interface for exploring semantic spaces.  The interface can be run either
locally or as a web server. 

If you wish to modify this code, it's helpful to have a decent understanding of Python, HTML, CSS. A basic understanding of APIs and making websites is also handy. Familiarity with the Python libraries Pandas, Flask, and scikit-learn can be helpful.

# Making changes on the existing Pythonanywhere version

Please see [the wiki for this repository](https://github.com/porcelluscavia/vectors-webtool/wiki)


# Running a copy on your local machine (to develop the app further)

Download the project from this git repository, install all Python requirements in requirements.txt. Paths may have to be changed in the configuration file "/home/vectorswebtool/vectors-webtool/config.ini," especially to add the path for the vector space on your local machine, which you should put into the /data/ folder.

Then, simply run the python file "/home/vectorswebtool/vectors-webtool/snaut-english/snaut.py" in your favorite Python IDE and go to http://localhost:15100/ if it doesn't open automatically.

It may reload several times over the course of a few minutes before you see the site, especially if the vector space is large. Don't worry, this is normal behavior.


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
