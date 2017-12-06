# Ares

*  Ares computes the pairwise similarity between a given list of documents stored in postgres.

* Setting up the program
  	  
   	   1. Browse to the directory of the downloaded code.
	   2. Run: sudo python3 setup.py install (this install the dependencies of the program)
	   3. Setting up the configuration
	      a) Open config.cfg in the code folder
	      b) Under postgres tab, add the connection details to the postgres database where
	      	 the program should connect to.

* Setting the vectorizer
  	  One of the two vectorizers have to be configured, before the program starts. This can be set
	  by the "type" keyword. The value of this keyword has to one of the following options :
	     
	     a) scikit
	     b) word2vec
	     	
          For using the google word2vec model, the key "word2vec_model_loc" in the config file has to be set.
	  This has to point to the filesystem location of the word2vec binary model.
	       
	  N.B: The model is available for download at the following drive location:
	       	  https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

* Other dependencies:
	Readcalc package for python used in the program requires boilerpipe as a dependency

		 a) Install https://github.com/misja/python-boilerpipe
	Either of the following two options has to be set in the config under scores type if readabiity scores have to be calculated.
	         a) textstat
		 b) readcalc
		     
* Running the program
  	  
	      The main file of the code is 'process.py'. Browse to the code directory and execute
	      this file by: *python process.py*

* Outputs

	** Upon successful run of the program the following tables will be created in the configured
	      database:
		
		a) documents - cleaned documents and their text statistics with an index
		   	 Columns:
				* index
				* processed_value
				* word_count
				* gunning_fog
				* reading_ease
				* smog_index
				* automated_readability_index
				* coleman_liau_index
				* linsear_write_formula
				* dale_chall_readability_score

		b) similarity - computed similarity between documents
		   	 Columns:
				* index1
				* index2
				* similarity

				  
		     	      
	      	  	      	 

	     	  