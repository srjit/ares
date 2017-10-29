# Ares

*  Ares computes the pairwise similarity between a given list of documents stored in postgres.

* Setting up the program
  	  
   	   1. Browse to the directory of the downloaded code.
	   2. Run: sudo python3 setup.py install (this install the dependencies of the program)
	   3. Setting up the configuration
	      a) Open config.cfg in the code folder
	      b) Under postgres tab, add the connection details to the postgres database where
	      	 the program should connect to.
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

				  
		     	      
	      	  	      	 

	     	  