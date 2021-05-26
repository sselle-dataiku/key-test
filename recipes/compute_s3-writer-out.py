# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
s3_reader_in = dataiku.Dataset("s3-reader-in")
s3_reader_in_df = s3_reader_in.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc. 

s3_writer_out_df = s3_reader_in_df # For this sample code, simply copy input to output


# Write recipe outputs
s3_writer_out = dataiku.Dataset("s3-writer-out")
s3_writer_out.write_with_schema(s3_writer_out_df)
